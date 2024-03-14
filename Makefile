install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

upgrade brain-games:
	pip install --upgrade brain-games

upgrade brain-even:
	pip install --upgrade brain-even

upgrade brain-calc:
	pip install --upgrade brain-calc

upgrade brain-gcd:
	pip install --upgrade brain-gcd