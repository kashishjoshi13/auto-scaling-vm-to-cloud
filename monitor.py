import psutil
import time
import os

THRESHOLD = 75

while True:
    cpu = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu}%")

    if cpu > THRESHOLD:
        print(" Threshold exceeded! Triggering cloud...")
        os.system("bash trigger_cloud.sh")
        break

    time.sleep(3)
