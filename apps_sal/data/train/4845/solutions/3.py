def sort_nested_list(A):
    numbers = []
    def peel(A, insert=False):
        for i in range(len(A)):
            if len(A[i]) != 0 and isinstance(A[i][0], list):
                A[i] = peel(A[i], insert)
            else:
                if insert:
                    A[i] = numbers[:len(A[i])]
                    del numbers[:len(A[i])]
                else:
                    numbers.extend(A[i])
        return A
    peel(A)
    numbers = sorted(numbers)
    return peel(A, insert=True)
