# SHA-1 Password Cracker

This project is a **FreeCodeCamp** project associated with the **Information Security Certification**. The goal is to demonstrate the importance of password security by cracking passwords that have been hashed using the SHA-1 algorithm.

## Table of Contents
- [Project Overview](#project-overview)
- [How It Works](#how-it-works)
- [Running the Project](#running-the-project)
- [Testing](#testing)
- [License](#license)

## Project Overview

In this project, you will create a password cracker that takes in a SHA-1 hash of a password and returns the original password if it's one of the top 10,000 most commonly used passwords. This project demonstrates why SHA-1 is considered insecure for storing passwords and how brute-force cracking works.

Additionally, the project supports using **salts** to enhance password security, and the password cracker can handle both salted and unsalted hashes.

## How It Works

1. **SHA-1 Hash Comparison:**  
   The program reads a list of the top 10,000 commonly used passwords from the `top-10000-passwords.txt` file. Each password is hashed using the SHA-1 algorithm and compared to the input hash.

2. **Salting Support:**  
   If the `use_salts` argument is set to `True`, the program will also check each password with known salts from the `known-salts.txt` file. The salt is both prepended and appended to the password before hashing.

3. **Hashing:**  
   The Python `hashlib` library is used to create SHA-1 hashes for password comparisons.

## Running the Project

### Prerequisites

- Ensure you have Python installed on your system.

### Running the Password Cracker

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/sha1-password-cracker.git
