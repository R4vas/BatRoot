![BatRoot.](https://dinoproject.blogs.bristol.ac.uk/files/2019/10/BatShape.png)


# BatRoot - The Ultimate Root Access Tool

Welcome to **BatRoot**, a powerful tool designed to extract and display sensitive information from Linux systems. **BatRoot** is capable of accessing and viewing contents from critical files such as `/etc/passwd` and `/etc/shadow`, which are essential for user account management and system authentication.

**⚠️ Warning:** This tool requires **sudo** to run properly. Using it without root privileges may result in failure or incomplete output.

---

## 🚨 Features
- **Extracts `/etc/passwd`**: Access the system's user account details, such as usernames and user IDs.
- **Extracts `/etc/shadow`**: Retrieve password hashes for user accounts.
- **Root Privileges Required**: This tool performs tasks that require administrative privileges, so make sure to run it with `sudo`.

---

## ⚡ Installation and Setup

To get started with **BatRoot**, follow these steps:

### 1. Clone the repository

Open a terminal and clone the repository:

```bash
git clone https://github.com/R4vas/BatRoot.git
cd BatRoot
sudo python batroot.py
```

##Picture of BatRoot!
![BatRoot.python](batroot.png)


