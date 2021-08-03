# code chef may2012  stones.py


t = int(input())
for t1 in range(t):
    j = input().strip()
    s = input().strip()
    answer = 0
    for c in s:
        if c in j:
            answer += 1
    print(answer)
