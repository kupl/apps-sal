def HQ9(code):
    nums = list(map(str, range(99, 0, -1))) + ['no more', '99']
    bofb = lambda x, w=True: f"{x} bottle{'s' * (x != '1')} of beer{' on the wall' * w}"
    take, store = 'Take one down and pass it around', 'Go to the store and buy some more'
    phrases = [(f"{take if x != '99' else store}, {bofb(x)}.", f"{bofb(x).capitalize()}, {bofb(x, 0)}.") for x in nums]
    lyrics = '\n'.join(f"{x[1]}\n{y[0]}" for x, y in zip(phrases, phrases[1:]))
    return {'H': 'Hello World!', 'Q': 'Q', '9': lyrics}.get(code, None)
