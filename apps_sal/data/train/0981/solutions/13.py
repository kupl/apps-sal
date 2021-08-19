test_cases = int(input())
for i in range(test_cases):
    no = int(input())
    skill = input().split()
    for j in range(no):
        skill[j] = int(skill[j])
    skill.sort()
    min = skill[no - 1]
    for j in range(no - 1):
        if skill[j + 1] - skill[j] < min:
            min = skill[j + 1] - skill[j]
    print(min)
