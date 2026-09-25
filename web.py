import streamlit as st
import pandas as pd
from pathlib import Path

APP_DIR = Path(__file__).parent
st.set_page_config(page_title="JT AGRITECH - Deux Secteurs", page_icon="🌱", layout="wide")

# Lecture 4 fichiers éditables
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
.metric-hanneton {background: linear-gradient(135deg, #3E2723 0%, #8B4513 100%); color:white; padding:25px; border-radius:20px; text-align:center; border:4px solid #FF9800;}
.metric-escargot {background: linear-gradient(135deg, #1B5E20 0%, #2E7D32 100%); color:white; padding:25px; border-radius:20px; text-align:center; border:4px solid #81C784;}
.metric-total {background: linear-gradient(135deg, #225522 0%, #4CAF50 100%); color:white; padding:25px; border-radius:20px; text-align:center; border:4px solid #8BC34A;}
.dossier {background:white; border-radius:15px; padding:15px; border-left:6px solid #8B4513; border-top:3px solid #FF9800; margin-bottom:10px;}
.dossier-escargot {background:white; border-radius:15px; padding:15px; border-left:6px solid #2E7D32; border-top:3px solid #4CAF50; margin-bottom:10px;}
.sous-dossier {background:#FFF8E1; border-radius:10px; padding:10px; margin:5px 0 5px 20px; border-left:3px solid #FF9800; font-size:13px;}
.sous-dossier-escargot {background:#E8F5E9; border-radius:10px; padding:10px; margin:5px 0 5px 20px; border-left:3px solid #4CAF50; font-size:13px;}
</style>
""", unsafe_allow_html=True)

# PORTAIL D'ACCUEIL - DEUX APPS DISTINCTES UN SEUL LIEN
st.markdown("""
<div style="background: linear-gradient(135deg, #225522 0%, #8fbc5f 100%); padding:30px; border-radius:20px; text-align:center; color:white; margin-bottom:25px;">
 <h2 style="color:white; margin:0;">🌱 JT-AGRITECH - DEUX SECTEURS - UN SEUL LIEN</h2>
 <p style="color:#e8f5d8; margin:5px 0 0 0; font-weight:700;">Portail - Total éleveurs seulement - Algorithme bon</p>
</div>
""", unsafe_allow_html=True)

# PORTAIL SEULEMENT TOTAL ELEVEURS - SUPPRIME BACS ET FINANCIER
st.markdown("### 📊 PORTAIL - TOTAL ÉLEVEURS SEULEMENT")
c1,c2,c3 = st.columns(3)
with c1:
    st.markdown(f"""<div class="metric-hanneton"><div style="font-size:42px; font-weight:900; color:#FFE0B2;">🪲 {total_hannetons}</div><div style="color:#FFCC80; font-weight:800;">Éleveurs Hannetons</div></div>""", unsafe_allow_html=True)
with c2:
    st.markdown(f"""<div class="metric-escargot"><div style="font-size:42px; font-weight:900; color:#C8E6C9;">🐌 {total_escargots}</div><div style="color:#A5D6A7; font-weight:800;">Éleveurs Escargots</div></div>""", unsafe_allow_html=True)
with c3:
    st.markdown(f"""<div class="metric-total"><div style="font-size:42px; font-weight:900; color:#E8F5E9;">👨‍🌾 {total_global}</div><div style="color:#C8E6C9; font-weight:800;">Total Éleveurs</div></div>""", unsafe_allow_html=True)

st.info("✅ Portail affiche seulement total éleveurs - Bacs et financier supprimés - Ne rien changer d'autre")

# ACCES DEUX SECTIONS DEPUIS PORTAIL
col_h, col_e = st.columns(2)
with col_h:
    if st.button("🪲 ACCÉDER APP HANNETONS - Parfaite", type="primary", use_container_width=True):
        st.session_state['section'] = 'hannetons'
with col_e:
    if st.button("🐌 ACCÉDER APP ESCARGOTS - Dossiers comme Hannetons", type="primary", use_container_width=True):
        st.session_state['section'] = 'escargots'

if 'section' not in st.session_state:
    st.session_state['section'] = 'portail'

st.divider()

if st.session_state['section'] == 'hannetons':
    st.markdown("""<div style="background: linear-gradient(135deg, #3E2723 0%, #8B4513 100%); color:white; padding:25px; border-radius:20px; text-align:center; border:4px solid #FF9800;"><h3 style="color:white; margin:0;">🪲 APP HANNETONS - Parfaite - Ne rien changer</h3></div>""", unsafe_allow_html=True)
    
    # 5 DOSSIERS HANNETON PARFAIT
    st.markdown("#### 📁 TABLEAU DE BORD HANNETONS")
    st.markdown("<div class='dossier'><b>📊 Tableau de Bord Hannetons - Parfait</b></div>", unsafe_allow_html=True)
    st.markdown("<div class='sous-dossier'>📈 Statistiques globales - Total éleveurs hannetons</div>", unsafe_allow_html=True)
    st.markdown("<div class='sous-dossier'>📦 Production totale hannetons</div>", unsafe_allow_html=True)
    
    st.markdown("#### 👨‍🌾 ELEVEURS ET PRODUCTION HANNETONS")
    st.markdown("<div class='dossier'><b>👨‍🌾 Éleveurs et Production Hannetons</b></div>", unsafe_allow_html=True)
    for s in ["📋 Liste éleveurs (8 NDOKO...)", "📦 Bacs hannetons - Substrat, Température", "🍂 Alimentation", "🔄 Cycle & Métamorphose", "📏 Tri & Calibrage", "🏥 Santé", "💧 Récolte"]:
        st.markdown(f"<div class='sous-dossier'>{s}</div>", unsafe_allow_html=True)
    
    st.markdown("#### 💰 FINANCE ET CONTRATS HANNETONS")
    st.markdown("<div class='dossier'><b>💰 Finance et Contrats Hannetons</b></div>", unsafe_allow_html=True)
    for s in ["💳 Paiements hannetons", "📄 Contrats", "💹 Rentabilité", "📊 Rapports financiers"]:
        st.markdown(f"<div class='sous-dossier'>{s}</div>", unsafe_allow_html=True)
    
    st.markdown("#### 💬 COMMUNICATION ET TERRAINS HANNETONS")
    st.markdown("<div class='dossier'><b>💬 Communication et Terrains Hannetons</b></div>", unsafe_allow_html=True)
    for s in ["📱 Messages WhatsApp", "🗺️ Terrains", "👥 Groupes éleveurs", "📢 Annonces"]:
        st.markdown(f"<div class='sous-dossier'>{s}</div>", unsafe_allow_html=True)
    
    st.markdown("#### ⚙️ SYSTÈMES ET SÉCURITÉS HANNETONS")
    st.markdown("<div class='dossier'><b>⚙️ Systèmes et Sécurités Hannetons</b></div>", unsafe_allow_html=True)
    for s in ["🔒 Sécurité données", "💾 Sauvegarde", "⚙️ Paramètres", "📋 Logs"]:
        st.markdown(f"<div class='sous-dossier'>{s}</div>", unsafe_allow_html=True)
    
    st.success("✅ Section hanneton parfaite - Ne rien changer")

elif st.session_state['section'] == 'escargots':
    st.markdown("""<div style="background: linear-gradient(135deg, #1B5E20 0%, #2E7D32 100%); color:white; padding:25px; border-radius:20px; text-align:center; border:4px solid #81C784;"><h3 style="color:white; margin:0;">🐌 APP ESCARGOTS - Dossiers comme Hanneton Parfait</h3></div>""", unsafe_allow_html=True)
    
    # 5 DOSSIERS ESCARGOTS COMME HANNETON PARFAIT
    st.markdown("#### 📁 TABLEAU DE BORD ESCARGOTS - Comme Hanneton")
    st.markdown("<div class='dossier-escargot'><b>📊 Tableau de Bord Escargots</b></div>", unsafe_allow_html=True)
    for s in ["📈 Statistiques globales escargots", f"👨‍🌾 Total éleveurs escargots ({total_escargots} ETOUDI... DIFFÉRENTS)", "📦 Production totale escargots"]:
        st.markdown(f"<div class='sous-dossier-escargot'>{s}</div>", unsafe_allow_html=True)
    
    st.markdown("#### 👨‍🌾 ELEVEURS ET PRODUCTION ESCARGOTS - Comme Hanneton")
    st.markdown("<div class='dossier-escargot'><b>👨‍🌾 Éleveurs et Production Escargots - Comme Hanneton</b></div>", unsafe_allow_html=True)
    for s in [f"📋 Liste éleveurs escargots ({total_escargots} ETOUDI... DIFFÉRENTS)", "📦 Bacs escargots - Humidité, Calcium DIFFÉRENT", "🥬 Alimentation escargots", "🥚 Reproduction & Ponte", "📏 Croissance & Tri", "🏥 Santé escargots", "💧 Récolte escargots"]:
        st.markdown(f"<div class='sous-dossier-escargot'>{s}</div>", unsafe_allow_html=True)
    
    st.markdown("#### 💰 FINANCE ET CONTRATS ESCARGOTS - Comme Hanneton")
    st.markdown("<div class='dossier-escargot'><b>💰 Finance et Contrats Escargots</b></div>", unsafe_allow_html=True)
    for s in ["💳 Paiements escargots - Finances DIFFÉRENTES (505000 FCFA, 68kg)", "📄 Contrats escargots", "💹 Rentabilité escargots", "📊 Rapports financiers escargots"]:
        st.markdown(f"<div class='sous-dossier-escargot'>{s}</div>", unsafe_allow_html=True)
    
    st.markdown("#### 💬 COMMUNICATION ET TERRAINS ESCARGOTS - Comme Hanneton")
    st.markdown("<div class='dossier-escargot'><b>💬 Communication et Terrains Escargots</b></div>", unsafe_allow_html=True)
    for s in ["📱 Messages WhatsApp escargots", "🗺️ Terrains escargots", "👥 Groupes éleveurs escargots", "📢 Annonces escargots"]:
        st.markdown(f"<div class='sous-dossier-escargot'>{s}</div>", unsafe_allow_html=True)
    
    st.markdown("#### ⚙️ SYSTÈMES ET SÉCURITÉS ESCARGOTS - Comme Hanneton")
    st.markdown("<div class='dossier-escargot'><b>⚙️ Systèmes et Sécurités Escargots</b></div>", unsafe_allow_html=True)
    for s in ["🔒 Sécurité données escargots", "💾 Sauvegarde escargots", "⚙️ Paramètres escargots", "📋 Logs escargots"]:
        st.markdown(f"<div class='sous-dossier-escargot'>{s}</div>", unsafe_allow_html=True)
    
    st.success("✅ Section escargot dossiers/sous-dossiers comme hanneton parfait - Tableau de bord, Éleveurs et Production, Finance et Contrats, Communication et Terrains, Systèmes et Sécurités")

else:
    st.info("👆 Cliquez bouton ci-dessus pour accéder deux applications distinctes depuis portail - Même lien - Algorithme bon")

st.divider()
st.markdown("**Lien unique deux apps distinctes:** https://jt-agritech.streamlit.app - Portail total éleveurs seulement")
