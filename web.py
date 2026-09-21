
import streamlit as st
import pandas as pd
from pathlib import Path
import urllib.parse
from PIL import Image, ImageOps
import io, zipfile

APP_DIR = Path(__file__).parent
st.set_page_config(page_title="JT AGRITECH SOLUTIONS", page_icon="🌱", layout="wide")

st.markdown("""
<style>
div[data-testid="stMetric"]{background:white;border-radius:15px;padding:15px;box-shadow:0 4px 12px rgba(34,85,34,0.08);border-left:5px solid #225522;}
</style>
""", unsafe_allow_html=True)

def find_file(names):
    for n in names:
        p = APP_DIR / n
        if p.exists():
            return p
    return None

logo_path = find_file(["logo.png", "photo1073368801732108452.jpeg", "logo.jpg"])
affiche_path = find_file(["affiche-bienvenue.jpg", "affiche-bienvenu.jpg", "profil-whatsapp.jpg"])

c1,c2 = st.columns([1,4])
with c1:
    if logo_path:
        st.image(str(logo_path), width=100)
with c2:
    st.markdown("<h1 style='margin:0;color:#225522;'>JT AGRITECH SOLUTIONS</h1><p style='margin:0;color:#5a7a3a;font-weight:700;'>Au service des paysans</p>", unsafe_allow_html=True)
st.divider()

fichier = APP_DIR / "eleveurs.xlsx"
if fichier.exists():
    df = pd.read_excel(fichier)
else:
    df = pd.DataFrame(columns=["nom","telephone","quartier","bacs","date_livraison","statut_livraison","statut_paiement","statut_recolte"])

for col, default in [("statut_livraison","En attente"),("statut_paiement","Non payé"),("statut_recolte","Non livrée")]:
    if col not in df.columns:
        df[col] = default

with st.sidebar:
    if logo_path:
        st.image(str(logo_path), width=80)
    menu = st.radio("MENU", ["📊 Tableau de bord", "➕ Ajouter éleveur", "💬 Messages WhatsApp"])

def create_card(row):
    W,H = 1080,1080
    white_band = Image.new('RGB', (W, 500), (255,255,255))
    if affiche_path:
        try:
            base = Image.open(affiche_path).convert("RGB")
            base = ImageOps.fit(base, (W,H), method=Image.Resampling.LANCZOS, centering=(0.5,0.35))
            img = base.copy()
            img.paste(white_band, (0,0))
        except Exception as e:
            img = Image.new('RGB', (W,H), (245,248,240))
            img.paste(white_band, (0,0))
    else:
        img = Image.new('RGB', (W,H), (245,248,240))
        img.paste(white_band, (0,0))

    from PIL import ImageDraw, ImageFont
    draw = ImageDraw.Draw(img)
    if logo_path:
        try:
            logo = Image.open(logo_path).convert("RGBA")
            logo.thumbnail((150,150))
            img.paste(logo, (35,15), logo)
        except:
            pass
    try:
        fb = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 52)
        fm = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 36)
        fs = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 32)
    except:
        fb = ImageFont.load_default()
        fm = fb
        fs = fb

    draw.rectangle([30,150,W-30,156], fill=(143,188,95))
    draw.text((210,25), "JT AGRITECH SOLUTIONS", fill=(34,85,34), font=fb)
    draw.text((210,85), "Au service des paysans", fill=(80,80,80), font=fs)
    draw.text((35,175), f"Bonjour {str(row['nom']).upper()},", fill=(0,0,0), font=fb)
    draw.text((35,245), f"Quartier: {row['quartier']} | Bacs: {row['bacs']}", fill=(0,0,0), font=fm)
    draw.text((35,295), f"Livraison: {row['date_livraison']}", fill=(0,0,0), font=fm)
    draw.text((35,345), f"Paiement: {row['statut_paiement']} | Recolte: {row['statut_recolte']}", fill=(34,85,34), font=fm)
    draw.text((35,395), f"Tel: {row['telephone']}", fill=(60,60,60), font=fs)
    return img

