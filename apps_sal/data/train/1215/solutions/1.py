import collections
import functools
import sys
input = sys.stdin.readline
(inp, ip) = (lambda: int(input()), lambda: [int(w) for w in input().split()])


def isSolvable(words, result):

    @functools.lru_cache(None)
    def helper(i, total, nums):
        if i == len(chars):
            return total == 0
        if i - 1 in checkpoints:
            t = str(abs(total))[::-1]
            for j in checkpoints[i - 1]:
                if j < len(t) and t[j] != '0':
                    return False
        for j in range(len(nums)):
            if nums[j] == 0 and chars[i] not in not_zero and helper(i + 1, total, nums[:j] + nums[j + 1:]):
                return True
            elif nums[j] != 0 and helper(i + 1, total + nums[j] * mult[chars[i]], nums[:j] + nums[j + 1:]):
                return True
        return False
    longest_word = len(max(words, key=len))
    if len(result) < longest_word or len(result) > longest_word + 1:
        return False
    if result in words:
        return len(words) < 3 and all((word == result or len(word) == 1 for word in words))
    not_zero = set((word[0] for word in words if len(word) > 1))
    if len(result) > 1:
        not_zero.add(result[0])
    chars = set(result + ''.join(words))
    mult = {char: 0 for char in chars}
    groups = collections.defaultdict(set)
    for word in words:
        for (i, char) in enumerate(reversed(word)):
            mult[char] += 10 ** i
            groups[i].add(char)
    for (i, char) in enumerate(reversed(result)):
        mult[char] -= 10 ** i
        groups[i].add(char)
    chars = {char for char in chars if mult[char]}
    for g in groups:
        groups[g] = groups[g].intersection(chars)
    chars = list(chars)
    for g in range(1, len(groups)):
        groups[g] |= groups[g - 1]
    chars.sort(key=lambda c: min((g for g in range(len(groups)) if c in groups[g])))
    checkpoints = collections.defaultdict(list)
    seen = set()
    checked = set()
    for (i, char) in enumerate(chars):
        seen.add(char)
        for g in groups:
            if g not in checked and groups[g].issubset(seen):
                checked.add(g)
                checkpoints[i].append(g)
    return helper(0, 0, tuple(range(10)))


n = inp()
x = [input().strip() for i in range(n)]
y = input().strip()
ans = isSolvable(x, y)
if ans:
    print('true')
else:
    print('false')
