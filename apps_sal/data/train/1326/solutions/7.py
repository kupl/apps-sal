# cook your dish here
for i in range(int(input())):
    n = input()
    fuel = list(map(int, input().split()))
    sum = fuel[0]
    count = 0
    for j in range(1, len(fuel)):
        if sum == 0:
            break
        else:
            sum = (sum - 1) + fuel[j]
            count += 1
    print(count + sum)
    fuel.clear()