if "Tableau" in menu:
    total = len(df)
    total_payes = len(df[df["statut_paiement"]=="Payé"]) if total>0 else 0
    total_recoltes = len(df[df["statut_recolte"]=="Livrée"]) if total>0 else 0
    total_bacs = int(df["bacs"].sum()) if total>0 and "bacs" in df.columns else 0
    en_attente = len(df[df["statut_livraison"]=="En attente"]) if total>0 else 0
    m1,m2,m3,m4,m5 = st.columns(5)
    m1.metric("👨‍🌾 TOTAL ELEVEURS", total)
    m2.metric("💰 TOTAL PAYES", total_payes)
    m3.metric("🚜 RECOLTES LIVREES", total_recoltes)
    m4.metric("📦 BACS TOTAUX", total_bacs)
    m5.metric("⏳ EN ATTENTE", en_attente)

    st.markdown("### 📋 LISTE DES ELEVEURS")
    if df.empty:
        st.info("Aucun éleveur")
    else:
        html_table = """
        <style>
       .table-jt {width:100%; border-collapse: collapse; border-radius:12px; overflow:hidden; box-shadow:0 2px 10px rgba(0,0,0,0.05);}
       .table-jt th {background-color:#225522; color:white; text-transform:uppercase; font-weight:800; padding:14px 10px; text-align:left; font-size:13px; letter-spacing:0.5px;}
       .table-jt td {padding:12px 10px; background-color:#f4f9ec; border-bottom:1px solid #e0e8d5; font-size:14px;}
       .table-jt tr:nth-child(even) td {background-color:#eaf3de;}
       .table-jt tr:hover td {background-color:#dbe9c8;}
        </style>
        <table class="table-jt"><thead><tr>
        """
        for col in df.columns:
            html_table += f"<th>{str(col).upper()}</th>"
        html_table += "</tr></thead><tbody>"
        for _, r in df.iterrows():
            html_table += "<tr>"
            for val in r:
                html_table += f"<td>{val}</td>"
            html_table += "</tr>"
        html_table += "</tbody></table>"
        st.markdown(html_table, unsafe_allow_html=True)

        st.divider()
        st.markdown("### ✏️ MODIFIER / SUPPRIMER / METTRE À JOUR")
        eleveur = st.selectbox("Choisis l'éleveur à modifier", df["nom"].tolist())
        idx = df[df["nom"]==eleveur].index[0]
        row = df.loc[idx]
        with st.form("modif_form"):
            cA,cB = st.columns(2)
            with cA:
                n = st.text_input("NOM", row["nom"])
                t = st.text_input("TELEPHONE", str(row["telephone"]))
                q = st.text_input("QUARTIER", str(row["quartier"]))
                b = st.number_input("BACS", value=int(row["bacs"]) if str(row["bacs"]).isdigit() else 1, min_value=1)
            with cB:
                d = st.text_input("DATE LIVRAISON", str(row["date_livraison"]))
                s_liv = st.selectbox("STATUT LIVRAISON BACS", ["En attente","Livré"], index=0 if row["statut_livraison"]=="En attente" else 1)
                s_pay = st.selectbox("STATUT PAIEMENT", ["Non payé","Payé","Partiel"], index=["Non payé","Payé","Partiel"].index(row["statut_paiement"]) if row["statut_paiement"] in ["Non payé","Payé","Partiel"] else 0)
                s_rec = st.selectbox("STATUT RÉCOLTE LIVRÉE", ["Non livrée","Livrée"], index=0 if row["statut_recolte"]=="Non livrée" else 1)
            col_save, col_del = st.columns(2)
            save = col_save.form_submit_button("💾 ENREGISTRER", type="primary", use_container_width=True)
            delete = col_del.form_submit_button("🗑️ SUPPRIMER", use_container_width=True)
            if save:
                df.loc[idx, ["nom","telephone","quartier","bacs","date_livraison","statut_livraison","statut_paiement","statut_recolte"]] = [n,t,q,b,d,s_liv,s_pay,s_rec]
                df.to_excel(fichier, index=False); st.success(f"✅ {n} mis à jour!"); st.rerun()
            if delete:
                df = df.drop(idx).reset_index(drop=True); df.to_excel(fichier, index=False); st.warning("Supprimé"); st.rerun()

