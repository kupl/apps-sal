def who_is_paying(name):
    if name == name[0:2]:
        return [name]
    else:
        return [name, name[0:2]]


# show Full name of the neighbor and the truncated version of the name
# as an array.

# If the number of the characters in name is equal or less than two,
# it will return an array containing only the name as is"
