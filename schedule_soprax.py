import time
import subprocess
import sys

TRATE = 6  # Set the interval in minutes

print(f"[SCHEDULER] Running soprax.py every {TRATE} minutes. Press Ctrl+C to stop.")

while True:
    print("[SCHEDULER] Starting soprax.py...")
    result = subprocess.run([sys.executable, "soprax.py"])
    if result.returncode != 0:
        print(f"[SCHEDULER] soprax.py exited with code {result.returncode}")
    print(f"[SCHEDULER] Waiting {TRATE} minutes for next run...")
    time.sleep(TRATE * 60)
