test_cases = int(input())
for i in range(test_cases):
    string = input()
    a = string.find('W')
    x = a - 0
    y = len(string) - 1 - x
    if y == x:
        print('Chef')
    else:
        print('Aleksa')
