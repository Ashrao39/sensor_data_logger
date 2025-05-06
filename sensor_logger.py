import random
import time

def read_sensor():
    return {
        "temperature": round(random.uniform(20.0, 30.0), 2),
        "humidity": round(random.uniform(30.0, 60.0), 2)
    }

print("Starting sensor data simulation...")
for i in range(10):
    data = read_sensor()
    print(f"[{i+1}] Temp: {data['temperature']}°C, Humidity: {data['humidity']}%")
    time.sleep(1)
