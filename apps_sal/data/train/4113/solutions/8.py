def solution(n): c = lambda x: (n - 1) // x if x == 15 else (n - 1) // x - c(15); return [c(3), c(5), c(15)]
