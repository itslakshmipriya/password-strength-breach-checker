# 🔐 Password Strength & Breach Checker

A full-stack cybersecurity tool that checks password strength in real time 
and verifies whether a password has been exposed in known data breaches — 
without ever sending the full password to a third party.

## Features
- **Real-time strength analysis** — checks length, character variety, 
  and complexity instantly in the browser
- **Breach detection** — checks passwords against the HaveIBeenPwned 
  database of 800M+ compromised passwords
- **Privacy-first design (k-anonymity)** — only the first 5 characters 
  of the password's SHA-1 hash are sent to the breach API; the full 
  password and hash never leave your own backend
- **No storage or logging** — passwords are never saved anywhere

## Tech Stack
- **Backend:** Python, Flask, Flask-CORS, Requests
- **Frontend:** HTML, CSS, JavaScript
- **API:** HaveIBeenPwned (Pwned Passwords)

## How It Works
1. User types a password into the browser.
2. JavaScript calculates a local strength score instantly.
3. On submit, the password is sent to the Flask backend.
4. Backend hashes it with SHA-1 and queries HIBP using only the hash prefix.
5. Backend checks if the full hash matches a known breach and returns the result.
6. Frontend displays the strength rating and breach status.

## Setup
```bash
git clone https://github.com/yourusername/password-checker-python.git
cd password-checker-python
pip install flask flask-cors requests
python app.py
