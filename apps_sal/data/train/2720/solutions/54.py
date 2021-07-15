def solution(digits):
    f = lambda x: [x[i:i+5] for i in range(len(x)+1-5)]
    numbers = str(digits)
    return max(list(map(int, f(numbers))))

