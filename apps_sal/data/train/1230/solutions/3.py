from math import log
flips = {}


def get_flip(a, b):
    temp = a ^ b
    ans = log(temp) / log(2)
    return int(ans)


def main():
    n = input()
    nums = input()
    nums = [int(i) for i in nums.split()]
    l = len(nums)
    for i in range(1, l):
        f = get_flip(nums[i - 1], nums[i])
        if f in flips:
            if flips[f] != i - 1:
                print('Yes')
                return
        else:
            flips[f] = i

    rec = {}
    for i in nums:
        if i in rec:
            rec[i] += 1
        else:
            rec[i] = 1

    r = 0
    for i in rec:
        if rec[i] > 1:
            r += int(rec[i] / 2)
        if r == 2:
            print('Yes')
            return
    print('No')
    return


def __starting_point():
    main()


__starting_point()
