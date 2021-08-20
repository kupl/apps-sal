t = int(input())
for _ in range(t):
    n = int(input())
    cards = list(map(int, input().split()))
    unique_cards = set(cards)
    if len(cards) - len(unique_cards) & 1:
        print(len(unique_cards) - 1)
    else:
        print(len(unique_cards))
