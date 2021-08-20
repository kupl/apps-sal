def password(candidate):
    """Returns True if 'candidate' password possesses arbitrary properties that do more than
       good for security of the users' accounts. It is probably accompanied by a password 
       field in which paste is disabled. Notice that a maximum character length is not specified.
       This is so we can silently truncate the users' passwords before hashing and storing
       them so that when they attempt to log in later, they have to guess how many characters
       we truncated. We might also do this differently on different clients so the same password
       works in some instances and fails in others. We will also impliment all this client side, 
       so the validation is easily defeated by anyone willing to monkey with our client-side script.
       Then we will add 'security questions' based on publicly available information, allowing
       anyone to sidestep authentication with a basic search.

       Otherwise, False.
    """
    if not len(candidate) >= 8:
        return False
    if not any((char.islower() for char in candidate)):
        return False
    if not any((char.isupper() for char in candidate)):
        return False
    if not any((char.isdigit() for char in candidate)):
        return False
    return True
