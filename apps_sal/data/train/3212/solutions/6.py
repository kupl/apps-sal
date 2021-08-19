def generate_hashtag(_):
    return (lambda __: _ > '' < _ == _[:140] and chr(35) + __)(_.title().replace(chr(32), ''))
