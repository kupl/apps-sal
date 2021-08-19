def reverseWords(s):
    reversed_str = ''
    s = s.split()
    for word in s:
        reversed_str = word + ' ' + reversed_str
    return reversed_str.strip()
