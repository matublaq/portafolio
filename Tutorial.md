ssh matublaq@100.126.9.54

Actualizar nextcloud: 
- cd /srv/compose/nextcloud
	docker compose pull --dry-run # comprobar si hay alguna actualización pendiente. 
	docker compose pull
	docker compose up -d
	docker compose ps



Actualizar repositorios caché de Data-news: 
- En ~/portafolio: 
	- docker exec -it portfolio_streamlit bash
	- python /app/sync_repos.py
	- exit

Reiniciar contenedor: 
- docker compose restart

Reconstruir docker. 
- docker compose down
- docker compose up -d --build