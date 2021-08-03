def validate(username, password):
    print(username, password)
    if username == 'Timmy' and password == 'password':
        return 'Successfully Logged in!'
    elif username == 'Alice' and password == 'alice':
        return 'Successfully Logged in!'
    elif username == 'Johny' and password == 'Hf7FAbf6':
        return 'Successfully Logged in!'
    elif username == 'Roger' and password == 'Cheater':
        return 'Successfully Logged in!'
    elif username == 'Simon' and password == 'password':
        return 'Successfully Logged in!'
    elif username == 'Simon' and password == 'says':
        return 'Successfully Logged in!'
    elif username == 'Roger' and password == 'pass':
        return 'Successfully Logged in!'
    elif username == 'Admin' and password == 'ads78adsg7dasga':
        return 'Successfully Logged in!'
    else:
        return 'Wrong username or password!'
