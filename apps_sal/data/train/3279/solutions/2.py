def sursurungal(txt):
    sursurungal.pluralize, dual, paucal, plural = False, 'bu{}'.format, '{}zo'.format, 'ga{}ga'.format

    def process_word(word):
        if sursurungal.pluralize != False:
            out = None
            if sursurungal.pluralize <= 1:
                out = word
            else:  # <-- Look at that curve!
                base = word
                if word[-1] == 's':
                    base = word[0:-1]
                if sursurungal.pluralize == 2:
                    out = dual(base)
                elif sursurungal.pluralize <= 9:
                    out = paucal(base)
                else:
                    out = plural(base)
            sursurungal.pluralize = False
            return out
        if word.isdigit():
            sursurungal.pluralize = int(word)
        return word
    return '\n'.join(' '.join(process_word(w) for w in l.split(' ')) for l in txt.split('\n'))
