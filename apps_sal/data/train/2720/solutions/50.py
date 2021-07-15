def solution(digits):
    lst = []
    for i in range(len(digits)):
        lst.append(digits[i:i+5])
    return int(max(lst))
