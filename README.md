# Brainwave_Matrix_Intern

# 🛡️ Phishing Link Scanner (Python)

Basic Phishing Link Scanner (No External Libraries)

## 📌 Introduction

This is a simple Python-based phishing link scanner created for beginners in cybersecurity and Python programming. The scanner analyzes a URL entered by the user and checks it against a simulated blacklist, suspicious keywords, and IP address formats to identify potentially dangerous links.

The project does not use any external libraries, making it lightweight and easy to understand for educational purposes.

---

## 📌 What is a Phishing Link Scanner?
A Phishing Link Scanner is a cybersecurity tool that analyzes a website link (URL) to check if it might be malicious or fake.

Phishing links are often used by cybercriminals to trick people into revealing personal information, such as passwords, banking details, or credit card numbers.

---

## 📌 Project Overview
This is a Python-based **Cyber Security tool** that scans and analyzes URLs to detect possible **phishing attempts** using heuristic checks such as:
- Suspicious keywords
- IP addresses instead of domain names
- Too many subdomains
- Non-HTTPS connections
Requires no external Python libraries.

This project is built for **Kali Linux** but works on any system with Python 3.

---

## 📌 How to Use

Run the Python script.

When prompted, enter the URL you want to scan.

The scanner will analyze the URL and print the results.

---

## 📌 Example Test URL
For testing, you can use:

http://paypal-secure-login.example.com/verify
Expected result: Suspicious due to keywords (login, verify), not HTTPS, and multiple subdomains.

---

## 📌 Disclaimer

This tool performs a basic scan and is intended for learning purposes only. It does not replace advanced threat detection systems or antivirus software.
