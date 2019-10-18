import ciar

class serial(ciar.ciar_module):
    a = 2

    def init(self,serial_id):
        print("A.init")

    def config(self,serial_id):
        pass

    def inval(self,serial_id):
        pass

    def deinit(self,serial_id):
        pass

    def set_a(self,serial_id,v):
        self.a = v
