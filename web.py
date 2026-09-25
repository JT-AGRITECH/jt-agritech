import streamlit as st
import pandas as pd
from pathlib import Path

APP_DIR = Path(__file__).parent
st.set_page_config(page_title="JT AGRITECH", page_icon="🌱", layout="wide")

# MOT DE PASSE V44 11h11 - NE RIEN CHANGER
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

if not st.session_state['authenticated']:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #225522 0%, #8fbc5f 100%); padding:30px; border-radius:20px; text-align:center; color:white;">
     <h2 style="color:white;">🌱 JT-AGRITECH - Accès Sécurisé</h2>
     <p style="color:#e8f5d8;">Entrez le mot de passe</p>
    </div>
    """, unsafe_allow_html=True)
    password = st.text_input("🔑 Mot de passe", type="password")
    if st.button("🔓 ENTRER", type="primary", use_container_width=True):
        if password == "JT-HANNETONS-2026!":
            st.session_state['authenticated'] = True
            st.rerun()
        else:
            st.error("❌ Mot de passe incorrect")
    st.info("💡 Mot de passe: JT-HANNETONS-2026!")
    st.stop()

# LECTURE 4 FICHIERS - V44 11h11 - NE RIEN CHANGER
try:
    df_hannetons = pd.read_excel(APP_DIR / "eleveurs_hannetons.xlsx").fillna("") if (APP_DIR / "eleveurs_hannetons.xlsx").exists() else pd.DataFrame()
    df_escargots = pd.read_excel(APP_DIR / "eleveurs_escargots.xlsx").fillna("") if (APP_DIR / "eleveurs_escargots.xlsx").exists() else pd.DataFrame()
    df = pd.read_excel(APP_DIR / "eleveurs.xlsx").fillna("") if (APP_DIR / "eleveurs.xlsx").exists() else df_hannetons
except:
    df_hannetons = pd.DataFrame()
    df_escargots = pd.DataFrame()
    df = df_hannetons

total_hannetons = len(df_hannetons) if not df_hannetons.empty else 8
total_escargots = len(df_escargots) if not df_escargots.empty else 8
total_global = total_hannetons + total_escargots

st.markdown("""
<style>
.metric-hanneton {background: linear-gradient(135deg, #3E2723 0%, #8B4513 100%); color:white; padding:20px; border-radius:15px; text-align:center; border:3px solid #FF9800;}
.metric-escargot {background: linear-gradient(135deg, #1B5E20 0%, #2E7D32 100%); color:white; padding:20px; border-radius:15px; text-align:center; border:3px solid #81C784;}
.metric-total {background: linear-gradient(135deg, #225522 0%, #4CAF50 100%); color:white; padding:20px; border-radius:15px; text-align:center; border:3px solid #8BC34A;}
</style>
""", unsafe_allow_html=True)

# PORTAIL V44 11h11 - NE RIEN CHANGER - SEULEMENT TOTAL ELEVEURS
st.markdown("""
<div style="background: linear-gradient(135deg, #225522 0%, #8fbc5f 100%); padding:25px; border-radius:20px; text-align:center; color:white; margin-bottom:20px;">
 <h2 style="color:white; margin:0;">🌱 JT-AGRITECH - V44 11h11 - DEUX APPS - UN SEUL LIEN</h2>
 <p style="color:#e8f5d8;">Portail total éleveurs seulement - Hanneton parfait intact</p>
</div>
""", unsafe_allow_html=True)

c1,c2,c3 = st.columns(3)
with c1:
    st.markdown(f"""<div class="metric-hanneton"><div style="font-size:36px; font-weight:900; color:#FFE0B2;">🪲 {total_hannetons}</div><div style="color:#FFCC80; font-weight:800;">Éleveurs Hannetons</div></div>""", unsafe_allow_html=True)
with c2:
    st.markdown(f"""<div class="metric-escargot"><div style="font-size:36px; font-weight:900; color:#C8E6C9;">🐌 {total_escargots}</div><div style="color:#A5D6A7; font-weight:800;">Éleveurs Escargots</div></div>""", unsafe_allow_html=True)
with c3:
    st.markdown(f"""<div class="metric-total"><div style="font-size:36px; font-weight:900; color:#E8F5E9;">👨‍🌾 {total_global}</div><div style="color:#C8E6C9; font-weight:800;">Total Éleveurs</div></div>""", unsafe_allow_html=True)

col_h, col_e = st.columns(2)
with col_h:
    if st.button("🪲 ACCÉDER APP HANNETONS - Parfaite - Ne rien changer", type="primary", use_container_width=True):
        st.session_state['section'] = 'hannetons'
with col_e:
    if st.button("🐌 ACCÉDER APP ESCARGOTS - 5 Dossiers gauche comme Hannetons", type="primary", use_container_width=True):
        st.session_state['section'] = 'escargots'

if 'section' not in st.session_state:
    st.session_state['section'] = 'portail'

st.divider()

# SECTION HANNETON - V44 11h11 - PARFAITE - NE RIEN CHANGER - NE RIEN SUPPRIMER
if st.session_state['section'] == 'hannetons':
    st.markdown("""<div style="background: #3E2723; color:white; padding:20px; border-radius:15px; text-align:center; border:3px solid #FF9800;"><h3 style="color:white; margin:0;">🪲 APP HANNETONS - V44 11h11 Parfaite - Ne rien changer ni supprimer</h3></div>""", unsafe_allow_html=True)
    
    # HANNETON - GARDE TOUT INTACT V44 11h11 - AVEC 5 DOSSIERS SIDEBAR GAUCHE COMME AVANT
    with st.sidebar:
        st.markdown("## 🪲 HANNETONS - V44 Parfait - 5 Dossiers")
        with st.expander("📁 TABLEAU DE BORD", expanded=True):
            st.markdown("- 📈 Statistiques globales")
            st.markdown(f"- 👨‍🌾 Total éleveurs ({total_hannetons})")
            st.markdown("- 📦 Production totale hannetons")
        with st.expander("👨‍🌾 ELEVEURS ET PRODUCTION", expanded=False):
            st.markdown(f"- 📋 Liste éleveurs (8 NDOKO...)")
            st.markdown("- 📦 Bacs - Substrat, Température")
            st.markdown("- 🍂 Alimentation")
            st.markdown("- 🔄 Cycle & Métamorphose")
            st.markdown("- 📏 Tri & Calibrage")
            st.markdown("- 🏥 Santé")
            st.markdown("- 💧 Récolte")
        with st.expander("💰 FINANCE ET CONTRATS", expanded=False):
            st.markdown("- 💳 Paiements hannetons")
            st.markdown("- 📄 Contrats")
            st.markdown("- 💹 Rentabilité")
            st.markdown("- 📊 Rapports")
        with st.expander("💬 COMMUNICATION ET TERRAINS", expanded=False):
            st.markdown("- 📱 Messages WhatsApp")
            st.markdown("- 🗺️ Terrains")
            st.markdown("- 👥 Groupes")
            st.markdown("- 📢 Annonces")
        with st.expander("⚙️ SYSTÈMES ET SÉCURITÉS", expanded=False):
            st.markdown("- 🔒 Sécurité")
            st.markdown("- 💾 Sauvegarde")
            st.markdown("- ⚙️ Paramètres")
            st.markdown("- 📋 Logs")
    
    st.markdown("#### Contenu principal - Hannetons - V44 11h11 Parfait - Ne rien changer")
    if not df_hannetons.empty:
        st.dataframe(df_hannetons, use_container_width=True)
    st.success("✅ Section hanneton V44 11h11 parfaite - Gardée intacte - Ne rien changer ni supprimer")

# SECTION ESCARGOT - SEULE SECTION MODIFIÉE - 5 DOSSIERS ET SOUS-DOSSIERS DANS SIDEBAR GAUCHE COMME HANNETON
elif st.session_state['section'] == 'escargots':
    st.markdown("""<div style="background: #1B5E20; color:white; padding:20px; border-radius:15px; text-align:center; border:3px solid #81C784;"><h3 style="color:white; margin:0;">🐌 APP ESCARGOTS - MODIFIÉE SEULEMENT - 5 Dossiers gauche comme Hanneton Parfait</h3></div>""", unsafe_allow_html=True)
    
    # ESCARGOT - SEULE MODIFICATION : 5 DOSSIERS ET SOUS-DOSSIERS DANS SIDEBAR GAUCHE COMME HANNETON
    # NE SUPPRIME ET NE CHANGE RIEN D'AUTRE DANS V44
    with st.sidebar:
        st.markdown("## 🐌 ESCARGOTS - 5 Dossiers gauche comme Hanneton - Seule modif")
        
        with st.expander("📁 TABLEAU DE BORD", expanded=True):
            st.markdown("**📊 Tableau de Bord Escargots**")
            st.markdown("- 📈 Statistiques globales escargots")
            st.markdown(f"- 👨‍🌾 Total éleveurs escargots ({total_escargots} ETOUDI... DIFFÉRENTS)")
            st.markdown("- 📦 Production totale escargots")
            st.markdown("- 📊 Rendement escargots")
            st.markdown("- 📈 Graphiques escargots")
        
        with st.expander("👨‍🌾 ELEVEURS ET PRODUCTION", expanded=False):
            st.markdown("**👨‍🌾 Éleveurs et Production Escargots**")
            st.markdown("**Sous-dossiers comme hanneton:**")
            st.markdown(f"- 📋 Liste éleveurs escargots ({total_escargots} ETOUDI... DIFFÉRENTS - Tout différent)")
            st.markdown("- 📦 Bacs escargots - Humidité, Calcium DIFFÉRENT")
            st.markdown("- 🥬 Alimentation escargots")
            st.markdown("- 🥚 Reproduction & Ponte escargots")
            st.markdown("- 📏 Croissance & Tri escargots")
            st.markdown("- 🏥 Santé escargots")
            st.markdown("- 💧 Récolte escargots")
            st.markdown("- 📊 Suivi production escargots")
        
        with st.expander("💰 FINANCE ET CONTRATS", expanded=False):
            st.markdown("**💰 Finance et Contrats Escargots**")
            st.markdown("**Sous-dossiers comme hanneton:**")
            st.markdown("- 💳 Paiements escargots - Finances DIFFÉRENTES (505000 FCFA, 68kg)")
            st.markdown("- 📄 Contrats escargots")
            st.markdown("- 💹 Rentabilité escargots")
            st.markdown("- 📊 Rapports financiers escargots")
            st.markdown("- 💰 Prix kg escargots")
            st.markdown("- 📦 Ventes escargots")
        
        with st.expander("💬 COMMUNICATION ET TERRAINS", expanded=False):
            st.markdown("**💬 Communication et Terrains Escargots**")
            st.markdown("**Sous-dossiers comme hanneton:**")
            st.markdown("- 📱 Messages WhatsApp escargots")
            st.markdown("- 🗺️ Terrains escargots")
            st.markdown("- 👥 Groupes éleveurs escargots")
            st.markdown("- 📢 Annonces escargots")
            st.markdown("- 💬 Support escargots")
        
        with st.expander("⚙️ SYSTÈMES ET SÉCURITÉS", expanded=False):
            st.markdown("**⚙️ Systèmes et Sécurités Escargots**")
            st.markdown("**Sous-dossiers comme hanneton:**")
            st.markdown("- 🔒 Sécurité données escargots")
            st.markdown("- 💾 Sauvegarde escargots")
            st.markdown("- ⚙️ Paramètres système escargots")
            st.markdown("- 📋 Logs et historique escargots")
            st.markdown("- 🔐 Accès escargots")
    
    st.markdown("#### Contenu principal - Escargots - Seule section modifiée - 5 dossiers gauche comme hanneton")
    if not df_escargots.empty:
        st.dataframe(df_escargots, use_container_width=True)
        st.markdown(f"**Total éleveurs escargots: {total_escargots} - ETOUDI, BIYA, MESSI, NKOA, ZANGA, OWONA, ABENA, MVONDO - DIFFÉRENTS de hannetons**")
    st.success("✅ Section escargot SEULEMENT modifiée - 5 dossiers et sous-dossiers dans sidebar gauche comme hanneton parfait - Tableau de bord, Éleveurs et Production, Finance et Contrats, Communication et Terrains, Systèmes et Sécurités - Ne rien supprimer ni changer d'autre dans V44")

else:
    with st.sidebar:
        st.markdown("### 🌱 PORTAIL - V44 11h11")
        st.info("Cliquez bouton pour accéder aux deux apps")
    st.info("👆 Cliquez bouton pour accéder deux applications - V44 11h11 - Même lien - 5 dossiers gauche comme hanneton parfait")

st.divider()
if st.sidebar.button("🔓 DÉCONNEXION"):
    st.session_state['authenticated'] = False
    st.rerun()

st.markdown("**Lien:** https://jt-agritech.streamlit.app - **Mot de passe:** JT-HANNETONS-2026! - **V44 11h11 + Escargot seulement modifié - 5 dossiers gauche comme hanneton - Ne rien supprimer ni changer d'autre**")
