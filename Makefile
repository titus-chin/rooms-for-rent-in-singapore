#################################################################################
# GLOBALS                                                                       #
#################################################################################

SHELL := /bin/bash
PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
PROJECT_NAME = rooms-for-rent-in-singapore

#################################################################################
# COMMANDS                                                                      #
#################################################################################

.PHONY: create-environment
## Create initial environment
create-environment:
	virtualenv ~/.virtualenvs/$(PROJECT_NAME)
	git init
	source activate.sh && \
	pip3 install -r requirements.txt && \
	pre-commit install && \
	aws s3 mb s3://$(PROJECT_NAME) && \
	black .
	git add .
	git commit -m "first commit"
	git branch -M main
	git remote add origin git@github.com:titus-chin/rooms-for-rent-in-singapore.git
	git push -u origin main
	$(MAKE) clean

.PHONY: requirements
## Update requirements.txt
requirements:
	pip3 freeze > requirements.txt

.PHONY: clean
## Delete all compiled Python files
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

.PHONY: test
## Test source code
test:
	pytest
	$(MAKE) clean

.PHONY: docs
## Make documentation for source code
docs:
	cd docs/ && $(MAKE) html
	$(MAKE) clean

.PHONY: sync-data-to-s3
## Upload data to S3
sync-data-to-s3:
	aws s3 sync data/ s3://$(PROJECT_NAME)/data/ --delete

.PHONY: sync-data-from-s3
## Download data from S3
sync-data-from-s3:
	aws s3 sync s3://$(PROJECT_NAME)/data/ data/ --delete

.PHONY: delete-project
## Delete project
delete-project:
	aws s3 rb s3://$(PROJECT_NAME) --force
	rm -r ~/.virtualenvs/$(PROJECT_NAME)
	sudo rm -r ~/Documents/github/$(PROJECT_NAME)

.PHONY: scrape-data
## Scrape rental lists from roomz.asia.
scrape-data:
	python3 src/data/rental_scraper.py
	$(MAKE) clean

.PHONY: streamlit
## Run streamlit app locally.
streamlit:
	streamlit run app.py
	$(MAKE) clean

.PHONY: update
## Update rental lists and web app.
update:
	source activate.sh && \
	$(MAKE) scrape-data && \
	$(MAKE) sync-data-to-s3
	git add .
	git commit -m "daily update"
	git push
	$(MAKE) clean

#################################################################################
# Self Documenting Commands                                                     #
#################################################################################

.DEFAULT_GOAL := help

# Inspired by <http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html>
# sed script explained:
# /^##/:
# 	* save line in hold space
# 	* purge line
# 	* Loop:
# 		* append newline + line to hold space
# 		* go to next line
# 		* if line starts with doc comment, strip comment character off and loop
# 	* remove target prerequisites
# 	* append hold space (+ newline) to line
# 	* replace newline plus comments by `---`
# 	* print line
# Separate expressions are necessary because labels cannot be delimited by
# semicolon; see <http://stackoverflow.com/a/11799865/1968>
.PHONY: help
help:
	@echo "$$(tput bold)Available rules:$$(tput sgr0)"
	@echo
	@sed -n -e "/^## / { \
		h; \
		s/.*//; \
		:doc" \
		-e "H; \
		n; \
		s/^## //; \
		t doc" \
		-e "s/:.*//; \
		G; \
		s/\\n## /---/; \
		s/\\n/ /g; \
		p; \
	}" ${MAKEFILE_LIST} \
	| LC_ALL='C' sort --ignore-case \
	| awk -F '---' \
		-v ncol=$$(tput cols) \
		-v indent=19 \
		-v col_on="$$(tput setaf 6)" \
		-v col_off="$$(tput sgr0)" \
	'{ \
		printf "%s%*s%s ", col_on, -indent, $$1, col_off; \
		n = split($$2, words, " "); \
		line_length = ncol - indent; \
		for (i = 1; i <= n; i++) { \
			line_length -= length(words[i]) + 1; \
			if (line_length <= 0) { \
				line_length = ncol - indent - length(words[i]) - 1; \
				printf "\n%*s ", -indent, " "; \
			} \
			printf "%s ", words[i]; \
		} \
		printf "\n"; \
	}' \
	| more $(shell test $(shell uname) = Darwin && echo '--no-init --raw-control-chars')
