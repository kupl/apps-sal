# cook your dish here
t = int(input())
for h in range(t):
    l = int(input())
    li = list(map(int, input().split()))
    li.insert(0, 0)
    status = True
    for i in range(1, len(li)):
        for j in range(1, len(li)):
            if i != j and li[i] != li[j]:
                if li[li[i]] == li[li[j]]:
                    print("Truly Happy")
                    status = False
                    break
        if not status:
            break
    if status:
        print("Poor Chef")
