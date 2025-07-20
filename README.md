# PRODIGY_CS_02
 Password Complexity Checker
#  Password Complexity Checker

# Task: Build a Password Strength Evaluation Tool

This project is part of my cybersecurity internship. The goal is to create a Python-based tool that evaluates the strength of a user's password and provides feedback based on security best practices.

# Features

- ✅ Checks password **length**
- ✅ Detects presence of **uppercase** and **lowercase** letters
- ✅ Verifies inclusion of **numbers** and **special characters**
- ✅ Gives feedback on **strength level** (Weak, Medium, Strong)
- ✅ Simple and interactive terminal input/output

# Technologies Used

- Programming Language: **Python 3**
- No external libraries required

# How the Strength is Determined

| Criteria                         | Points |
|----------------------------------|--------|
| Length ≥ 8 characters            | +1     |
| Contains uppercase letters       | +1     |
| Contains lowercase letters       | +1     |
| Contains digits                  | +1     |
| Contains special characters (!@#...) | +1     |

- **0-2 Points** → Weak  
- **3-4 Points** → Medium  
- **5 Points** → Strong  

# How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/password-complexity-checker.git
   cd password-complexity-checker

2. python3 password_checker.py

3. Example output

Enter your password: Hello@123
Password Strength: STRONG
Good job! Your password meets all major security criteria.



