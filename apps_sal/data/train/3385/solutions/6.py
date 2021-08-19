def longest(s):
    max_substring = ''
    substring = ''
    for ch in s:
        if substring == '' or ord(ch) >= ord(substring[-1]):
            substring += ch
        elif ord(ch) < ord(substring[-1]):
            substring = ''.join(ch)
        if len(substring) > len(max_substring):
            max_substring = substring
    return max_substring
