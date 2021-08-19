#input - string
# output - list/array of words
# edge cases - no input given, integer or other data type given
# assumptions - I need to take a string and return a list of the words in the string.

# sample data - ("Robin Singh"), ["Robin", "Singh"]
# do I need to create a separate array? no
# I can just use string split function


# function string_to_array(string)
def string_to_array(s):
    return s.split(' ')
