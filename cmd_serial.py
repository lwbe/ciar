import ciar
import serial


class cmd_serial(ciar.ciar_module):
    confstring_def = """cmd_serial(
                 serialnum|vendor,product|device,
                 baudrate="9600",
                 bytesize=serial.EIGHTBITS,
                 stopbits=serial.STOPBITS_ONE,
                 parity=serial.PARITY_NONE,
                 flow,
                 timeout)
    """

    def init(self, device_id, confstring):
        # treat the confstring to store information
        print("A.init")

    def config(self):
        pass

    def inval(self):
        pass

    def deinit(self):
        pass

    def set_a(self, v):
        pass

