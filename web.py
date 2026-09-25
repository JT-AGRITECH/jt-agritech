import streamlit as st
import pandas as pd
from pathlib import Path
import urllib.parse
from PIL import Image, ImageOps, ImageDraw, ImageFont
from datetime import datetime, date, timedelta
import io, zipfile, base64
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import os

APP_DIR = Path(__file__).parent

# LECTURE 4 FICHIERS EDITABLES - TOUT DIFFÉRENT BIEN DISTINCTES - NE RIEN CHANGER
PIECES_DIR = APP_DIR / "pieces_jointes"
PIECES_DIR.mkdir(exist_ok=True)

try:
    _JT_LOGO_B64_WRAPPER = "[BASE64_PLACEHOLDER_2]"
except:
    pass

# V44 de 11h11 - TOUT DIFFÉRENT BIEN DISTINCTES - BASE PARFAITE - NE RIEN CHANGER
# ... (garde tout le code V44 intact de 11h11 ici - 7726 lignes) ...

# SEULE MODIFICATION : AJOUT 5 DOSSIERS ET SOUS-DOSSIERS DANS SIDEBAR GAUCHE COMME HANNETON PARFAIT
# NE SUPPRIME ET NE CHANGE RIEN D'AUTRE

# Dans ta fonction principale, après st.set_page_config, ajoute ce bloc sidebar gauche :

with st.sidebar:
    st.markdown("## 📁 DOSSIERS - Comme hanneton parfait")
    st.markdown("### 🪲 HANNETONS + 🐌 ESCARGOTS - Même structure")
    
    # DOSSIER 1 : TABLEAU DE BORD
    with st.expander("📁 TABLEAU DE BORD", expanded=False):
        st.markdown("**📊 Tableau de Bord**")
        st.markdown("- 📈 Statistiques globales")
        st.markdown(f"- 👨‍🌾 Total éleveurs hannetons")
        st.markdown(f"- 🐌 Total éleveurs escargots")
        st.markdown("- 📦 Production totale")
        st.markdown("- 📊 Rendement global")
        if st.button("📊 Voir Tableau de Bord", key="btn_tb"):
            st.session_state['page'] = 'tableau_bord'
    
    # DOSSIER 2 : ELEVEURS ET PRODUCTION AVEC SOUS-DOSSIERS
    with st.expander("👨‍🌾 ELEVEURS ET PRODUCTION", expanded=False):
        st.markdown("**👨‍🌾 Éleveurs et Production**")
        st.markdown("**Sous-dossiers Hannetons:**")
        st.markdown("- 📋 Liste éleveurs hannetons (8 NDOKO...)")
        st.markdown("- 📦 Bacs hannetons - Substrat, Température")
        st.markdown("- 🍂 Alimentation hannetons")
        st.markdown("- 🔄 Cycle & Métamorphose")
        st.markdown("- 📏 Tri & Calibrage hannetons")
        st.markdown("- 🏥 Santé hannetons")
        st.markdown("- 💧 Récolte hannetons")
        st.markdown("**Sous-dossiers Escargots - Comme hanneton:**")
        st.markdown("- 📋 Liste éleveurs escargots (8 ETOUDI... DIFFÉRENTS)")
        st.markdown("- 📦 Bacs escargots - Humidité, Calcium DIFFÉRENT")
        st.markdown("- 🥬 Alimentation escargots")
        st.markdown("- 🥚 Reproduction & Ponte escargots")
        st.markdown("- 📏 Croissance & Tri escargots")
        st.markdown("- 🏥 Santé escargots")
        st.markdown("- 💧 Récolte escargots")
        if st.button("👨‍🌾 Voir Éleveurs et Production", key="btn_ep"):
            st.session_state['page'] = 'eleveurs_production'
    
    # DOSSIER 3 : FINANCE ET CONTRATS AVEC SOUS-DOSSIERS
    with st.expander("💰 FINANCE ET CONTRATS", expanded=False):
        st.markdown("**💰 Finance et Contrats**")
        st.markdown("**Sous-dossiers Hannetons:**")
        st.markdown("- 💳 Paiements hannetons")
        st.markdown("- 📄 Contrats hannetons")
        st.markdown("- 💹 Rentabilité hannetons")
        st.markdown("- 📊 Rapports financiers hannetons")
        st.markdown("**Sous-dossiers Escargots - Comme hanneton:**")
        st.markdown("- 💳 Paiements escargots - 505000 FCFA, 68kg DIFFÉRENT")
        st.markdown("- 📄 Contrats escargots")
        st.markdown("- 💹 Rentabilité escargots")
        st.markdown("- 📊 Rapports financiers escargots")
        if st.button("💰 Voir Finance et Contrats", key="btn_fc"):
            st.session_state['page'] = 'finance_contrats'
    
    # DOSSIER 4 : COMMUNICATION ET TERRAINS AVEC SOUS-DOSSIERS
    with st.expander("💬 COMMUNICATION ET TERRAINS", expanded=False):
        st.markdown("**💬 Communication et Terrains**")
        st.markdown("**Sous-dossiers Hannetons:**")
        st.markdown("- 📱 Messages WhatsApp hannetons")
        st.markdown("- 🗺️ Terrains hannetons")
        st.markdown("- 👥 Groupes éleveurs hannetons")
        st.markdown("- 📢 Annonces hannetons")
        st.markdown("**Sous-dossiers Escargots - Comme hanneton:**")
        st.markdown("- 📱 Messages WhatsApp escargots")
        st.markdown("- 🗺️ Terrains escargots")
        st.markdown("- 👥 Groupes éleveurs escargots")
        st.markdown("- 📢 Annonces escargots")
        if st.button("💬 Voir Communication et Terrains", key="btn_ct"):
            st.session_state['page'] = 'communication_terrains'
    
    # DOSSIER 5 : SYSTÈMES ET SÉCURITÉS AVEC SOUS-DOSSIERS
    with st.expander("⚙️ SYSTÈMES ET SÉCURITÉS", expanded=False):
        st.markdown("**⚙️ Systèmes et Sécurités**")
        st.markdown("**Sous-dossiers Hannetons:**")
        st.markdown("- 🔒 Sécurité données hannetons")
        st.markdown("- 💾 Sauvegarde hannetons")
        st.markdown("- ⚙️ Paramètres système hannetons")
        st.markdown("- 📋 Logs et historique hannetons")
        st.markdown("**Sous-dossiers Escargots - Comme hanneton:**")
        st.markdown("- 🔒 Sécurité données escargots")
        st.markdown("- 💾 Sauvegarde escargots")
        st.markdown("- ⚙️ Paramètres système escargots")
        st.markdown("- 📋 Logs et historique escargots")
        if st.button("⚙️ Voir Systèmes et Sécurités", key="btn_ss"):
            st.session_state['page'] = 'systemes_securites'

# FIN AJOUT 5 DOSSIERS SIDEBAR GAUCHE - NE RIEN CHANGER D'AUTRE DANS V44
