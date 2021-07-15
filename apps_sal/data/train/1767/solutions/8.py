from collections import Counter

def is_valid(hand):
    if any(hand.count(str(i)) > 4 for i in range(1, 10)):
        return False
    stack = [[Counter(int(h) for h in hand), True, len(hand)]]
    while stack:
        status, has_pair, r = stack.pop()
        if r == 0:
            return True
        else:
            x = min(k for k, v in status.items() if v > 0)
            if status[x] >= 3:
                stack.append([(status - Counter([x, x, x])), has_pair, r - 3])
            if status[x+1] >= 1 and status[x+2] >= 1:
                stack.append([(status - Counter([x, x + 1, x + 2])), has_pair, r - 3])
            if has_pair and status[x] >= 2:
                stack.append([(status - Counter([x, x])), False, r - 2])
    return False

def solution(tiles):
    return ''.join(n for n in '123456789' if is_valid(tiles + n))
