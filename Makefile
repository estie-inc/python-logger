run:
	docker-compose build
	docker-compose up -d
stop:
	docker-compose down
enter:
	docker-compose exec python-logger /bin/bash
start:
	docker-compose exec python-logger poetry run start
test:
	docker-compose exec python-logger poetry run test
lint:
	docker-compose exec python-logger poetry run lint
format:
	docker-compose exec python-logger poetry run format
log:
	docker-compose logs -f python-logger
