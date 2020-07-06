rabbit-run:
	docker run -d -p 5672:5672 -p 15672:15672 --name rabbitmq rabbitmq

rabbit-start:
	docker start rabbitmq

rabbit-list:
	docker exec -it rabbitmq rabbitmqctl list_queues name messages_ready messages_unacknowledged
	
