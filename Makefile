SHELL=/bin/bash
ENV_NAME=cloudsme_stats
ACTIVATE_ENV=source /usr/local/bin/virtualenvwrapper.sh; workon ${ENV_NAME}

.PHONY: python_env bundle

bundle: python_env
	${ACTIVATE_ENV}; pyinstaller -F --clean cloudsigma_stats.spec

python_env:
	-source /usr/local/bin/virtualenvwrapper.sh; mkvirtualenv --no-site-packages ${ENV_NAME}
	${ACTIVATE_ENV}; pip install -r requirements.txt	
