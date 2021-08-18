from typing import List


def friend(x: List[str] = ["Ryan", "Kieran", "Mark", ]):
    friends = []

    for name in x:
        if len(name) == 4:
            friends.append(name)

    return friends
