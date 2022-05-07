.PHONY: environment
environment:
	pyenv install -s 3.10.0
	pyenv uninstall --force dxf-ruler
	pyenv virtualenv 3.10.0 --force dxf-ruler
	pyenv local dxf-ruler

.PHONY: install
install:
	pip freeze | xargs -r pip uninstall -y
	python -m pip install --upgrade pip
	pip install -r requirements.txt
	pre-commit install

.PHONY: run
run:
	FLASK_ENV=development flask run