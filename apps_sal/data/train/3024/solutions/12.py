import re


def friend(x):
    true_friends = []
    for name in x:
        # checking the name's length is not enough
        # (even tho all tests are green)
        # name should contain only letters from the alphabet
        if len(name) == 4 and re.search('[a-zA-Z]', name):
            true_friends.append(name)
    return true_friends
