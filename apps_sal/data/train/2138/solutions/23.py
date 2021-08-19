alice = input()
bob = input()
a = alice.count('1')
b = bob.count('1')
a += a % 2
print('YES' if a >= b else 'NO')
