# Simple Password Cracker Using Python

## 📌 Project Overview

**Simple Password Cracker Using Python** is a beginner-friendly cybersecurity project developed to demonstrate how a **brute-force password attack** works.

The project uses Python to generate possible numeric password combinations and compare them with a **locally provided test password**. It helps students understand the basic concept of password security and why strong passwords are important.

> ⚠️ **Educational Use Only:** This project is designed only for local testing and cybersecurity education. It does not attack real websites, online accounts, Wi-Fi networks, social media accounts, or external systems.

---

## 🎯 Objectives

- Understand the basic concept of password cracking.
- Learn how a brute-force attack works.
- Understand password security.
- Practice Python programming.
- Calculate the number of attempts required.
- Measure the time taken to find a test password.
- Learn basic cybersecurity concepts.

---

## 🔐 What is Brute Force?

A **brute-force attack** is a method where many possible password combinations are tried until the correct password is found.

For example, if the test password is:

```text
1234
```

The program may try:

```text
0000
0001
0002
...
1233
1234
```

When the correct password is found, the program stops.

---

## ⚙️ How the Project Works

The project follows these basic steps:

1. The user enters a local test password.
2. The program validates the input.
3. The program generates numeric combinations from `0000` to `9999`.
4. Each generated combination is compared with the test password.
5. The program counts the number of attempts.
6. When the password matches, the program displays the result.
7. The total time taken is displayed.

---

## 🛠️ Technologies Used

- **Python**
- **VS Code**
- **Git**
- **GitHub**

No external database or internet connection is required.

---

## ✨ Features

- Simple and beginner-friendly Python code.
- Local password testing.
- Numeric brute-force demonstration.
- Attempt counter.
- Time calculation.
- Password found message.
- Basic input validation.
- Completely offline operation.

---

## 📂 Project Structure

```text
AI_Immersion_Password_Cracker/
│
├── password_cracker.py
│
└── README.md
```

---

## 💻 Requirements

Before running the project, make sure Python is installed.

Check Python version:

```bash
python --version
```

A Python 3.x version is recommended.

---

## ▶️ How to Run

### Step 1: Open the project in VS Code

Open the project folder:

```text
AI_Immersion_Password_Cracker
```

### Step 2: Open Terminal

In VS Code:

```text
Terminal → New Terminal
```

### Step 3: Run the program

```bash
python password_cracker.py
```

### Step 4: Enter a test password

Use a small numeric password such as:

```text
1234
```

---

## 📊 Sample Output

```text
========================================
     SIMPLE PASSWORD CRACKER
========================================

Enter a 4-digit test password: 1234

Trying: 0000
Trying: 0001
Trying: 0002
...
Trying: 1234

Password Found: 1234
Total Attempts: 1235
Time Taken: 0.00 seconds

========================================
        DEMONSTRATION COMPLETE
========================================
```

The exact time may differ depending on the computer.

---

## 🔒 Cybersecurity Precautions

This project is created strictly for educational purposes.

It should only be used with:

- Your own test password.
- Local applications.
- Authorized cybersecurity laboratories.
- Educational demonstrations.

It should **not** be used to:

- Attack online accounts.
- Crack another person's password.
- Attack websites.
- Attack Wi-Fi networks.
- Access systems without permission.
- Steal credentials.

---

## ✅ Advantages

- Easy to understand.
- Suitable for beginners.
- Demonstrates a real cybersecurity concept.
- Requires only Python.
- Works without internet.
- Helps understand password security.
- Can be demonstrated easily during a college presentation.

---

## ⚠️ Limitations

- The project uses only a small numeric password range.
- It is not designed for real-world password cracking.
- Longer or complex passwords would require a much larger search space.
- The demonstration is intentionally limited for safety and educational purposes.

---

## 🚀 Future Enhancements

Possible educational improvements include:

- Password strength checker.
- GUI interface using Tkinter.
- Progress indicator.
- Password security recommendations.
- Comparison of weak and strong passwords.
- Educational charts showing how password length affects brute-force difficulty.
- Hashing demonstration using locally generated test passwords.

---

## 📚 Learning Outcomes

After completing this project, students can understand:

- Basic cybersecurity concepts.
- Brute-force attacks.
- Password security.
- Python loops and conditions.
- Input validation.
- Time measurement in Python.
- Basic Git and GitHub workflow.

---

## 👨‍💻 Project Type

**AI Immersion Project**

**Domain:** Cybersecurity

**Project Level:** Beginner

**Programming Language:** Python

**Development Environment:** VS Code

**Version Control:** Git & GitHub

---

## 🏁 Conclusion

The **Simple Password Cracker Using Python** project provides a safe and simple demonstration of how brute-force password attacks work.

It helps beginners understand why weak passwords are vulnerable and why strong, unique passwords and proper security controls are important in cybersecurity.

This project is intended only for **educational and authorized local testing**.
