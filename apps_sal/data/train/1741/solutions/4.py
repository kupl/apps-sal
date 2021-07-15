# https://www.codeleading.com/article/49772209610/
arr=[0, 8, 95, 1183, 14824]

for i in range(0, 10**5): 
    arr.append((15 * arr[-1] - 32 * arr[-2] + 15 * arr[-3] - arr[-4]) % 12345787)

def five_by_2n(n): 
    return arr[n]
