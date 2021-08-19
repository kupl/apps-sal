import re


def friend(x):
    true_friends = []
    for name in x:
        if len(name) == 4 and re.search('[a-zA-Z]', name):
            true_friends.append(name)
    return true_friends
