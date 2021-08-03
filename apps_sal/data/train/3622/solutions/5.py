def validate_usr(username):
    numeric = "0123456789"
    if len(username) >= 4 and len(username) <= 16:
        for letter in username:
            status = 0
            if letter.islower() or letter == "_":
                status = 1
            for num in numeric:
                if letter == num:
                    status = 1
            if status == 0:
                return False
        return True
    else:
        return False
