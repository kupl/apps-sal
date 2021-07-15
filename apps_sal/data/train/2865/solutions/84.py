def solution(string):
    word=''
    for i in range(-len(string),0):
        word=string[i]+word
    return word
