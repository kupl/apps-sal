# cook your dish here
test_cases = int(input())


for t in range(test_cases):
    password = input()
    r = ''
    for i in range(len(password)):
        r = r + str(int(password[i]) - 2)

    print(r)
