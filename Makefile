run:
	docker-compose build
	docker-compose up -d
stop:
	docker-compose down
enter:
	docker-compose exec python-logger /bin/bash
start:
	docker-compose exec python-logger pipenv run start
test:
	docker-compose exec python-logger pipenv run test
lint:
	docker-compose exec python-logger pipenv run lint
format:
	docker-compose exec python-logger pipenv run format
log:
	docker-compose logs -f python-logger
