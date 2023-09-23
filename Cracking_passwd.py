import hashlib

def get_hashed_password():
    """Requests the user to enter a hashed password and then retrieves it."""
    return input("Enter the hashed password: ")

def get_password_filename():
    """Prompts user for password filename and returns it"""
    return input("Enter passwords filename including path (e.g. /root/home/passwords.txt): ")

def open_password_file(filename):
    """Attempts to open the specified file and returns the file object, or None if the file couldn't be opened"""
    try:
        return open(filename, 'r')
    except FileNotFoundError:
        print("Error: File", filename, "not found. Please give the path of the file correctly.")
        return None

def find_password_in_file(hashed_password, password_file):
    """Attempts to find a password in the password_file that matches the hashed_password and returns the password if found"""
    for word in password_file:
        enc_word = word.encode('utf-8')  # Encoding the word into utf-8 format
        hash_word = hashlib.md5(enc_word.strip())  # Hashing a word into md5 hash
        digest = hash_word.hexdigest()  # Digesting that hash into a hexadecimal value

        if digest == hashed_password:  # Comparing hashes
            return word.strip()

    return None

def main():
    print("-------------- PASSWORD CRACKER --------------")
    
    hashed_password = get_hashed_password()
    password_filename = get_password_filename()
    password_file = open_password_file(password_filename)
    
    if password_file:
        password = find_password_in_file(hashed_password, password_file)
        password_file.close()  # Close the password file after reading
        
        if password:
            print("Password found. The password is:", password)
        else:
            print("Password is not found in the", password_filename, "file")

    print(" Thank you :) <3 ")


if __name__ == "__main__":
    main()
