import logging

#New Relic Logger
logger_new_relic = logging.getLogger("newrelic")

#TODO Implement newrelic service
class NewRelicLogger(object):

    def __init__(self, config):
        self.config = config #TODO It should get new relic config

    def info(self, msg):
        logger_new_relic.info(msg)

    def error(self, msg):
        logger_new_relic.error(msg) #TODO It should send error log for new relic app

    def critical(self, msg):
        logger_new_relic.critical(msg) #TODO It should send critical log for new relic app