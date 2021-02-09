# ARGS:
# V: version - ex: v1.0.0

.DEFAULT_GOAL: build

build:
	docker build -t gcr.io/rowan-senior-project/tensorbeat-scraper:$(V) .

push:
	docker push gcr.io/rowan-senior-project/tensorbeat-scraper:$(V)

build_and_push: build push