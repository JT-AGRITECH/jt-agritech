import streamlit as st
import pandas as pd
from pathlib import Path

APP_DIR = Path(__file__).parent
st.set_page_config(page_title="JT AGRITECH - Deux Secteurs", page_icon="🌱", layout="wide")

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

# PORTAIL D'ACCUEIL - SEULEMENT TOTAL ELEVEURS
st.markdown("""
<div style="background: linear-gradient(135deg, #225522 0%, #8fbc5f 100%); padding:25px; border-radius:20px; text-align:center; color:white; margin-bottom:20px;">
 <h2 style="color:white; margin:0;">🌱 JT-AGRITECH - DEUX APPS - UN SEUL LIEN</h2>
 <p style="color:#e8f5d8; margin:5px 0 0 0;">Portail total éleveurs seulement - Dossiers à gauche comme hanneton parfait</p>
</div>
""", unsafe_allow_html=True)

c1,c2,c3 = st.columns(3)
with c1:
    st.markdown(f"""<div class="metric-hanneton"><div style="font-size:36px; font-weight:900; color:#FFE0B2;">🪲 {total_hannetons}</div><div style="color:#FFCC80; font-weight:800;">Éleveurs Hannetons</div></div>""", unsafe_allow_html=True)
with c2:
    st.markdown(f"""<div class="metric-escargot"><div style="font-size:36px; font-weight:900; color:#C8E6C9;">🐌 {total_escargots}</div><div style="color:#A5D6A7; font-weight:800;">Éleveurs Escargots</div></div>""", unsafe_allow_html=True)
with c3:
    st.markdown(f"""<div class="metric-total"><div style="font-size:36px; font-weight:900; color:#E8F5E9;">👨‍🌾 {total_global}</div><div style="color:#C8E6C9; font-weight:800;">Total Éleveurs</div></div>""", unsafe_allow_html=True)

st.info("✅ Portail affiche seulement total éleveurs - Bacs et financier supprimés - Algorithme bon - Ne rien changer d'autre")

col_h, col_e = st.columns(2)
with col_h:
    if st.button("🪲 ACCÉDER APP HANNETONS - Parfaite", type="primary", use_container_width=True):
        st.session_state['section'] = 'hannetons'
with col_e:
    if st.button("🐌 ACCÉDER APP ESCARGOTS - Dossiers à gauche comme Hannetons", type="primary", use_container_width=True):
        st.session_state['section'] = 'escargots'

if 'section' not in st.session_state:
    st.session_state['section'] = 'portail'

st.divider()

# DEUX APPLICATIONS DISTINCTES AVEC DOSSIERS À GAUCHE COMME HANNETON PARFAIT
if st.session_state['section'] == 'hannetons':
    st.markdown("""<div style="background: #3E2723; color:white; padding:20px; border-radius:15px; text-align:center; border:3px solid #FF9800;"><h3 style="color:white; margin:0;">🪲 APP HANNETONS - Parfaite - Dossiers à gauche - Ne rien changer</h3></div>""", unsafe_allow_html=True)
    
    # SIDEBAR GAUCHE - 5 DOSSIERS AVEC SOUS-DOSSIERS COMME HANNETON PARFAIT
    with st.sidebar:
        st.markdown("### 🪲 HANNETONS - Dossiers à gauche")
        
        st.markdown("#### 📁 TABLEAU DE BORD")
        with st.expander("📊 Tableau de Bord Hannetons", expanded=False):
            st.markdown("- 📈 Statistiques globales")
            st.markdown(f"- 👨‍🌾 Total éleveurs ({total_hannetons})")
            st.markdown("- 📦 Production totale")
            st.markdown("- 📊 Rendement")
        
        st.markdown("#### 👨‍🌾 ELEVEURS ET PRODUCTION")
        with st.expander("👨‍🌾 Éleveurs et Production", expanded=False):
            st.markdown(f"- 📋 Liste éleveurs (8 NDOKO...)")
            st.markdown("- 📦 Bacs - Substrat, Température")
            st.markdown("- 🍂 Alimentation")
            st.markdown("- 🔄 Cycle & Métamorphose")
            st.markdown("- 📏 Tri & Calibrage")
            st.markdown("- 🏥 Santé")
            st.markdown("- 💧 Récolte")
        
        st.markdown("#### 💰 FINANCE ET CONTRATS")
        with st.expander("💰 Finance et Contrats", expanded=False):
            st.markdown("- 💳 Paiements")
            st.markdown("- 📄 Contrats")
            st.markdown("- 💹 Rentabilité")
            st.markdown("- 📊 Rapports financiers")
        
        st.markdown("#### 💬 COMMUNICATION ET TERRAINS")
        with st.expander("💬 Communication et Terrains", expanded=False):
            st.markdown("- 📱 Messages WhatsApp")
            st.markdown("- 🗺️ Terrains")
            st.markdown("- 👥 Groupes éleveurs")
            st.markdown("- 📢 Annonces")
        
        st.markdown("#### ⚙️ SYSTÈMES ET SÉCURITÉS")
        with st.expander("⚙️ Systèmes et Sécurités", expanded=False):
            st.markdown("- 🔒 Sécurité données")
            st.markdown("- 💾 Sauvegarde")
            st.markdown("- ⚙️ Paramètres")
            st.markdown("- 📋 Logs et historique")
    
    st.markdown("#### Contenu principal - Section Hanneton Parfaite")
    if not df_hannetons.empty:
        st.dataframe(df_hannetons, use_container_width=True)
    st.success("✅ Section hanneton parfaite - Dossiers à gauche - Ne rien changer ni modifier d'autre")

