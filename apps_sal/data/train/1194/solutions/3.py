from collections import Counter
for _ in range(int(input())):
    n = int(input())
    s = input()
    counter = Counter(s)
    print((2 * (max(counter['U'], counter['D']) - abs(counter['U'] - counter['D'])
                + max(counter['R'], counter['L']) - abs(counter['R'] - counter['L']))))
