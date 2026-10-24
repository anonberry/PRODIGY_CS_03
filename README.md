# PRODIGY_CS_03

# 🔐 Password Complexity Checker

## 📌 Project Overview
The Password Complexity Checker is a Python-based application designed to evaluate the strength of a password based on several security criteria.

The program analyzes password characteristics such as length, uppercase and lowercase letters, numbers, and special characters to provide feedback and encourage users to create stronger passwords.

## 🎯 Objectives
- Understand the characteristics of strong passwords.
- Implement password validation using Python.
- Apply conditional statements and string manipulation.
- Promote password security awareness.

## ✨ Features
- **Password Length Check:** Checks whether the password meets the minimum length requirement.
- **Character Diversity:** Checks for uppercase letters, lowercase letters, digits, and special characters.
- **Weak Password Detection:** Identifies commonly used or weak passwords.
- **Pattern Detection:** Checks for repeated characters and simple sequences.
- **Strength Assessment:** Provides a password strength rating.
- **Feedback:** Suggests improvements based on the password assessment.

## 🛠️ Technologies Used
- Python 3
- Python Standard Library
  - `string`
  - `re` (if used in the implementation)

## 📁 Project Structure
```text
PRODIGY_CS_03/
│
├── password_checker.py
├── README.md
└── LICENSE
```

## 🚀 Getting Started

### Prerequisites
- Python 3 installed on your system.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/anonberry/PRODIGY_CS_03.git
   ```

2. Navigate into the project directory:
   ```bash
   cd PRODIGY_CS_03
   ```

3. Run the program:
   ```bash
   python password_checker.py
   ```

## 💻 Usage
1. Run the Python program.
2. Enter a password when prompted.
3. The program evaluates the password against its implemented criteria.
4. Review the strength rating and suggestions.

## ⚙️ How It Works
The checker evaluates the password using a set of predefined rules:

1. Checks the password length.
2. Determines whether uppercase and lowercase letters are present.
3. Checks for numbers and special characters.
4. Looks for weak passwords and simple patterns.
5. Calculates a score based on the implemented criteria.
6. Displays a strength rating and recommendations.

## 🔒 Security Considerations
- This project is an educational password assessment tool.
- A password that satisfies multiple complexity rules is not automatically secure.
- The checker does not guarantee protection against password cracking.
- Passwords should not be stored or logged in plaintext.
- Avoid entering real passwords into untrusted password-checking tools.
- For real-world password security, use established password-strength estimation methods and secure authentication practices.

## 📚 Learning Outcomes
- Improved understanding of password security principles.
- Practical experience with Python conditionals and string processing.
- Experience designing validation rules and providing user feedback.
- Awareness of the limitations of rule-based password strength checkers.

## 👨‍💻 Author
**anonberry**

GitHub: [@anonberry](https://github.com/anonberry)

## 📄 License
This project is licensed under the MIT License.
