# I like to think of this in terms of math but it's been a while
# since number theory and modular arithmatic. Looking at this, we
# get the serries 1, 5, 13, 25, 41,... as we're starting at 0,
# it's actually 0, 4, 12, 24, 40, ... So this is 4*sum of the first
# n-1 numbers which gives us the formula of the nth number (starting
# with 0) is 2n(n+1).

# So the the nth character in the center is 2n(n+1) % len(chars).
# But this is an infinite serries so I need to know when to stop.
# If n is odd, then the pattern repeats every n (only half + 1 letters)
# If n is even, then the pattern repeats ever n/2 generally (sometimes shorter).

# Need to check the final product to make sure that there is no repeat
# in there as the exceptions in the evens and the characters may not be unique.
def center_of(chars):
    center = ""
    n = len(chars)
    if n == 0:
        return center
    elif n % 2 == 0:
        n //= 2
    # get the list of character positions
    pos = []
    for i in range(n):
        pos.append(2 * i * (i + 1) % len(chars))
    # get the characters in the center
    for num in pos:
        center += chars[num]
    # test if there's are repeat in the center
    for i in range(len(center) // 2):
        test = center[:i + 1]
        if center == test * (len(center) // len(test)):
            center = test
            break
    return center
