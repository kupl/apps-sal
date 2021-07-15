TABLE  = str.maketrans('rwx-','1110')
FIELDS = 'user group other'.split()

def chmod_calculator(perm):
    return ''.join( str(int( perm.get(p,'---').translate(TABLE), 2 )) for p in FIELDS )
