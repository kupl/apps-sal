from collections import defaultdict


def get_key_length(cipher_text, max_key_length):
    # Step 1: List of recurrent patterns of three signs
    d = defaultdict(list)
    for i in range(len(cipher_text) - 3):
        d[cipher_text[i:i + 3]].append(i)

    # Step 2: Compute distance between patterns
    e = defaultdict(int)
    for k, v in list(d.items()):
        for v0, v1 in zip(v, v[1:]):
            e[v1 - v0] += 1

    # Step 3: Test of divisibility
    lengths = []
    total = sum(e.values())
    for length in range(2, max_key_length):
        score = [0, 0]
        for k, n in list(e.items()):
            score[k % length == 0] += n
        # We put a threshold on 66% of completion
        lengths.append((score[True] / total > 0.66, length))

    return max(lengths)[1]
