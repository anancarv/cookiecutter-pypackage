# Cookiecutter PyPackage

Cookiecutter template for creating high quality Python packages.

## Features
* [github-actions](https://github.com/features/actions): For Continuous Integration
* [black](https://github.com/psf/black): Python code formatter
* [detect-secrets](https://github.com/Yelp/detect-secrets): Secrets detection within the code base 
* [mypy](https://github.com/python/mypy): Static type checker for Python
* [bandit](https://github.com/PyCQA/bandit): Find common security issues in Python code.
* [pylint](https://www.pylint.org/): Source code analyzer
* [pre-commit](https://github.com/pre-commit/pre-commit): A framework for managing and maintaining multi-language pre-commit hooks.


## Install
First, you need to Install cookiecutter
```bash
pip install cookiecutter
```

Generate a Python package project:
```bash
cookiecutter https://github.com/anancarv/cookiecutter-pypackage.git
full_name [Ananias CARVALHO]:
email [carvalhoananias@example.com]:
github_username [anancarv]:
...
```


## Developing

To start working on your project, here are some guidelines to set up your environment:
  1. `cd <YOUR_PROJECT_SLUG>`
  2. [Install poetry](https://python-poetry.org/docs/#installation)
  3. Activate virtualenv`poetry shell`
  4. Install dependencies: `poetry install`
  5. Run `pre-commit install --install-hooks` to install [precommit hooks](https://github.com/pre-commit/pre-commit)

After having installed pre-commit, before each commit, pre-commit hooks will perform static analysis, linting and code quality checks. 
As a result, you will be sure that each of your commit is clean.

Since your newly created project comes with `github actions`, every push will trigger the workflow `.github/workflows/check_code.yml` for analysing your code.

For publishing your package to [pypi](https://pypi.org/), you only need to set the secret `PYPI_TOKEN` with your token previously generated on pypi.

## Similar Cookiecutter Templates
* [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage)
