'''
    leave a comment if you don't understand something :)
    thanks for choosing my code!! ~Srikar

'''

T = int(input())
mod = 1000000007
for _ in range(T):
    n, k = list(map(int, input().split()))
    if n == 0:
        k -= 1
        print((k * (k + 1)) % mod)
    else:
        if k == 1:
            print((n**2) % mod)

        else:
            if k % 2 == 0:
                a = k // 2  # even numbers
                b = a - 1  # odd numbers

                ans = ((n**2) % mod) + ((a * ((2 * n) % mod)) % mod) + ((b * (b + 1)) % mod)
            else:
                k -= 1
                a = k // 2  # even numbers
                b = a  # odd numbers

                ans = ((n**2) % mod) + ((a * ((2 * n) % mod)) % mod) + ((b * (b + 1)) % mod)

            print(ans % mod)
