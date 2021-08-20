def solution(stones):
    num = 0
    for i in range(len(stones) - 1):
        if stones[i] == stones[i + 1]:
            num += 1
    return num
