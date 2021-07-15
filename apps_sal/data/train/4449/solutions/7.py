def solution(stones):
    result = 0
    for i in range(len(stones)-1):
        if stones[i]==stones[i+1]:
            result += 1
    return result
