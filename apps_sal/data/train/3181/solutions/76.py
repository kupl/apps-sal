def check_alive(health):
    # the folowing line checks if the user's health is less than or equal to 0.
    if health <= 0:
        result = False
    # the following line will be used if line 3 is false.
    else:
        result = True
    return result
