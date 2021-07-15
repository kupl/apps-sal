import sys

t = int(sys.stdin.readline())

for test in range(t):
    n = int(sys.stdin.readline())
    lines = [sys.stdin.readline().strip() for i in range(n)]
    turns = [x.split()[0] for x in lines][1:][::-1]
    turns = ['Right' if t == 'Left' else 'Left' for t in turns]
    turns = ['Begin'] + turns
    lines = lines[::-1]
    for i in range(n):
        print(turns[i], ' '.join(lines[i].split()[1:]))
        
    print()

        

