# Cookiecutter PyPackage

[Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for creating high quality Python packages.

<!-- toc -->

- [Install](#install)
- [Developing](#developing)
  * [Create a GitHub Repo](#create-a-github-repo)
  * [Features](#features)
- [Similar Cookiecutter Templates](#similar-cookiecutter-templates)

<!-- tocstop -->

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
  5. Init a git repository: `git init .`
  5. Run `pre-commit install --install-hooks` to install [precommit hooks](https://github.com/pre-commit/pre-commit)

After having installed pre-commit, before each commit, hooks will perform static analysis, linting and code quality checks.
As a result, you will be sure that each of your commit is clean.

All the code analysis features can be found in the [Features section](#features).

### Create a GitHub Repo
Go to your GitHub account and create a new repo named mypackage, where mypackage matches the `project_slug` from your previous answers.
Back to your CLI, you can do the following in the root of your generated project:
```bash
git add .
git commit -m "Initial skeleton."
git remote add origin git@github.com:<MY_USERNAME>/mypackage.git
git push -u origin master
```

Since your newly created project comes with `github actions`, every push will trigger the workflow `.github/workflows/check_code.yml` for analysing your code.

For publishing your package to [pypi](https://pypi.org/), you must create a release. 
Indeed, each release creation triggers the workflow `.github/workflows/deploy.yml` that builds and deploys your package.
The only requirement is to set the `PYPI_TOKEN` variable within your [github secrets](https://help.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets) with your token previously generated on pypi.

### Features
* [poetry](https://python-poetry.org/): Dependency management and packaging made easy.
* [github-actions](https://github.com/features/actions): For Continuous Integration
* [black](https://github.com/psf/black): Python code formatter
* [mypy](https://github.com/python/mypy): Static type checker for Python
* [bandit](https://github.com/PyCQA/bandit): Find common security issues in Python code.
* [flake8](https://github.com/PyCQA/flake8): Source code analyzer
* [pre-commit](https://github.com/pre-commit/pre-commit): A framework for managing and maintaining multi-language pre-commit hooks.

## Similar Cookiecutter Templates
* [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage)
