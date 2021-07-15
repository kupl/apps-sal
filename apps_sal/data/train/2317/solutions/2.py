for _ in range(int(input())):
    n = int(input())
    l1 = list(map(int, input().split()))
    answer = 0
    max_so_far = l1[0]
    for i in range(1, n):
        if l1[i] >= max_so_far:
            max_so_far = l1[i]
        else:
            answer = max(answer, (max_so_far - l1[i]).bit_length())
        
        
    print(answer)
