# Play with the function in your test cases.
# When you think you've solved the
# implement the following function as your answer
# Note: you should remove any mention of the word in your code to pass the tests

def solved(s):
    l = len(s)
    s = s[0:l // 2] + s[l // 2 + 1:] if l % 2 else s
    s = list(s)
    s.sort()
    return ''.join(s)
