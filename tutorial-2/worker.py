# the previous receive program.
# Now it fakes 1 second of work for every dot in the received message.

import pika
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
# Queue marked as persistent
# durable to make it resilient to rabbit service break
# if queue is already declared, won't be redeclared.
# * messages must be published as persistent too...


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)
    # allows rabbit to get rid of non acknowledged messages


channel.basic_qos(prefetch_count=1)
channel.basic_consume(
    queue='task_queue', on_message_callback=callback, auto_ack=False)
    # auto_ack is False by default. True turns off the ack system

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()