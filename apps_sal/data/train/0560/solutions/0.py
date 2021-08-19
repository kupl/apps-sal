# cook your dish here
for i in range(int(input())):
    N = int(input())
    ALICE = list(map(int, input().split()))
    BOB = list(map(int, input().split()))
    ALICE[ALICE.index(max(ALICE))] = 0
    BOB[BOB.index(max(BOB))] = 0
    if sum(ALICE) < sum(BOB):
        print("Alice")
    elif sum(BOB) < sum(ALICE):
        print("Bob")
    else:
        print("Draw")
