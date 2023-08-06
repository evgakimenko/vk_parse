include .env

dev: stop start

stop:
	docker-compose down

start:
	docker-compose up -d --build



