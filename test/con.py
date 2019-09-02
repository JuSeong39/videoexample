import time
import os
from kafka import *

topic = "time-test"
key = "SHINEE KEY"
data = "lucifer"
consumer = KafkaConsumer(topic, bootstrap_servers=['localhost:9090'], auto_offset_reset = 'earliest')
consumer.subscribe(topic)
for msg in consumer:
	#print("{}, {}, {}".format(msg.key, msg.timestamp, msg.value))
	#print(msg)
	#str1 = msg.value.split(',')
	#print("{}, {}".format(str1[0], str1[2]))
	img = base64.b64decode(msg)
	cv2.imshow('image', img)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
