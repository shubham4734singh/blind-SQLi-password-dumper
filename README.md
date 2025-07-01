# 🔐 Blind SQL Injection Tool (TrackingId Cookie-Based)
# If Payloads not just change the payloads in code.........
This Python script automates **blind SQL injection attacks** using the `TrackingId` cookie header, primarily targeting labs like those on **PortSwigger Web Security Academy**.

It supports:
- **Boolean-based blind SQLi**
- **Error-based blind SQLi** (Oracle-style using `TO_CHAR(1/0)`)

The goal is to extract the **administrator's password** character by character using customized payloads, with support for various SQL dialects.

> ⚠️ **For educational use only** on authorized systems.

---

## 🚀 Features

- ✅ Works with both **Boolean-based** and **Error-based** blind SQL injection
- ✅ Automatically prompts for:
  - 🔗 Lab URL
  - 🍪 TrackingId
  - 🔐 Session ID
- ✅ Detects password length automatically
- ✅ Extracts password one character at a time
- ✅ Supports lowercase, uppercase, and numeric characters
- 🔧 Easily modify character set to include special characters if needed

---

## 💻 Requirements

- Python 3.x
- `requests` module

To install the dependency:

```bash
pip install requests
