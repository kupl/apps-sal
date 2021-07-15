def solution(string, ending):
    if string.endswith(ending):
        return True
    else:
        return False
print(solution('abc','bc'))
print(solution('abc','d'))
