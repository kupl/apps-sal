def button_sequences(seqR, seqB):
    seq = ''
    leds = ['R', 'B']
    action = [None, None]
    for r, b in zip(seqR, seqB):
        r = int(r)
        b = int(b)
        for ind, button in enumerate([r, b]):
            if button and not action[ind]:
                action[ind] = 'press'
            elif button and action[ind]:
                action[ind] = 'held'
            elif action[ind] and not button:
                action[ind] = 'release'
        for ind in [0, 1]:
            if (action[ind] == 'press') and (action[ind - 1] != 'held'):
                seq += leds[ind]
                break
            elif (action[ind] == 'held') and (action[ind - 1] == 'release'):
                if seq[-1] == leds[ind]:
                    continue
                seq += leds[ind]
                break

        if action[0] == 'release':
            action[0] = None
        if action[1] == 'release':
            action[1] = None
    return seq
