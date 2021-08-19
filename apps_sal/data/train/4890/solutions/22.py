def find_difference(a, b):
    # Your code here!
    A = 1
    B = 1
    for i in range(len(a)):
        A = A * a[i]
        B = B * b[i]
    return A - B if(A > B) else B - A
