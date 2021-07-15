def f(n):
    sod = 0
    for char in str(n):
        sod += int(char)
    if n%sod == 0:
        return "Yes"
    else:
        return "No"

t = int(input())
answers = list()
for _ in range(t):
    n = int(input())
    answers.append(f(n))

for answer in answers:
    print(answer)
