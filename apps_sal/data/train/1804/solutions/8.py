from collections import defaultdict


def recoverSecret(triplets):
    letters = defaultdict(set)
    for a, b, c in triplets:
        letters[a].add(b)
        letters[a].add(c)
        letters[b].add(c)

    for key, value in list(letters.items()):
        for after_key in value:
            letters[key] = letters[key].union(letters[after_key])

    return ''.join(k for k, _ in sorted(
        iter(letters.items()), key=lambda __v: len(__v[1]), reverse=True
    ))
