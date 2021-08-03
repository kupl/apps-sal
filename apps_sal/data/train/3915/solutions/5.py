def solve(input_string):
    answer = []
    for n in input_string.split('\n'):
        carry, carried = 0, 0
        A, B = map(str, n[::-1].split())
        for x in range(len(A)):
            carried += (int(A[x]) + int(B[x]))
            carry += carried > 9
            carried //= 10
        answer.append(carry)
    return '\n'.join("No carry operation" if not c else "%d carry operations" % c for c in answer)
