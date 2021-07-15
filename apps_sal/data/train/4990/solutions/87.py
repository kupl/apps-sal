def solution(string, ending):
    lengh1 = len(string)
    lengh2 = len(ending)
    if string.find(ending,lengh1-lengh2) != -1 :
        return True
    else:
        return False

