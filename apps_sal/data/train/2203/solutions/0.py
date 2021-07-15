def main():
    n = int(input())
    a = [[int(i) for i in input().split()] for j in range(n)]
    
    result = [-1] * n
    for i in range(n - 1):
        for j in range(n):
            d = set(a[j][k] for k in range(n) if result[k] == -1 and j != k)
            if len(d) == 1:
                result[j] = d.pop()
    result[result.index(-1)] = n
    
    print(' '.join(str(i) for i in result))
    
main()
