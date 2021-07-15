def prime_string(s):
    for i in range(len(s) // 2):
        if s[:i + 1] * (len(s)//len(s[:i+1])) == s : return 0
    return 1
