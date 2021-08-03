def validate(username, password):
    print(username, password)
    if "||" in password or "//" in password or "||" in username or "//" in username:
        return "Wrong username or password!"
    password_dict = {'Pippi': "pass", 'OMEGA=="Admin-privilege"': "alice", 'Admin': "ads78adsg7dasga", 'Timmy': 'password', "Alice": "alice", 'Simon': 'says', 'Roger': 'pass', 'Johny': 'Hf7FAbf6'}
    if password == password_dict[username]:
        return "Successfully Logged in!"
    else:
        return "Wrong username or password!"
