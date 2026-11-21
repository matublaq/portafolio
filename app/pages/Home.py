from utils import *

# ---------- Settings ----------
st.set_page_config(
    page_title="Matublaq",
    layout="wide"
)

st.html(
    """
    <style>
        hr {border-color: #968532 !important; margin: 0px; padding: 0px;}

        div[data-testid='stDivider'] {
            margin-bottom: 0.0rem;
        }

        .projects-grid {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 20px;
            margin: 15px 0;
            width: 100%;
        }

        .project-card-link {
            text-decoration: none;
            display: block;
            flex: 1 1 324px;
            max-width: 360px;
        }

        .project-card {
            width: 100%;
            height: 204px;
            border: 3px solid #33322B;
            border-radius: 12px;
            overflow: hidden;
            position: relative;
            background-color: #000000;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            box-sizing: border-box;
        }

        .project-card img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
        }

        .project-card-title {
            position: absolute;
            bottom: 0;
            width: 100%;
            background: rgba(0, 0, 0, 0.55);
            color: white;
            text-align: center;
            padding: 10px;
            box-sizing: border-box;
            font-family: sans-serif;
            font-weight: bold;
            font-size: 15px;
        }
    </style>
    """
)

# ---------- Home ----------
# --- Title, subtitle and introduction ---
st.markdown("<h4 style='text-align: center; color: #C0A520;'>Data-science applied to news</h4>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center; color: #C0A520;'>100% official data. Source include in every new</h6>", unsafe_allow_html=True)

st.divider()

# --- Main news ---
col1a, col2a = st.columns(2)
with col1a:
    st.markdown("<p style='text-align: center;'>text</p>", unsafe_allow_html=True)
with col2a:
    st.markdown("<p style='text-align: center;'>chart</p>", unsafe_allow_html=True)

st.divider()

# --- Projects ---
import textwrap

def build_project_card(image, link, title):
    return textwrap.dedent(f"""\
        <a href="{link}" target="_blank" class="project-card-link">
            <div class="project-card">
                <img src="{image}" alt="{title}">
                <div class="project-card-title">{title}</div>
            </div>
        </a>
    """).strip()

projects_data = [
    {"image": "/app/static/CO2_vehicle_contamination.png", "link": "CO2_contamination_vehicle", "title": "Vehicle contamination"},
    {"image": "/app/static/campo_project.jpeg", "link": "CampoProject", "title": "Campo"},
    {"image": "/app/static/stockmarket.jpeg", "link": "StockMarket", "title": "Stock market"},
]

cards_html = "".join(build_project_card(**p) for p in projects_data)
st.markdown(f'<div class="projects-grid">{cards_html}</div>', unsafe_allow_html=True)

st.divider()

# ---- Colors ----
st.markdown(
    """
    <div style="display: flex; gap: 8px; width: 100%;">
        <div style="flex: 1; height: 30px; background-color: #33322B; border-radius: 6px; display: flex; align-items: center; justify-content: center; color: white; font-size: 12px;">#33322B</div>
        <div style="flex: 1; height: 30px; background-color: #413D2B; border-radius: 6px; display: flex; align-items: center; justify-content: center; color: white; font-size: 12px;">#413D2B</div>
        <div style="flex: 1; height: 30px; background-color: #6B6236; border-radius: 6px; display: flex; align-items: center; justify-content: center; color: white; font-size: 12px;">#6B6236</div>
        <div style="flex: 1; height: 30px; background-color: #968532; border-radius: 6px; display: flex; align-items: center; justify-content: center; color: white; font-size: 12px;">#968532</div>
        <div style="flex: 1; height: 30px; background-color: #C0A520; border-radius: 6px; display: flex; align-items: center; justify-content: center; color: white; font-size: 12px;">#C0A520</div>
        <div style="flex: 1; height: 30px; background-color: #EBC301; border-radius: 6px; display: flex; align-items: center; justify-content: center; color: white; font-size: 12px;">#EBC301</div>
    </div>
    """,
    unsafe_allow_html=True
)