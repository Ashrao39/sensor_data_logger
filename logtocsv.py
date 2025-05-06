import random
import csv
from datetime import datetime

def read_sensor():
    return {
        "temperature": round(random.uniform(20.0, 30.0), 2),
        "humidity": round(random.uniform(30.0, 60.0), 2)
    }

with open('sensor_data_log.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Temperature", "Humidity"])

    for _ in range(10):
        data = read_sensor()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([timestamp, data["temperature"], data["humidity"]])
        print(f"Logged: {timestamp} | {data}")
