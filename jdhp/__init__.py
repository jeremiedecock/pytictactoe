# This (i.e. "jdhp") is a Python namespace package.
# See the following links for more information:
# - http://peak.telecommunity.com/DevCenter/setuptools#namespace-packages
# - https://github.com/zestsoftware/zest.releaser/blob/master/zest/__init__.py
# - https://www.python.org/dev/peps/pep-0423/#respect-ownership
# - http://stackoverflow.com/questions/7785944/what-does-import-pkg-resources-declare-namespace-name-do
# - http://stackoverflow.com/questions/5064951/packaging-common-python-namespaces

try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    from pkgutil import extend_path
    __path__ = extend_path(__path__, __name__)
