def solution(string):
#     return string[::-1]
    s = ''
    for i in string: 
        s = i + s
    return s 
