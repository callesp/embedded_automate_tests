import serial
import threading

PORT = 'COM1'
BAUDRATE = 9600


class Serial:
    _instance_lock = threading.Lock()

    @classmethod
    def instance(cls, *args, **kargs):
        if not hasattr(Serial, '_instance'):
            with Serial._instance_lock:
                if not hasattr(Serial, '_instance'):
                    Serial._instance = serial.Serial(PORT, BAUDRATE, timeout=1)

        return Serial._instance


# ser = Serial.instance()
