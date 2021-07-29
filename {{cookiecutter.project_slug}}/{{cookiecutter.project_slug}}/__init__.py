"""
Top-level package for {{ cookiecutter.project_slug }}.
"""
import logging

__version__ = "{{cookiecutter.project_version}}"

logging.basicConfig(format="%(asctime)s %(levelname)s:%(name)s: %(message)s")
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.info(f"Version {__version__}")
