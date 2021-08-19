def solution(s):
    final_string = ''
    for i in range(len(s)):
        char = s[i]
        if char.isupper():
            final_string += ' ' + char
        else:
            final_string += char
    return final_string
