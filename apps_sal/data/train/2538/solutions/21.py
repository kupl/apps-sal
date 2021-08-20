class Solution:

    def countLargestGroup(self, n: int) -> int:
        if n == 2:
            return 2
        mix = {}
        for i in range(1, n + 1):
            if dsum(i) not in mix:
                mix[dsum(i)] = [i]
            else:
                mix[dsum(i)].append(i)
        mx = 0
        for i in list(mix.values()):
            if len(i) > mx:
                mx = len(i)
        resc = 0
        for i in list(mix.values()):
            if len(i) == mx:
                resc = resc + 1
        return resc


def dsum(digit):
    cnt = 0
    while digit > 0:
        temp = digit % 10
        cnt = cnt + temp
        digit = digit // 10
    return cnt
