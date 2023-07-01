"""
    Process file
"""
from content.current_news import CurrentNews
from content.kafka_contact import KafkaProducer

class Process():
    """
        Class that start the process
    """

    def start_process(self):
        """
            Execution of processing steps
        """
        news = CurrentNews().get_news()
        KafkaProducer("news_topic").write_kafka(news)
    