# https://www.rabbitmq.com/tutorials/tutorial-two-python.html

# modifies previous send. Now message is set in the command line call

import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode=2  # message persistent
                      ))
# not guarantees 100% resilience. 
# For higher guarantees, check: https://www.rabbitmq.com/confirms.html


print(" [x] Sent %r" % message)
connection.close()

import sys
