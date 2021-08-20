def reverseWords(s):
    for line in s.split('\n'):
        return ' '.join(line.split()[::-1])
