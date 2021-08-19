def hanoiArray(n):

    def move(n, source, target, auxiliary):
        if n > 0:
            # Move n - 1 disks from source to auxiliary, so they are out of the way
            move(n - 1, source, auxiliary, target)

            # Move the nth disk from source to target
            target.append(source.pop())

            # Store new state
            res.append([A[:], B[:], C[:]])

            # Move the n - 1 disks that we left on auxiliary onto target
            move(n - 1, auxiliary, target, source)

    A = list(range(n, 0, -1))
    B = []
    C = []

    res = [[A[:], B[:], C[:]]]

    # Initiate call from source A to target C with auxiliary B
    move(n, A, C, B)
    return '\n'.join(map(str, res))
