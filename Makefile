.ONESHELL:
jupyter:
	set -auxo pipefail
	python3.6 -m venv ./.venv
	source ./.venv/bin/activate
	pip3.6 install --upgrade pip
	pip3.6 install -r requirements.txt
	jupyter-lab

clear: clean

clean:
	rm -rf ./.venv
