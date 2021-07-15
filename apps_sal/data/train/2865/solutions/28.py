def solution(string):
    word=''
    for letter in reversed(string):
        word+=letter
    return word
