# Este script hace pull (fetch + merge) o clona los repositorios de repos.txt e instala sus dependencias
import os
import subprocess
from pathlib import Path

REPOS_FILE = Path(__file__).parent / "repos.txt"
DEFAULT_CACHE_DIR = Path(__file__).resolve().parent / "ignore_cache" / "repositorios"
CACHE_DIR = Path(os.environ.get("REPOS_CACHE_DIR", str(DEFAULT_CACHE_DIR)))
PAGES_DIR = Path(__file__).resolve().parent / "pages"
DEPTH = int(os.environ.get("GIT_CLONE_DEPTH", "1"))

def run(cmd, cwd=None):
    subprocess.run(cmd, cwd=cwd, check=True)

def safe_name_from_url(url: str) -> str:
    name = url.rstrip("/").split("/")[-1]
    if name.endswith(".git"):
        name = name[:-4]
    return name

def create_page_stub(name: str, repo_dest: Path):
    """Crea un archivo puente en la carpeta pages/ para que Streamlit enrute la URL automáticamente."""
    PAGES_DIR.mkdir(parents=True, exist_ok=True)
    stub_path = PAGES_DIR / f"{name}.py"
    
    stub_content = f'''import os
import sys
from pathlib import Path
import streamlit as st

repo_dir = Path(r"{repo_dest}")

if not repo_dir.exists():
    st.error(f"El repositorio {{repo_dir.name}} no se encuentra sincronizado.")
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
    
    global_ns = {{
        "__file__": str(entry_file),
        "__name__": "__main__",
        "__package__": None,
    }}
    
    exec(compile(code, str(entry_file), 'exec'), global_ns)
else:
    st.error(f"No se encontró un archivo de entrada (streamlit_app.py / app.py / main.py) en el repositorio {{repo_dir.name}}.")
'''
    stub_path.write_text(stub_content, encoding="utf-8")

def clone_or_pull(url: str):
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    name = safe_name_from_url(url)
    dest = CACHE_DIR / name

    # Marcar el directorio como seguro para evitar errores de propiedad en Docker. 
    run(["git", "config", "--global", "--add", "safe.directory", str(dest)])

    if not dest.exists():
        run(["git", "clone", "--depth", str(DEPTH), url, str(dest)])
    else:
        # Actualiza sin re-clonar todo
        run(["git", "-C", str(dest), "fetch", "--all", "--prune"])
        run(["git", "-C", str(dest), "pull", "--ff-only"])
    
    # NUEVO: Si el repositorio clonado tiene su propio requirements.txt, instalarlo automáticamente
    sub_reqs = dest / "requirements.txt"
    if sub_reqs.exists():
        print(f"-> Instalando dependencias de {name} desde su requirements.txt...")
        run(["pip", "install", "--no-cache-dir", "-r", str(sub_reqs)])

    # Crear o actualizar el puente en la carpeta pages de Streamlit
    create_page_stub(name, dest)

def main():
    if not REPOS_FILE.exists():
        print(f"No existe {REPOS_FILE}")
        return

    urls = [line.strip() for line in REPOS_FILE.read_text().splitlines() if line.strip()]
    if not urls:
        print("repos.txt está vacío")
        return

    print(f"Sincronizando {len(urls)} repos en {CACHE_DIR} ...")
    for url in urls:
        print(f"- {url}")
        clone_or_pull(url)

    print("Sincronización y generación de páginas OK.")

if __name__ == "__main__":
    main()