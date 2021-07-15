def even_numbers(arr,n):
    A = []
    while len(A) < n and arr:
        temp = arr.pop()
        if temp % 2 == 0:
            A = [temp] + A    
    return A

