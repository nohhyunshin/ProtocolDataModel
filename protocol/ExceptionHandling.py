import time
from protocol.ProtocolDevices import ProtocolDevices

MAX_RETRY = 3

# 통신 지연, 연결 끊김, 재시도 필요 상황 등 예외 상황을 처리
def error_exception (device: ProtocolDevices) :
    retry = 0
    while retry < MAX_RETRY :
        try : 
            return device.read_data()
        except KeyboardInterrupt:
            print("프로그램 종료")
            raise
        except Exception as e :
            retry += 1
            time.sleep(1)   # 1초 주기로 데이터 생성
    raise ConnectionError("Device read failed")