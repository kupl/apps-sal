def solution(string):
    string2 = ''
    for x in range(0,len(string)):
        string2 += string[len(string)-x-1]
    return(string2)
