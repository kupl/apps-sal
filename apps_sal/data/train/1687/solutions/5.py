def num_bits(number):
    binary = bin(number)
    setBits = [ones for ones in binary[2:] if ones == '1']
    return len(setBits)


T = int(input())
for i in range(T):
    N, K = input().split(' ')
    N = int(N)
    K = int(K)
    l = []
    if K == 3:
        l = [0, 1, 3, 0]
    elif K == 4:
        l = [0, 1, 3, 7, 0]
    elif K == 5:
        l = [0, 1, 2, 3, 5, 0]
    elif K == 6:
        l = [0, 1, 2, 3, 5, 7, 0]
    elif K == 7:
        l = [1, 2, 3, 5, 4, 7, 0, 1]
    else:
        l = [1, 2, 3, 5, 4, 7, 0, 6, 1]

    for i in range(K):
        print(l[i], l[i + 1])


'''
0,1,2,3,4,5,6,7
0: 0
1: 1,2,4,8
2: 3,5,6,9,10,12
3: 7,11,13,14
4: 15

K=3
0 1 3 5 4 2 6 7
0 1 3
K=4
0 1 3 7
K=5
0 1 3 7 2
K=6
0 1 3 7 2 5
K=7
0 1 3 7 2 5 
'''
