# Makefile with some convenient quick ways to do common things

include meta.make

###############################################################################

all: help

.PHONY : all \
		 lint \
		 clean \
		 conda \
		 doc \
		 doc-show \
	     help \
		 init \
		 init-pypi \
		 init-skeleton \
		 list \
		 pep8 \
		 publish \
		 publish-doc-github \
		 publish-doc-jdhp \
		 publish-pypi \
		 pypi \
		 pypi-check \
		 test \
		 trailing-spaces \


###############################################################################

PYTHON=python3

## HELP #######################################################################

#help:
#	@echo ''
#	@echo 'Available make targets:'
#	@echo ''
#	@echo '  help                Print this help message (the default)'
#	@echo '  init                Import submodules'
#	@echo '  clean               Remove generated files'
#	@echo '  develop             Make symlinks to this package in python install dir'
#	@echo '  test                Run tests'
#	@echo '  doc                 Generate Sphinx docs'
#	@echo '  doc-show            Generate and display docs in browser'
#	@echo '  analyze             Do a static code check and report errors'
#	@echo ''
#	@echo 'Advanced targets (for experts):'
#	@echo ''
#	@echo '  conda               Build a conda package for distribution'
#	@echo '  publish-doc-jdhp    Generate and upload the docs to www.jdhp.org'
#	@echo '  publish-doc-github  Generate and upload the docs to GitHub'
#	@echo ''

# See http://stackoverflow.com/questions/4219255/how-do-you-get-the-list-of-targets-in-a-makefile

help: list

list:
	@echo "Available targets:"
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$' | xargs


###############################################################################

init:
	git submodule init
	git submodule update

lint:
	@pyflakes3 $(PYTHON_PACKAGE_NAME_SPACE)
	@pyflakes3 examples

pep8:
	@pep8 --statistics

conda:
	$(PYTHON) setup.py bdist_conda

doc:
	$(PYTHON) setup.py build_sphinx

doc-show:
	$(PYTHON) setup.py build_sphinx --open-docs-in-browser

test:
	$(PYTHON) setup.py test -V $<

trailing-spaces:
	find $(PYTHON_PACKAGE_NAME_SPACE) examples docs -name "*.py" -exec perl -pi -e 's/[ \t]*$$//' {} \;

init-skeleton:
	./init-skeleton.sh


## PUBLISH ####################################################################

init-pypi:
	python3 setup.py register

publish: publish-pypi publish-doc-jdhp

pypi-check:
	# Check if the package is OK for pypi (expecially to avoid silent errors
	# on the "long_description" argument.
	# For more information, see the following link:
	# http://inre.dundeemt.com/2014-05-04/pypi-vs-readme-rst-a-tale-of-frustration-and-unnecessary-binding/
	python3 setup.py check --restructuredtext -s

publish-pypi: pypi-check
	# Send the new package to pypi
	python3 setup.py sdist upload

publish-doc-github: doc
	ghp-import -n -p -m 'Update gh-pages docs' docs/_build/html

publish-doc-jdhp: doc
	
	########
	# HTML #
	########
	
	# JDHP_SOFTWARE_URI is a shell environment variable that contains the
	# destination URI of the HTML files.
	@if test -z $$JDHP_SOFTWARE_URI ; then exit 1 ; fi

	# Upload the HTML files
	rsync -r -v -e ssh $(HTML_TMP_DIR)/ ${JDHP_SOFTWARE_URI}/$(PYTHON_PACKAGE_NAME)/
	
	#######
	# PDF #
	#######
	
	## JDHP_DL_URI is a shell environment variable that contains the destination
	## URI of the PDF files.
	#@if test -z $$JDHP_DL_URI ; then exit 1 ; fi
	#
	## Upload the PDF file
	#rsync -v -e ssh $(PYTHON_PACKAGE_NAME).pdf ${JDHP_DL_URI}/pdf/


## CLEAN ######################################################################

init: clean

clean:
	@echo "Remove generated files"
	@find . -type d -iname "__pycache__" -exec rm -rfv {} \;
	@find . -type f -iname "*.pyc" -exec rm -v {} \;
	@find . -type f -iname "*.pyo" -exec rm -v {} \;
	@find . -type f -iname "*.pyd" -exec rm -v {} \;
	@find . -type f -iname "*.so"  -exec rm -v {} \;
	@rm -rvf docs/_build
	@rm -rvf build
	@rm -rvf dist
	@rm -rvf sdist
	@rm -rvf *.egg-info/
	@rm -rvf htmlcov/
	@rm -rvf debian
	@rm -v MANIFEST

## ANY OTHER COMMAND CAN BE PASSED TO SETUP.PY ################################

%:
	$(PYTHON) setup.py $@

