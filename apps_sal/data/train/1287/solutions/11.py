vowel = ['a', 'e', 'i', 'o', 'u']


def f(n):
    return 1 if n in vowel else 0


for _ in range(int(input())):
    a = input()
    num = ''
    for i in a:
        num += str(f(i))
    print(int(num, 2) % 1000000007)
