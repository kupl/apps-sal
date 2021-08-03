# cook your dish here
lst = {2: 3, 3: 3, 4: 3, 5: 3, 6: 3, 7: 4, 8: 3, 9: 4}

for _ in range(int(input())):
    val = list(map(int, input().strip()))
    count = 1
    for i in val:
        count *= lst[int(i)]
    if count != 1:
        print(count % 1000000007)
    else:
        print(0)
