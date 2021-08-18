def alice_bob(alice, bob):
    alice.remove(max(alice))
    bob.remove(max(bob))
    result_alice = 0
    result_bob = 0
    result_alice += sum(alice)
    result_bob += sum(bob)
    if result_alice > result_bob:
        return 'Bob'
    elif result_alice < result_bob:
        return 'Alice'
    elif result_bob == result_alice:
        return 'Draw'


T = int(input())
for i in range(T):
    N = int(input())
    alice = list(map(int, input().split()))
    bob = list(map(int, input().split()))
    print(alice_bob(alice, bob))
