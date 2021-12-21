import wiotp.sdk.device
import time
import random
myConfig = { 
    "identity": {
        "orgId": "o79180",
        "typeId": "Device",
        "deviceId":"1234"
    },
    "auth": {
        "token": "maurya5799"
    }
}

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    heart=random.randint(20,180)
    oxygen=random.randint(0,100)
    sLevel=random.randint(0,10)
    lat=random.uniform(33,34)
    long=random.uniform(74,75)
    myData={'BPM':heart, 'sp02':oxygen, 'stress':sLevel, 'map':{"name":"Soldier", "lat":lat, "lon":long}}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    time.sleep(2)
client.disconnect()