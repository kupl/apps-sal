def every(array, ii=0, si=0):
    return array[si::] if ii == 0 else array[si::ii]
