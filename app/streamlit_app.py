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

# ---------- pages ----------
home_page = st.Page("pages/Home.py", title="Home", icon="🏠")
campo_page = st.Page("pages/CampoProject.py", title="Farm", icon="🌾")
co2_vehicle_contamination_page = st.Page("pages/CO2_contamination_vehicle.py", title="Vehicle contamination")
inflation_page = st.Page("pages/Inflation.py", title="Inflation", icon="📈")

# --- nav ---
nav = st.navigation(
    {
        "HOME": [home_page],
        "Base de datos": [inflation_page, campo_page, co2_vehicle_contamination_page]
    }, 
    position="hidden" # Oculta el nativo. 
)

# ---------- Header fijo ----------
# st.markdown(
#     """
#     <style>
#         .fixed-header {
#             position: fixed; 
#             top: 4rem;
#             left: 3rem; 
#             right: 3rem; 
#             z-index: 999;

#             height: 3rem; 

#             display: flex; 
#             align-items: center; 
#             justify-content: center;
#             padding: 1rem; 

#             background-color: rgba(107, 98, 54, 0.35); /* Tu color #6B6236 pero con opacidad del 35% */
#             backdrop-filter: blur(0.20rem);             /* Desenfoque del fondo (equivalente a ~12px) */
#             -webkit-backdrop-filter: blur(0.75rem);     /* Compatibilidad con Safari */    

#             border: 0.0625rem solid rgba(255, 255, 255, 0.15); /* Borde sutil brillante de cristal (1px) */
#             border-radius: 1rem; 
#             box-shadow: 0 0.5rem 1.5rem rgba(0, 0, 0, 0.2);

#             box-sizing: border-box;
#         }

#         .block-container {
#             padding-top: 8rem;
#         }

#     </style>
    
#     <div class="fixed-header">
#         <a href='Home' style='text-decoration: none;'>
#             <h1 style='text-align: center; font-size: 20px; color: #C0A520;'>Data News</h1>
#         </a>
#         <h2 style='font-size: 15px;'>Data science applied to news</h2>
#     </div>
#     """,
#     unsafe_allow_html=True
# )
st.markdown(
    """
    <style>
        .fixed-header {
            position: fixed; 
            top: 4rem;
            left: 3rem; 
            right: 3rem; 
            z-index: 999;
            height: 3.5rem; 

            display: flex; 
            align-items: center; 
            justify-content: center;  
            padding: 0.5rem 1rem; 

            background-color: rgba(107, 98, 54, 0.35); 
            backdrop-filter: blur(0.20rem);            
            -webkit-backdrop-filter: blur(0.75rem);    

            border: 0.0625rem solid rgba(255, 255, 255, 0.15); 
            border-radius: 1rem; 
            box-shadow: 0 0.5rem 1.5rem rgba(0, 0, 0, 0.2);
            box-sizing: border-box;
        }

        /* Contenedor del enlace ajustado al texto */
        .header-link {
            text-decoration: none !important;
            display: inline-flex;
            flex-direction: row;
            align-items: baseline;    /* <--- Alinea ambos textos por la base inferior de las palabras */
            justify-content: center;  
            gap: 30px;                
            cursor: pointer;
        }
        
        .header-link:hover .main-title {
            color: #EBC301 !important; 
        }

        .main-title {
            font-size: 20px;
            font-weight: bold;
            color: #C0A520;
            line-height: 1;
        }

        .sub-title {
            font-size: 12px;
            color: #C0A520;
            line-height: 1;
        }

        .block-container {
            padding-top: 8rem;
        }
    </style>
    
    <div class="fixed-header">
        <a href="#" class="header-link">
            <span class="main-title">Data News</span>
            <span class="sub-title">Data science applied to news</span>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------- Eejcutar el enrutador ----------
nav.run()