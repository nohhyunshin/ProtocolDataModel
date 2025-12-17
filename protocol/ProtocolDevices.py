from abc import ABC, abstractmethod

# 산업용 프로토콜 장비에 공통적으로 적용되는 인터페이스

class ProtocolDevices(ABC) :
    @abstractmethod
    def connect(self) : pass

    @abstractmethod
    def disconnect(self) : pass

    @abstractmethod
    def read_data(self) -> dict : pass

    # MQTT Topic 및 표준 데이터 포맷 생성
    @abstractmethod
    def get_metadata(self) -> dict : pass


# Modbus TCP 시뮬레이터
class ModbusTCP (ProtocolDevices) :
    def connect(self) :
        print("Modbus TCP Connected")
    
    def disconnect(self) :
        print("Modbus TCP disconneted")

    """
    레지스터 기반의 데이터 반환
    holding register의 주소 공간은 40001 - 49999
    """
    def read_data(self) :
        return {
            "holding_register_40001" : 123,
            "holding_register_40002" : 456,
            "holding_register_40003" : 789
        }
    
    def get_metadata(self) :
        return {
            "protocol_type" : "modbus_tcp",
            "device_id" : "modbus_01"
        }


# OPC-UA 시뮬레이터
class OPCUA (ProtocolDevices) :
    def connect(self) :
        print("OPC-UA connected")
    
    def disconnect(self):
        print("OPC-UA disconnected")
    
    # Node 기반의 데이터 구조 (온도, 압력 등의 변수)
    def read_data(self) :
        return {
            "temperature" : 26,
            "pressure" : 1.2
        }
    
    def get_metadata(self) :
        return {
            "protocol_type" : "opc-ua",
            "device_id" : "opcua_01"
        }
    
# RS485 시뮬레이터
class RS485 (ProtocolDevices) :
    def connect(self):
        print("RS485 connected")

    def disconnect(self):
        print("RS485 disconnected")
    
    def read_data(self) :
        return {
            "temperature": 5.7,
            "humidity": 73
        }
    
    def get_metadata(self) :
        return {
            "protocol_type" : "rs485",
            "device_id" : "rs485_01"
        }
