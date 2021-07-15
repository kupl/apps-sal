FROM   = "abc def ghi jkl mno pqrs tuv wxyz".split()
TO_NUM = "222 333 444 555 666 7777 888 9999".split()

TABLE_TO_NUM  = str.maketrans( *map(''.join, (FROM, TO_NUM)) )
TABLE_TO_CHAR = str.maketrans( *map(lambda lst: ''.join(x[0] for x in lst), (TO_NUM, FROM)))


def T9(words, seq):
    return ( [w for w in words if seq == w.lower().translate(TABLE_TO_NUM)]
                or [seq.translate(TABLE_TO_CHAR)] )
