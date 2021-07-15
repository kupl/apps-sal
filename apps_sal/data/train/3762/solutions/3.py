from collections import deque

def pattern(n):
    A = deque([str(i+1) for i in range(n)])
    result = []
    for i in range(len(A)):
        print(A)
        result.append(''.join(A))
        A.rotate(-1)
    return '\n'.join(result)

