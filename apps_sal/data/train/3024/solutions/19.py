# def friend(x):
#     friends = []
#     for friend in x:
#         if len(friend) == 4:
#             friends.append(friend)
#         return friends


def friend(x):
    return [friend for friend in x if len(friend) == 4]
