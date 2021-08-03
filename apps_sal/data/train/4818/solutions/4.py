def solution(a, b): return "{0}{1}{0}".format(min(a, b, key=len), max(a, b, key=len))
