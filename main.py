import time
from protocol.ProtocolDevices import ModbusTCP, OPCUA, RS485
from protocol.ExceptionHandling import error_exception
from protocol.StandardLogic import to_standard_format
from protocol.MQTTPublish import publish_mqtt

devices = [
    ModbusTCP(),
    OPCUA(),
    RS485()
]

for device in devices :
    device.connect()

try :
    while True :
        for device in devices :
            try :
                raw = error_exception(device)
                meta = device.get_metadata()
                standard = to_standard_format(raw,meta)
                publish_mqtt(standard)
                print(standard)
            except Exception as e :
                print(e)
        time.sleep(1)
except KeyboardInterrupt:
    print("프로그램 종료")
    for device in devices :
        device.disconnect()   