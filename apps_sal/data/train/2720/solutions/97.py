def solution(digits):
    numlist = [int(digits[i:i+5]) for i in range(0,len(digits)-4)]
    return max(numlist)
def solution(digits):
    return int(max(digits[a:a + 5] for a in range(len(digits) - 4)))
def solution(digits):
    result = -1;
    for i in range(len(digits)):
        current = int(digits[i: i+5])
        if current >= result:
            result = current
    return result


