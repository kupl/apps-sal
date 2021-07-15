def tower_of_hanoi(rings):
    def hanoi(n):
        if n==1:
            return 1
        else:
            return 2*hanoi(n-1)+1
    return hanoi(rings)
    #your code here

