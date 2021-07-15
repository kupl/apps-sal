def solution(s):
    return sum(1 for i in range(len(s)) if i and s[i-1]==s[i])
