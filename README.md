# cybersec-internship-task6-password-strength
Password strength evaluation and report generation for Cyber Security Internship Task 6
# 🔐 Password Strength Checker – Cybersecurity Internship Task 6

## 📌 Objective

The objective of this task is to understand the elements that make a password strong, test various passwords using online strength checking tools, and document the results and insights.

---

## 🛠 Tools Used

- [passwordmeter.com](https://www.passwordmeter.com)
- Python (basic strength scoring script)
- Google Sheets / Docs (for analysis and reporting)

---

## 📁 Project Structure
password-strength-checker/
├── data/
│ └── password_results.csv # Passwords tested and their scores
├── images/
│ └── screenshot.png # Tool usage screenshot (if any)
├── src/
│ └── strength_checker.py # Python script for scoring
├── report/
│ └── report.pdf # Summary of findings
├── README.md # Project overview

---

## 🧪 Passwords Tested

| Password     | Length | Uppercase | Lowercase | Digit | Special Char | Complexity Score | Strength Category |
| ------------ | ------ | --------- | --------- | ----- | ------------ | ---------------- | ----------------- |
| Passw0rd!    | 9      | Yes       | Yes       | Yes   | Yes          | 8.0              | Strong            |
| 123456       | 6      | No        | No        | Yes   | No           | 2.5              | Weak              |
| Admin#2025   | 10     | Yes       | Yes       | Yes   | Yes          | 8.5              | Strong            |
| password     | 8      | No        | Yes       | No    | No           | 3.0              | Weak              |
| Secur3\@123  | 10     | Yes       | Yes       | Yes   | Yes          | 9.0              | Very Strong       |
| Qwerty!      | 7      | Yes       | Yes       | No    | Yes          | 5.5              | Medium            |
| StrongPass99 | 12     | Yes       | Yes       | Yes   | No           | 7.5              | Strong            |
| abcdef       | 6      | No        | Yes       | No    | No           | 2.0              | Weak              |
| Test\@2023   | 9      | Yes       | Yes       | Yes   | Yes          | 8.5              | Strong            |
| MyPass\$1    | 8      | Yes       | Yes       | Yes   | Yes          | 7.5              | Strong            |

---

## 🔍 Key Learnings

- Password strength improves with:
  - **Length ≥ 12 characters**
  - Use of **uppercase, lowercase, digits, and special characters**
  - Avoiding dictionary words and patterns
- **Passphrases** (e.g., `Purple!Dog3Likes_Tea`) are both strong and memorable.
- Avoid reusing passwords across sites.

---

## 🛡 Common Attacks

- **Brute Force Attack**: Tries all character combinations.
- **Dictionary Attack**: Uses a list of common passwords and words.
- **Credential Stuffing**: Uses leaked credentials on multiple sites.

---
