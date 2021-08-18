a, b = list(map(int, input().split()))
sample_dict = {}
for i in range(a):
    x = input().strip().split()
    sample_dict[x[0]] = x[1]
for i in range(b):
    x = input().strip()
    if len(x.split('.')) == 1:
        print('unknown')
    elif x.split('.')[-1] in list(sample_dict.keys()):
        print(sample_dict[x.split('.')[-1]])
    else:
        print('unknown')
