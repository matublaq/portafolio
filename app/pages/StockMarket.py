import os
import sys
from pathlib import Path
import streamlit as st

repo_dir = Path(r"/app/cache/repositorios/StockMarket")

if not repo_dir.exists():
    st.error(f"El repositorio {repo_dir.name} no se encuentra sincronizado.")
    st.stop()

# Agregar el directorio al PATH de Python para resolver importaciones internas
sys.path.insert(0, str(repo_dir))

# Buscar el archivo de entrada principal dentro del repositorio clonado
entry_files = ["streamlit_app.py", "app.py", "main.py"]
entry_file = next((repo_dir / f for f in entry_files if (repo_dir / f).exists()), None)

if entry_file:
    # Cambiar temporalmente el directorio de trabajo a la carpeta del repo
    # para que los archivos relativos (CSVs, imágenes, etc.) funcionen correctamente.
    os.chdir(str(repo_dir))
    
    with open(entry_file, "r", encoding="utf-8") as f:
        code = f.read()
    
    global_ns = {
        "__file__": str(entry_file),
        "__name__": "__main__",
        "__package__": None,
    }
    
    exec(compile(code, str(entry_file), 'exec'), global_ns)
else:
    st.error(f"No se encontró un archivo de entrada (streamlit_app.py / app.py / main.py) en el repositorio {repo_dir.name}.")
