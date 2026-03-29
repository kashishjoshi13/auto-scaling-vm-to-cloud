#!/bin/bash

echo " Threshold exceeded! Triggering cloud..."

ssh -i mykey.pem ubuntu@13.126.205.189 << EOF
echo "Connected to Cloud VM"
echo "Starting application..."
nohup python3 app.py > output.log 2>&1 &
echo "App started successfully"
EOF
