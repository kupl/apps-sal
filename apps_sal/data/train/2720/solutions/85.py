def solution(digits):
    maxseq = 0
    for x in range(len(digits) - 4):
        if int(digits[x:x + 5]) > maxseq:
            maxseq = int(digits[x:x + 5])
    return maxseq


