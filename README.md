# Auto Scaling from Local VM to Cloud

This project demonstrates a basic auto-scaling mechanism by monitoring CPU usage on a Local Virtual Machine and triggering deployment on an AWS EC2 cloud instance when usage exceeds a defined threshold.

---

## Objective

To monitor CPU usage on a local VM and automatically trigger cloud deployment when CPU usage exceeds 75%.

---

## Tools Used

- VirtualBox  
- Ubuntu  
- Python (psutil, flask)  
- AWS EC2  
- SSH  

---

## Project Structure

auto-scaling-vm-to-cloud/

monitor.py           # CPU monitoring script  
trigger_cloud.sh     # Script to trigger cloud via SSH  
app.py               # Flask application (runs on cloud)  
README.md  

---

## How It Works

1. monitor.py continuously checks CPU usage using psutil  
2. If CPU usage > 75%, it triggers trigger_cloud.sh  
3. The script connects to AWS EC2 via SSH  
4. The Flask application (app.py) is started on the cloud  
5. User accesses the app via browser  

---

## Running the Project

Step 1: Run Monitoring Script

python3 monitor.py

---

Step 2: Simulate High CPU Load

yes > /dev/null &

---

Step 3: Cloud Deployment Trigger

When CPU exceeds 75%, cloud deployment starts automatically.

---

## Output

Access the deployed application:

http://13.126.205.189:5000

---

## Key Concepts

- Resource Monitoring (CPU usage)  
- Threshold-based Triggering  
- SSH Automation  
- Cloud Deployment (AWS EC2)  
- Basic Auto-Scaling Simulation  

---

## Conclusion

This project successfully simulates auto-scaling by integrating local resource monitoring with cloud deployment using AWS EC2.

---

## Author

Kashish 
