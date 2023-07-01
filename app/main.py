from requests import get
from os import getenv 
from json import dumps
from confluent_kafka import Producer


def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')



def get_kafka_producer(kafka_ip:str,kafka_port:int):
    """ 
        TODO
    """
    try:
        return Producer({
            'bootstrap.servers': f'{kafka_ip}:{kafka_port}'
        })
    except ImportError:
        print("Problem to create Kafka`s Producer")


def write_kafka(producer:Producer, list_send:list):
    """ 
        TODO
    """
    for data in list_send:
        producer.poll(0)
        producer.produce('first_topic',
                        dumps(data).encode('utf-8'),
                        callback=delivery_report)



def get_news():
    """
        Method that get data from currentapi
        Return: List of news
    """
    api_key = getenv('API_KEY')
    api_url = f'https://api.currentsapi.services/v1/latest-news?language=es&apiKey={api_key}'
    response = get(url=api_url, timeout=4)
    return response.json()

def main():
    """
        Main function start when the file is executed.
    """
    return 0


if __name__== "__main__":
    main()
