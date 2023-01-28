install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt &&\
		pre-commit install

lint:
	pylint --disable=R,C hello.py app.py

format:
	black *.py

test:
	python3 -m pytest -vv --cov=./ test_hello.py
