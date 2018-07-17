import logging

#New Mongo Logger
logger_mongo = logging.getLogger("mongo")

#TODO Implement mongo db log
class NewMongoLogger(object):

    def __init__(self, config):
        self.config = config #TODO It should get a mongo config

    def info(self, msg):
        logger_mongo.info(msg)

    def error(self, msg):
        logger_mongo.error(msg) #TODO It should send error log for mongo db

    def critical(self, msg):
        logger_mongo.critical(msg) #TODO It should send critical log for mongo db