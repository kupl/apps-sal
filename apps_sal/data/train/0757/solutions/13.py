t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    vowels = ['A', 'E', 'I', 'O', 'U']
    flag = 0
    if n == 1:
        print("No")
    else:
        for i in range(n):
            if s[i] in vowels and s[(i + 1) % n] in vowels:
                print("Yes")
                flag = 1
                break
        if flag == 0:
            print("No")
