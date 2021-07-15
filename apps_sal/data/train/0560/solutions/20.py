t = int(input())
for i in range(t):
 n = int(input())
 alice = list(map(int,input().split()))
 bob = list(map(int,input().split()))
 alice.remove(max(alice))
 bob.remove(max(bob))
 sum_alice = sum(alice)
 sum_bob = sum(bob)
 if sum_bob>sum_alice:
  print("Alice")
 elif sum_alice>sum_bob:
  print("Bob")
 else:
  print("Draw")
