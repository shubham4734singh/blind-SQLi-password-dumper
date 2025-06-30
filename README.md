# 🔐 Blind SQL Injection Script (TrackingId Cookie-Based)

This Python script performs a **blind SQL injection attack** using the `TrackingId` cookie on a PortSwigger Web Security Academy lab. 
It automates the extraction of an administrator's password using boolean-based blind SQL injection.

---

## 🚀 Features

- ✅ Automatically prompts for:
  - Lab URL
  - TrackingId
  - Session cookie
- ✅ Extracts password length using boolean-based conditions
- ✅ Extracts the password character-by-character
- ✅ Supports lowercase, uppercase, and numeric characters
- 🔜 (Optional): You can add special characters to bruteforce more complex passwords

---

## 💻 Requirements

- Python 3.x
- `requests` module (pre-installed in Kali; install manually on Windows)

To install `requests` (if needed):

```bash
pip install requests
