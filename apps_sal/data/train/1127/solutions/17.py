T = int(input())
for _ in range(T):
    name = list(map(str, input().split()))
    proper_name = ''
    for i in range(len(name) - 1):
        proper_name = proper_name + name[i][0].upper() + '. '
    proper_name = proper_name + name[-1][0].upper() + name[-1][1:].lower()
    print(proper_name)
