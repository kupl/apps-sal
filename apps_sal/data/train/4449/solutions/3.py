def solution(stones):
    return sum(a==b for a,b in zip(stones, stones[1:]))
