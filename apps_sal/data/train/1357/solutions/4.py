for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    total = 0

    for i in arr:
        if i == 5:  total += i
        else:
            if total == 0:
                print("NO")
                break
            else:
                to_return = i - 5
                if total < to_return:
                    print("NO")
                    break
                else:
                    total -= 5
    else:
        print("YES")
