#!/usr/bin/env bash
set -e

echo "==> Sincronizando repos para el portfolio..."
python /app/sync_repos.py

echo "==> Arrancando Streamlit..."
exec streamlit run /app/streamlit_app.py \
  --server.address=0.0.0.0 \
  --server.port=8501 \
  --server.runOnSave=true \
  --browser.gatherUsageStats=false
