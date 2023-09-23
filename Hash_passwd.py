import hashlib

def get_password_from_file(filename):
    try:
        with open(filename, 'r') as file:
            password = file.readline().strip()
            return password
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    filename = input("Enter the filename including path (e.g. /path/to/your/file.txt): ")
    password = get_password_from_file(filename)  # Make sure this line is exactly like this

    if password:
        hashed_password = hashlib.md5(password.encode()).hexdigest()
        print("Hashed Password (MD5):", hashed_password)

if __name__ == "__main__":
    main()
