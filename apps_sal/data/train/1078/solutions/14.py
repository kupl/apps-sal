for _ in range(int(input())):
    S, W1, W2, W3 = (int(i) for i in input().split(' '))
    if(W1 + W2 + W3 <= S):
        print(1)
    elif(S >= (W1 + W2) or S >= (W2 + W3)):
        print(2)
    else:
        print(3)
