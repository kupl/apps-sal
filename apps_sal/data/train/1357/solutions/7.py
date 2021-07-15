for _ in range(int(input())):
    n = int(input())
    nums = [int(j) for j in input().split()]
    yes, five, ten = 1, 0, 0
    for j in range(n):
        if nums[j] == 15:
            if ten > 0 and five > 0:
                ten -= 1
                five -= 1
            elif five > 1:
                five -= 2
            else:
                yes = 0
        elif nums[j] == 10:
            ten += 1
            if five > 0:
                five -= 1
            else:
                yes = 0
        else:
            five += 1
    if yes == 1:
        print("YES")
    else:
        print("NO")
