import bcrypt

def hased_password(password: str) -> str:
    """Creates a hashed password using bcrypt.

    Args:
        password (str): The password to be hashed.

    Returns:
        str: The hased password as UTF-8 encoded string.
    """
    hashed = bcrypt.hashpw(password.encode("UTF-8"), bcrypt.gensalt()).decode("UTF-8")
    return hashed

def check_password(hashed_password: str, password: str) -> bool:
    """Checks user password agasint encoded password.

    Args:
        hashed_password (str): The encoded password string to check against password.
        password (str): The password to check. 

    Returns:
        bool: True if the password matches the hased_password, and False otherwise. 
    """
    
    return bcrypt.checkpw(password.encode("UTF-8"), hashed_password.endcode("UTF-8"))