def solution(digits):
    x = [digits[index:index + 5] for index, value in enumerate(digits)]
    resul = max(x)
    return int(resul)
