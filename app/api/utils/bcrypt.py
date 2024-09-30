import bcrypt

def hash_password(password: str)->str:
    
    encode_pass = password.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(encode_pass, salt)

def check_pass(hashed_pass:str, plain_pass:str)-> bool:

    encode_pass = plain_pass.encode('utf-8')
    return True if bcrypt.checkpw(encode_pass, hashed_pass) else False
