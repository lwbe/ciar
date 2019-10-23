# contains the base class for each module and
# commands to send data to redis server.

import logging
import redis

# setting logging facility
logging.basicConfig(level=logging.INFO)


# the base class module
class ciar_module():
    confstring_def = None
    instances = {}

    def __init__(self):
        logging.info("Instanciation of class %s", self.__class__)
        if not self.confstring_def:
            raise Exception("No confstring definition !!")
        # create a connexion to the redis database
        self.redis = redis.Redis()
        try:
            logging.info("connect to redis server : %s" % self.redis.client())
        except ConnectionRefusedError as e:
            raise Exception("Cannot connect to redis server check if it is started: Error %s" % e)
        except Exception as e:
            raise Exception("Probleme with redis server check if it is started: Error %s" % e)

# --
    def init(self, device_id, confstring):
        if device_id in self.instances:
            raise Exception("%s already defined!!" % device_id)

        logging.info("Treating confstring %s " % confstring)
        self.instances[device_id] = self

# --
    def deinit(self,device_id):
        self.instances.pop(device_id)

# --
    def config(self):
        pass

# --
    def set(self, key, value):
        pass

# --
    def check(self):
        logging.info("check if class is well defined")



def send_command(channel,*args):
    pass