def HQ9(code):

    def BB():
        s = ''
        for i in range(99, 0, -1):
            s1 = ' of beer on the wall, {0}'.format(i)
            s2 = ' bottles'
            s3 = ' bottle'
            s4 = ' of beer.\nTake one down and pass it around, '
            s5 = str(i - 1) if i > 1 else 'no more'
            s6 = ' of beer on the wall.\n'
            s += str(i)
            if i > 2:
                s += s2 + s1 + s2 + s4 + s5 + s2 + s6
            elif i == 2:
                s += s2 + s1 + s2 + s4 + s5 + s3 + s6
            elif i == 1:
                s += s3 + s1 + s3 + s4 + s5 + s2 + s6
                s += 'No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.'
        return s
    return 'Hello World!' if code == 'H' else code if code == 'Q' else BB() if code == '9' else None
