import psutil
import os
import time

# Configuration
CPU_THRESHOLD = 80.0  # CPU usage percentage threshold
CHECK_INTERVAL = 10  # Time interval to check CPU usage (seconds)
LARAVEL_SERVICE_NAME = "laravel-backend"  # Replace with your Laravel service name

# Function to check CPU usage
def is_cpu_usage_high():
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"Current CPU usage: {cpu_usage}%")
    return cpu_usage > CPU_THRESHOLD

# Function to restart the Laravel service
def restart_laravel_service():
    print(f"CPU usage exceeded {CPU_THRESHOLD}%. Restarting {LARAVEL_SERVICE_NAME}...")
    os.system(f"sudo systemctl restart {LARAVEL_SERVICE_NAME}")
    print(f"Service {LARAVEL_SERVICE_NAME} restarted successfully.")

# Main loop
if __name__ == "__main__":
    print("Starting CPU usage monitoring...")
    while True:
        if is_cpu_usage_high():
            restart_laravel_service()
        time.sleep(CHECK_INTERVAL)
