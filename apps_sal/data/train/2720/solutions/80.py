def solution(digits):
    all = []
    j = 5
    while j <= len(digits):
        all.append(int(digits[j - 5:j]))
        j += 1
    return max(all)
