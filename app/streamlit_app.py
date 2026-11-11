from utils import *

# ---------- Settings ----------
st.set_page_config(
    page_title = "Matublaq", 
    layout="wide"
)
st.html(
    """
    <style>
        hr {border-color: #968532 !important; margin: 0px; padding: 0px;}
    </style>
    """
)
# ---------- Header ----------
st.markdown(
    """
    <style>
        .fixed-header {
            position: fixed; 
            top: 4rem;
            left: 3rem; 
            right: 3rem; 
            z-index: 999;

            height: 3rem; 

            display: flex; 
            align-items: center; 
            justify-content: center;
            padding: 1rem; 

            background-color: rgba(107, 98, 54, 0.35); /* Tu color #6B6236 pero con opacidad del 35% */
            backdrop-filter: blur(0.20rem);             /* Desenfoque del fondo (equivalente a ~12px) */
            -webkit-backdrop-filter: blur(0.75rem);     /* Compatibilidad con Safari */    

            border: 0.0625rem solid rgba(255, 255, 255, 0.15); /* Borde sutil brillante de cristal (1px) */
            border-radius: 1rem; 
            box-shadow: 0 0.5rem 1.5rem rgba(0, 0, 0, 0.2);

            box-sizing: border-box;
        }

        .block-container {
            padding-top: 8rem;
        }

    </style>
    
    <div class="fixed-header">
        <h1 style='text-align: center; font-size: 20px;'>Data News</h1>
    </div>
    """,
    unsafe_allow_html=True
)

#---------- Home page ----------
#--- Title, subtitle  and intoduction ---
# st.markdown("<h1 style='margin-top: 100px; text-align: center; color: #C0A520';>Data news</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #C0A520';>Data-science applied to news</h4>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center; color: #C0A520'> 100% official data. Source include in every new </h6>", unsafe_allow_html=True)

st.divider()
#--- Main news ---
col1a, col2a = st.columns(2)
with col1a: 
    st.markdown("<p style='text-align: center;'>text</p>", unsafe_allow_html=True)
with col2a: 
    st.write("<p style='text-align: center;'>chart</p>", unsafe_allow_html=True)

st.divider()
#--- Projects ---
# Functions.
def project_card(image, link, title):
    tarjeta_html = f"""
    <a href="{link}" target="_blank" style="text-decoration: none;">
        <div style="
            width: 324px; 
            height: 204px; 
            border: 3px solid #33322B;
            border-radius: 12px;
            overflow: hidden;
            position: relative;
            background-color: #000000;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            margin: 15px auto;
        ">
            <img src="{image}" style="
                width: 100%;
                height: 100%;
                object-fit: cover;
            ">
            <div style="
                position: absolute;
                bottom: 0;
                width: 100%;
                background: rgba(0, 0, 0, 0.35);
                color: white;
                text-align: center;
                padding: 10px;
                font-family: sans-serif;
                font-weight: bold;
                font-size: 15px;
            ">
                {title}
            </div>
        </div>
    </a>
    """
    st.markdown(tarjeta_html, unsafe_allow_html=True)

col1b, col2b = st.columns(2)
with col1b: 
    project_card(image="/app/static/CO2_vehicle_contamination.png", link="StockMarket", title="Vehicle contamination")
with col2b: 
    project_card(image="/app/static/campo_project.jpeg", link="CampoProject", title="Campo")

st.divider()
# ---- Colors ----
# Contenedor flex en HTML que NUNCA se romperá ni se pondrá en vertical. 
st.markdown("""
    <style>
        /* Estilos */
        div[data-testid='stDivider'] {
            margin-bottom: 0.0rem; 
        }
    </style>
    <div style="display: flex; gap: 8px; width: 100%;">
        <div style="flex: 1; height: 30px; background-color: #33322B; border-radius: 6px; display: flex; align-items: center; justify-content: center; color: white; font-size: 12px;">#33322B</div>
        <div style="flex: 1; height: 30px; background-color: #413D2B; border-radius: 6px; display: flex; align-items: center; justify-content: center; color: white; font-size: 12px;">#413D2B</div>
        <div style="flex: 1; height: 30px; background-color: #6B6236; border-radius: 6px; display: flex; align-items: center; justify-content: center; color: white; font-size: 12px;">#6B6236</div>
        <div style="flex: 1; height: 30px; background-color: #968532; border-radius: 6px; display: flex; align-items: center; justify-content: center; color: white; font-size: 12px;">#968532</div>
        <div style="flex: 1; height: 30px; background-color: #C0A520; border-radius: 6px; display: flex; align-items: center; justify-content: center; color: white; font-size: 12px;">#C0A520</div>
        <div style="flex: 1; height: 30px; background-color: #EBC301; border-radius: 6px; display: flex; align-items: center; justify-content: center; color: white; font-size: 12px;">#EBC301</div>
    </div>
""", unsafe_allow_html=True)