import hashlib

def crack_sha1_hash(hash, use_salts=False):
    # Load the top 10,000 passwords
    with open("top-10000-passwords.txt", "r") as file:
        passwords = file.read().splitlines()
    
    # If use_salts is True, load salts
    if use_salts:
        with open("known-salts.txt", "r") as salt_file:
            salts = salt_file.read().splitlines()
    
    # Function to hash a password using SHA-1
    def sha1_hash(password):
        return hashlib.sha1(password.encode('utf-8')).hexdigest()

    # No salts - Hash each password and compare
    if not use_salts:
        for password in passwords:
            if sha1_hash(password) == hash:
                return password
    # With salts - Try prepending and appending each salt to each password
    else:
        for password in passwords:
            for salt in salts:
                # Prepend salt
                if sha1_hash(salt + password) == hash:
                    return password
                # Append salt
                if sha1_hash(password + salt) == hash:
                    return password

    return "PASSWORD NOT IN DATABASE"
