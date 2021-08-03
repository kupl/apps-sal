def build_palindrome(s):
    p = []
    for i in range(len(s)):
        string = s + s[:i][::-1]
        if string == string[::-1]:
            p.append(string)
    return min(p, key=lambda i: len(i))
