def solution(digits):
    i = 0
    j = 5
    largest = 0
    while j <= len(digits):
        relative = int(digits[i:j])
        if relative > largest:
            largest = relative
        i += 1
        j += 1
    return largest
