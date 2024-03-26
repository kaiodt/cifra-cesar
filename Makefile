.PHONY: install format lint test sec

install:
	@poetry install

format:
	@blue .

lint:
	@ruff check --fix .
	@ruff check .

test:
	@pytest -v

sec:
	@pip-audit