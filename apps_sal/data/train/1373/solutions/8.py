n = int(input())
for i in range(n):
    a, b = [int(i) for i in input().split()]
    l = [int(i) for i in input().split()]
    start = 0
    end = 0
    d = []
    answer = []
    for j in range(0, len(l)):
        d.append(l[j])
        end = end + 1
        if(len(set(d)) < b):
            pass
        else:
            end = end - 1
            start = end
            while(len(set(d)) >= b):
                d.pop(0)
        answer.append(len(d))
    print(max(answer))
