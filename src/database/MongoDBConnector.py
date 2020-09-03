from Config.config as ENV
from pymongo import MongoClient


class MongoConnector:

     """
     For connect MongoDB Database
     """

    client = MongoClient(ENV.MONGODB_URL)
    cl = client[ENV.DATABASE_NAME]

    @classmethod
    def connect(cls) -> MongoClient:
        return cls.cl

    @classmethod
    def disconnect(cls):
        return cls.client.close()
