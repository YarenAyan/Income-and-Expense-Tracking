import bcrypt

def hash_password(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)

def check_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed)
