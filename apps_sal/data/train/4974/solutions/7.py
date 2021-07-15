from itertools import zip_longest

def user_contacts(data):
    return dict(zip(*zip_longest(*data)))
