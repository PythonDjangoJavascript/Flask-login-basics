from flask_bcrypt import Bcrypt
from werkzeug.security import generate_password_hash, check_password_hash


bcrypt = Bcrypt()


def passHassing(password="mySuperSecretPassword"):

    hasshed_password = bcrypt.generate_password_hash(password)
    return(hasshed_password)


hassedPassword = passHassing()


def checkPassword(password):
    return bcrypt.check_password_hash(hassedPassword, password)


# With werkzeurg
hassed_pass_with_werk = generate_password_hash("mySuperSecretPassword")
print(f"Using Werkzeurg: {hassed_pass_with_werk}")
print(check_password_hash(hassed_pass_with_werk, "wrongPassword"))
print(check_password_hash(hassed_pass_with_werk, "mySuperSecretPassword"))

if __name__ == '__main__':
    print(passHassing())
    print(checkPassword("mySuperSecretPassword"))
