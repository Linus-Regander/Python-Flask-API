IMAGE_NAME=python_user_api

build:
	DOCKER_BUILDKIT=1 docker build \
		--no-cache \
		-f Dockerfile \
		-t $(IMAGE_NAME):dev \
		.

start:
	docker compose up --build