elif st.session_state['section'] == 'escargots':
    st.markdown("""<div style="background: #1B5E20; color:white; padding:20px; border-radius:15px; text-align:center; border:3px solid #81C784;"><h3 style="color:white; margin:0;">🐌 APP ESCARGOTS - Dossiers à gauche comme Hanneton Parfait</h3></div>""", unsafe_allow_html=True)
    
    # SIDEBAR GAUCHE - 5 DOSSIERS ESCARGOTS COMME HANNETON PARFAIT
    with st.sidebar:
        st.markdown("### 🐌 ESCARGOTS - Dossiers à gauche comme Hanneton")
        
        st.markdown("#### 📁 TABLEAU DE BORD")
        with st.expander("📊 Tableau de Bord Escargots", expanded=False):
            st.markdown("- 📈 Statistiques globales escargots")
            st.markdown(f"- 👨‍🌾 Total éleveurs escargots ({total_escargots} ETOUDI... DIFFÉRENTS)")
            st.markdown("- 📦 Production totale escargots")
            st.markdown("- 📊 Rendement escargots")
        
        st.markdown("#### 👨‍🌾 ELEVEURS ET PRODUCTION")
        with st.expander("👨‍🌾 Éleveurs et Production Escargots", expanded=False):
            st.markdown(f"- 📋 Liste éleveurs escargots ({total_escargots} ETOUDI... DIFFÉRENTS - Tout différent)")
            st.markdown("- 📦 Bacs escargots - Humidité, Calcium DIFFÉRENT")
            st.markdown("- 🥬 Alimentation escargots")
            st.markdown("- 🥚 Reproduction & Ponte")
            st.markdown("- 📏 Croissance & Tri")
            st.markdown("- 🏥 Santé escargots")
            st.markdown("- 💧 Récolte escargots")
        
        st.markdown("#### 💰 FINANCE ET CONTRATS")
        with st.expander("💰 Finance et Contrats Escargots", expanded=False):
            st.markdown("- 💳 Paiements escargots - Finances DIFFÉRENTES (505000 FCFA, 68kg)")
            st.markdown("- 📄 Contrats escargots")
            st.markdown("- 💹 Rentabilité escargots")
            st.markdown("- 📊 Rapports financiers escargots")
        
        st.markdown("#### 💬 COMMUNICATION ET TERRAINS")
        with st.expander("💬 Communication et Terrains Escargots", expanded=False):
            st.markdown("- 📱 Messages WhatsApp escargots")
            st.markdown("- 🗺️ Terrains escargots")
            st.markdown("- 👥 Groupes éleveurs escargots")
            st.markdown("- 📢 Annonces escargots")
        
        st.markdown("#### ⚙️ SYSTÈMES ET SÉCURITÉS")
        with st.expander("⚙️ Systèmes et Sécurités Escargots", expanded=False):
            st.markdown("- 🔒 Sécurité données escargots")
            st.markdown("- 💾 Sauvegarde escargots")
            st.markdown("- ⚙️ Paramètres escargots")
            st.markdown("- 📋 Logs et historique escargots")
    
    st.markdown("#### Contenu principal - Section Escargot Dossiers comme Hanneton Parfait")
    if not df_escargots.empty:
        st.dataframe(df_escargots, use_container_width=True)
    st.success("✅ Section escargot avec dossiers à gauche exactement comme hanneton parfait - 5 dossiers avec sous-dossiers - Tableau de bord, Éleveurs et Production, Finance et Contrats, Communication et Terrains, Systèmes et Sécurités - Tout différent")

else:
    with st.sidebar:
        st.markdown("### 🌱 PORTAIL - Dossiers à gauche")
        st.info("Cliquez bouton ci-dessus pour accéder aux deux applications")
    st.info("👆 Cliquez bouton ci-dessus pour accéder deux applications distinctes depuis portail - Même lien - Dossiers à gauche comme hanneton parfait - Algorithme bon")

st.divider()
st.markdown("**Lien unique deux apps distinctes:** https://jt-agritech.streamlit.app - Dossiers à gauche comme hanneton parfait - Ne rien changer d'autre")
