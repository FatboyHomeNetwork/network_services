import subprocess
import sys
from datetime import datetime

def run_and_print():

    # 1. Generate timestamp in system format
    # Using ISO format (YYYY-MM-DD HH:MM:SS) is best for CSV sorting
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
   
    # 2. Execute the official Ookla CLI
    # --accept-license and --accept-gdpr are mandatory for background tasks
    cmd = ["speedtest.exe", "--format=csv", "--accept-license", "--accept-gdpr"]
    
    # We capture stdout; we do not use 'shell=True' for better security
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    
    # 3. Clean the output (remove trailing newlines)
    csv_data = result.stdout.strip()

    # 4. Print combined data to STDOUT
    # This is what allows '>>' to work in CMD/Bash
    if csv_data:
        print(f"{timestamp},{csv_data}")
            


if __name__ == "__main__":
    run_and_print()