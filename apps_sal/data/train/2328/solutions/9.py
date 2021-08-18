def subsetsum(array, num):

    if num == 0 or num < 1:
        return False
    elif len(array) == 0:
        return False
    else:
        if array[0] == num:
            return True
        else:
            return subsetsum(array[1:], (num - array[0])) or subsetsum(array[1:], num)


n, q = [int(i) for i in input().split()]
l = [int(i) for i in input().split()]
while q > 0:
    q -= 1
    s = []
    s = [int(i) for i in input().split()]
    if s[0] == 3:
        l1 = int(s[1])
        r = int(s[2])
        w = int(s[3])
        if subsetsum(l[l1 - 1:r], w) == True:
            print("Yes")
        else:
            print("No")
    elif s[0] == 2:
        l1 = int(s[1])
        r = int(s[2])
        l1 -= 1
        r -= 1
        k = l[l1:r + 1]
        k.reverse()
        l = l[:l1] + k + l[r + 1:]
    else:
        i = int(s[1])
        x = int(s[2])
        l[i - 1] = x
