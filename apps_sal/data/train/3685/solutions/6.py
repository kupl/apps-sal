#  WHO  WORE  IT  BETTER  ??

' 1) LOOP CAT ? '
def read_out(array):  #  2 seconds
    acrostic = ''
    for word in array:
        acrostic += word[0]
    return acrostic

' 2) LIST COMP ? '
read_out = lambda a: ''.join(w[0] for w in a)  #  3.6 seconds

' 3) MAP OBJ ? '
read_out = lambda a: ''.join([w[0] for w in a])

#  YOU  DECIDE  !!

# VOTE: 1, 2, or 3

