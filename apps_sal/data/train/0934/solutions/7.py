testcases = int(input())
while testcases > 0:
    array_length = list(map(int, input().split()))
    array1 = list(map(int, input().split()))
    array2 = list(map(int, input().split()))
    array3 = list(map(int, input().split()))
    sum = 0
    for i in range(array_length[0]):
        for j in range(array_length[1]):
            for k in range(array_length[2]):
                if array1[i] <= array2[j] and array2[j] >= array3[k]:
                    sum = (sum + (((array1[i] + array2[j]) % 1000000007) * ((array2[j] + array3[k]) % 1000000007))) % 1000000007
    testcases -= 1
    print(sum % 1000000007)
