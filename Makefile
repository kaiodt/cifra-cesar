.PHONY: install format lint test sec

install:
	@poetry install

format:
	@ruff check --fix .
	@blue .

lint:
	@ruff check .

test:
	@pytest -v

sec:
	@pip-audit