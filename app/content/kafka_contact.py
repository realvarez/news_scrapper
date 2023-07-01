"""
    TODO
"""
from os import getenv
from json import dumps
from confluent_kafka import Producer


class KafkaProducer():
    """
        Class that contains methods to send data to kafka server
    """

    def __init__(self, topic) -> None:
        self.kafka_ip = getenv('KAFKA_IP')
        self.kafka_port = getenv('KAFKA_PORT')
        self.kafka_producer = self.get_kafka_producer()
        self.topic = topic
        self.encode = 'utf-8'


    def delivery_report(self, err, msg):
        """ Called once for each message produced to indicate delivery result.
            Triggered by poll() or flush(). """
        if err is not None:
            print(f'Message delivery failed: {err}')
        else:
            print(f'Message delivered to {msg.topic()} [{msg.partition()}]')


    def get_kafka_producer(self):
        """ 
            TODO
        """
        try:
            return Producer({
                'bootstrap.servers': f'{self.kafka_ip}:{self.kafka_port}'
            })
        except ImportError:
            print("Problem to create Kafka`s Producer")
            return None

    def write_kafka(self, list_send:list)->None:
        """ 
            TODO
        """
        for element in list_send:
            self.kafka_producer.poll(0)
            self.kafka_producer.produce(self.topic,
                                        dumps(element).encode(self.encode),
                                        callback=self.delivery_report)