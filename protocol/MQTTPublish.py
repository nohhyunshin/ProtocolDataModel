import json

# MQTT publish
def publish_mqtt(client, standard_data):
    topic = f"factory/{standard_data['protocol_type']}/{standard_data['device_id']}/telemetry"
    client.publish(topic, json.dumps(standard_data))