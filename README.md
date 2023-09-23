# Ethical-Haking-Project
I was inspired by [InProgrammer] (https://inprogrammer.com/) 
## Project Overview
In this project, two Python scripts was created and a password file that enable users to hash passwords and perform dictionary attacks on hashed passwords,
aiming to retrieve the original plain-text password.

### Files
1. **Cracking_passwd.py**: 
   - **Description**: This script is designed to perform a dictionary attack to crack hashed passwords. It hashes each password listed in a specified file and compares it with the input hashed password.
   - **Usage**: When running this script, users will be prompted to input a hashed password and the filename (including the path) containing a list of potential plain-text passwords.
   - **Output**: If a match is discovered, the script will reveal the plain-text password corresponding to the provided hashed password.

2. **Hash_passwd.py**: 
   - **Description**: This script reads a password from a designated file and converts it into an MD5 hash.
   - **Usage**: Users are required to input the filename (including the path) containing the password when prompted.
   - **Output**: The script will then display the hashed password to the user and will handle any errors, including file not found errors, gracefully, notifying the user accordingly.

3. **password.txt**:
   - **Description**: This file serves as an input containing a plain-text password for the Python scripts.
   - **Content**: It appears to contain a single password, `YouWontGuessThisPassword:)`.
