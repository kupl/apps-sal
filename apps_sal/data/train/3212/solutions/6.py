generate_hashtag = lambda _: (lambda __: _ > '' < _ == _[:0b10001100] and chr(35) + __)(_.title().replace(chr(32),''))

