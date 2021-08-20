def middle_permutation(string):
    s = ''.join(sorted(string))
    mid = int(len(s) / 2) - 1
    if len(s) % 2 == 0:
        return s[mid] + (s[:mid] + s[mid + 1:])[::-1]
    else:
        return s[mid:mid + 2][::-1] + (s[:mid] + s[mid + 2:])[::-1]
