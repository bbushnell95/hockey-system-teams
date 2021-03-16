IMAGE_NAME:=bbushnell95/hockey-system-teams
IMAGE_TAG:=latest

build:
	docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .

push:
	docker push ${IMAGE_NAME}:${IMAGE_TAG}

start:
	IMAGE_NAME=${IMAGE_NAME} IMAGE_TAG=${IMAGE_TAG} docker-compose up

start-dev:
	IMAGE_NAME=${IMAGE_NAME} IMAGE_TAG=${IMAGE_TAG} docker-compose -f docker-compose.dev.yml up
