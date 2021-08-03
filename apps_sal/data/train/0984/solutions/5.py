for _ in range(int(input())):
    n = int(input())
    nums = [int(j) for j in input().split()]
    odd, even, res = 0, 0, 0
    for j in range(n):
        if nums[j] % 2 == 0:
            even += 1
        else:
            odd += 1
            res += even
    print(res)
