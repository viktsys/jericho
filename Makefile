deps:
	sudo apt update -y
	sudo apt install python3-dev libpq-dev

pyc-clean:
	export PYTHONPYCACHEPREFIX="${HOME}/.cache/Python"

serve-api: pyc-clean
	python3 ./api/manage.py runserver

serve-app: pyc-clean
	vite serve 