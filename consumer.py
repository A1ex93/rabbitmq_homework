#!/usr/bin/env python
# coding=utf-8
import pika

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.1.111'))
channel = connection.channel()
channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True
                      )

channel.start_consuming()
