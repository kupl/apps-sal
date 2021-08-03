def solution(digits):
    mnum = 0
    for i in range(5, len(digits)):
        for j in range(i, len(digits) + 1):
            if int(digits[j - 5:j]) > mnum:
                mnum = int(digits[j - 5:j])
    return mnum
