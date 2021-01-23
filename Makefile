.ONESHELL:
createenv:
	set -auxo pipefail
	python3.6 -m venv ./.venv
	source ./.venv/bin/activate
	pip3.6 install --upgrade pip
	pip3.6 install -r requirements.txt

.ONESHELL:
jupyter: createenv
	source ./.venv/bin/activate
	jupyter-lab

.ONESHELL:
pep8: createenv
	source ./.venv/bin/activate
	flake8 *.py
	pylint *.py

.ONESHELL:
test: createenv
	source ./.venv/bin/activate
	python create_tables.py
	python etl.py

clear: clean

clean:
	rm -rf ./.venv
