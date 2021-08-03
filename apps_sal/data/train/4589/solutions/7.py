def solution(a, i, v): return (v, a[i % len(a)])[abs(i) <= len(a)]
