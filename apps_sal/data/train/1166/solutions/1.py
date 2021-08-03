# cook your dish here
n = int(input())
arr = [int(i) for i in input().split()]
q = int(input())
for _ in range(q):
    val = int(input())
    if val not in arr:
        print(0)
    else:
        count = 0
        for i in range(1, n + 1):
            for j in range(n - i + 1):
                if min(arr[j:j + i]) == val:
                    count += 1

        print(count)
