def isCandidate(x, seq):
    count = 0
    left_pointer = 0
    right_pointer = len(seq) - 1

    while left_pointer < right_pointer:
        left = seq[left_pointer]
        right = seq[right_pointer]

        if left + right == x:
            count += 1
            if count == 2:
                return False

        if left + right > x:
            right_pointer -= 1
            left_pointer = 0
            continue

        left_pointer += 1

    return count == 1


def ulam_sequence(u0, u1, n):
    seq = [u0, u1]
    x = u0 + u1
    while len(seq) < n:
        if isCandidate(x, seq):
            seq.append(x)
        x += 1
    return seq
