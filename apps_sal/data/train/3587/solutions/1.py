from collections import Counter, defaultdict

NUMBERS = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
VALUES = {num: str(i) for i, num in enumerate(NUMBERS)}
counts = Counter(''.join(NUMBERS))

wordsContainningLetter = defaultdict(set)
for n in NUMBERS:
    for c in n:
        wordsContainningLetter[c].add(n)

EXECUTIONS_ORDER, founds = [], set()
while counts:
    for c, v in counts.copy().items():
        if v == 1:
            try:
                word = (wordsContainningLetter[c] - founds).pop()
            except KeyError:
                break
            wordCount = Counter(word)
            founds.add(word)
            EXECUTIONS_ORDER.append((c, wordCount, VALUES[word]))
            counts -= wordCount


def original_number(s):
    ans, count, executions = [], Counter(s), iter(EXECUTIONS_ORDER)
    while count:
        c, wordCount, value = next(executions)
        ans.extend([value] * count[c])
        for _ in range(count[c]):
            count -= wordCount
    return ''.join(sorted(ans))
