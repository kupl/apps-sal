def replace_exclamation(s):

    def e(_):
        return '!' if _ in 'aeiouAEIOU' else _
    return ''.join([e(x) for x in s])
