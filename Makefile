run:
	docker-compose build
	docker-compose up -d
stop:
	docker-compose down
enter:
	docker-compose exec pylogger /bin/bash
start:
	docker-compose exec pylogger pipenv run start
test:
	docker-compose exec pylogger pipenv run test
lint:
	docker-compose exec pylogger pipenv run lint
format:
	docker-compose exec pylogger pipenv run format
log:
	docker-compose logs -f pylogger
