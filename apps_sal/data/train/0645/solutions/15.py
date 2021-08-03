# cook your dish here
T = int(input())
while(T):
    n = int(input())
    k = int(input())
    if k % n == 0:
        print(0)
    elif ((k % n) == (n - k % n)):
        print(2 * (k % n) - 1)
    elif ((k % n) > (n - k % n)):
        print(2 * (n - k % n))
    elif ((k % n) < (n - k % n)):
        print(2 * (k % n))
    T -= 1
