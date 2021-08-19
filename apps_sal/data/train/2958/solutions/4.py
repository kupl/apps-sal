# This was a really fun kata!
# I merely guessed the pattern.
# I reasoned out answers between (1,1,1) and (2,2,2),
# interpolated some educated guesses between the test cases,
# and noticed (if my guesses were right):
# (n, n, n) -> nth triangular number cubed (n*(n+1)/2) ** 3
#
# I struggled for a while to figure out
# what's going on when x and y and z aren't all the same ?
#
# And then I thought, could it be this simple?
# The xth cubic number times the yth cubic number times the zth cubic number?
#
# And I ran the sample tests and the answer was yeah lol

# But I failed on my first solution attempt
# Because I forgot to use integer division instead of float division ;(

def subcuboids(x, y, z):
    return (x * (x + 1) // 2) * (y * (y + 1) // 2) * (z * (z + 1) // 2)
