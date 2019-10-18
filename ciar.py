# contains the base class for each module and
# commands to send data to redis server.


class ciar_module():

    def __init__(self):
        print("in init")
        print(dir(locals()["self"]))

    def init(self):
        print("pyrame_module.init")

    def set(self,key,value):
        pass



def send_command(channel,*args):
    pass