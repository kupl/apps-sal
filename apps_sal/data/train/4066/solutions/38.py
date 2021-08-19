# Write a function to split a string and convert it into an array of words.
# For example:
# "Robin Singh" ==> ["Robin", "Singh"]


def string_to_array(s):
    return s.split() if s != "" else [""]
