# end goal - function should return True if exactly ONE of two expressions evalualte to true, otherwise false
# input = two booleans, a and b
# output = boolean

# How would the computer recognize that only one boolean is True when nested? by comparing the two booleans rather than conditionals for each statement

#function xor taking two expressions a, b
def xor(a,b):
# if a is not equal to b, then only one of the expressions can be True
    return a != b

