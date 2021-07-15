def HQ9(code):
    nums = list(map(str, range(99, 0, -1))) + ['no more', '99']
    bofb = lambda x, w=True: f"{x} bottle{'s' * (x != '1')} of beer{' on the wall' * w}"
    take, store = 'Take one down and pass it around', 'Go to the store and buy some more'
    poem = '\n'.join(f"{take if x != '99' else store}, {bofb(x)}.\n{bofb(x).capitalize()}, {bofb(x, 0)}." for x in nums)
    poem = '\n'.join(poem.split('\n')[1:-1])
    return {'H': 'Hello World!',
            'Q': 'Q',
            '9': poem}.get(code, None)
