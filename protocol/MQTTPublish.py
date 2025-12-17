import json

# MQTT publish
def publish_mqtt(standard_data):
    topic = f"factory/{standard_data['protocol_type']}/{standard_data['device_id']}/telemetry"
    payload = json.dumps(standard_data)
    return payload