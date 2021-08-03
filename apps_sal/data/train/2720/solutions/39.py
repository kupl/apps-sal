def solution(digits):
    i = 0
    j = 5
    maks = 0
    while j <= len(digits):
        maks = max(maks, int(digits[i:j]))
        i += 1
        j += 1
    return maks
