count = 0
for _ in range(int(input())):
    view = list(map(int, input().split()))
    if(sum(view) > 1):
        count += 1
print(count)
