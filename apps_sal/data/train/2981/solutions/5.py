def solution(n,l):
    return [] if l<=0 else [int(d) for d in str(n)][-l:]