elif "Ajouter" in menu:
    st.subheader("➕ AJOUTER ELEVEUR")
    with st.form("add_form"):
        col1,col2 = st.columns(2)
        with col1:
            nom = st.text_input("NOM *"); tel = st.text_input("TELEPHONE WHATSAPP *"); quartier = st.text_input("QUARTIER *")
        with col2:
            bacs = st.number_input("BACS", min_value=1, value=2); date_liv = st.text_input("DATE LIVRAISON"); statut_pay = st.selectbox("PAIEMENT", ["Non payé","Payé"])
            statut_rec = st.selectbox("RÉCOLTE", ["Non livrée","Livrée"])
        if st.form_submit_button("✅ ENREGISTRER", type="primary", use_container_width=True):
            if nom and tel:
                new = {"nom":nom,"telephone":tel,"quartier":quartier,"bacs":bacs,"date_livraison":date_liv,"statut_livraison":"En attente","statut_paiement":statut_pay,"statut_recolte":statut_rec}
                df = pd.concat([df, pd.DataFrame([new])], ignore_index=True)
                df.to_excel(fichier, index=False); st.success(f"{nom} ajouté!"); st.balloons()
            else:
                st.error("Nom et téléphone obligatoires")
else:
    if df.empty:
        st.warning("Ajoute d'abord un éleveur")
    else:
        tab_indiv, tab_tous = st.tabs(["👤 ENVOI INDIVIDUEL", "📢 ENVOI À TOUS"])
        with tab_indiv:
            eleveur_nom = st.selectbox("CHOISIS ELEVEUR", df["nom"].tolist(), key="sel_indiv")
            row = df[df["nom"]==eleveur_nom].iloc[0]
            card = create_card(row)
            buf = io.BytesIO(); card.save(buf, format="JPEG", quality=95); buf.seek(0)
            col_img, col_msg = st.columns([1,1])
            with col_img:
                st.markdown("**CARTE PERSONNALISÉE (NON DÉFORMÉE)**")
                st.image(card, use_container_width=True)
                st.download_button("📥 TÉLÉCHARGER CARTE HD", buf, file_name=f"JT_{row['nom']}.jpg", mime="image/jpeg", type="primary", use_container_width=True)
            with col_msg:
                msg = f"""🌱 BIENVENUE CHEZ JT AGRITECH SOLUTIONS
Au service des paysans

Bonjour {row['nom']},

📍 Quartier: {row['quartier']}
📦 Bacs: {row['bacs']}
📅 Livraison: {row['date_livraison']}
💰 Paiement: {row['statut_paiement']}
🚜 Récolte: {row['statut_recolte']}

Inscription confirmée.
JT AGRITECH SOLUTIONS"""
                st.markdown("**MESSAGE WHATSAPP**")
                st.text_area("Message", msg, height=320, label_visibility="collapsed")
                tel = str(row['telephone']).replace(" ","").replace("+","")
                if not tel.startswith("237") and len(tel)>=9:
                    tel="237"+tel[-9:]
                wa_link = f"https://wa.me/{tel}?text={urllib.parse.quote(msg)}"
                st.markdown(f"""<a href="{wa_link}" target="_blank" style="text-decoration:none;"><div style="background:#25D366;color:white;padding:14px;border-radius:12px;text-align:center;font-weight:700;display:flex;justify-content:center;align-items:center;gap:10px;"><img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="22" style="filter:brightness(0) invert(1);"> OUVRIR WHATSAPP POUR {str(row['nom']).upper()}</div></a>""", unsafe_allow_html=True)
        with tab_tous:
            st.markdown(f"**ENVOI GROUPÉ À {len(df)} ELEVEURS RÉPERTORIÉS**")
            msg_tous = f"""🌱 JT AGRITECH SOLUTIONS - MESSAGE GROUPÉ
Vous êtes {len(df)} éleveurs.
{len(df[df['statut_paiement']=='Payé'])} ont déjà payé.
{len(df[df['statut_recolte']=='Livrée'])} ont déjà livré leur récolte.
Merci.
JT AGRITECH"""
            st.text_area("Message pour TOUS", msg_tous, height=200)
            if st.button(f"⚙️ GÉNÉRER ZIP DES {len(df)} CARTES", type="primary", use_container_width=True):
                zb = io.BytesIO()
                with zipfile.ZipFile(zb, "w", zipfile.ZIP_DEFLATED) as zf:
                    for _, r in df.iterrows():
                        c = create_card(r)
                        b = io.BytesIO(); c.save(b, format="JPEG", quality=90); b.seek(0)
                        zf.writestr(f"JT_{r['nom']}.jpg", b.getvalue())
                zb.seek(0)
                st.download_button(f"📥 TÉLÉCHARGER ZIP {len(df)} CARTES", zb, file_name=f"JT_AGRITECH_{len(df)}_CARTES.zip", mime="application/zip", type="primary", use_container_width=True)
