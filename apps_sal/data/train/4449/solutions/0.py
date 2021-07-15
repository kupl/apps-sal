def solution(s):
    st=[1 for i in range(1,len(s)) if s[i-1]==s[i]]
    return sum(st)
