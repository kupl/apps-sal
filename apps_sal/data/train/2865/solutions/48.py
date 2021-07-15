def solution(word):
    newword = ''
    for letter in word:
        newword = letter + newword
    return newword
