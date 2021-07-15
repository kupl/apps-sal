def solve(s):
    max_ord = 0
    curr_ord = 0
    for char in s:
        if char not in 'aeiou':
            curr_ord += ord(char)-ord('a')+1
        else:
            if curr_ord > max_ord:
                max_ord = curr_ord
            curr_ord = 0
    return max_ord

