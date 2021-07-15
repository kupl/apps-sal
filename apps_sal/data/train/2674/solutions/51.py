# You will be given an vector of string(s).
# You must sort it alphabetically (case-sensitive, and based on the ASCII 
# values of the chars) and then return the first value.

# The returned value must be a string, and have "***" between each of its letters.

# You should not remove or add elements from/to the array.


def two_sort(list):
    # your code here
    list.sort()
    y = list[0]
    res = '***'.join(y[i:i + 1] for i in range(0, len(y), 1))
    return res
