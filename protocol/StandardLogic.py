from datetime import datetime

#  단일 표준 데이터 포맷으로 변환
def to_standard_format (raw_data : dict, metadata : dict) :
    return {
        "timestamp" : datetime.utcnow().isoformat(),
        "protocol_type" : metadata["protocol_type"],
        "device_id" : metadata["device_id"],
        "data" : raw_data       
    }