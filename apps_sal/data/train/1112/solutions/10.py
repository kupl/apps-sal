def f(n):
    line=n
    p=1
    
    while line>0:
        for i in range(line):
            print(p, end="")
            p += 1
        print()
        line -= 1
    


t = int(input())
answers = list()
for _ in range(t):
    n = int(input())
    answers.append(n)

for answer in answers:
    f(answer)
