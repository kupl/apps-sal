# cook your dish here
def replace_if_possible(i):
    nonlocal string
    if (string[i] != '?' and string[i] != 'C') or \
        (string[i + 1] != '?' and string[i + 1] != 'H') or \
        (string[i + 2] != '?' and string[i + 2] != 'E') or \
            (string[i + 3] != '?' and string[i + 3] != 'F'):
        return

    string[i:i + 4] = 'CHEF'


t = int(input())
for _ in range(t):
    string = list(input())

    i = len(string) - 4
    while i >= 0:
        replace_if_possible(i)
        i -= 1

    for i in range(len(string)):
        if string[i] == '?':
            string[i] = 'A'

    print("".join(string))
