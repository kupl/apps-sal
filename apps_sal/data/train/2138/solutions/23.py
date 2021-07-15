alice = input()
bob = input()

a = alice.count('1') 
b = bob.count('1')
a += (a%2) # if it is odd, then add another one.

print("YES" if a >= b else "NO")


