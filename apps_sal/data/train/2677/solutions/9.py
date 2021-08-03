def tv_remote(words: str):
    screen_keyboard_symbols = "abcde123fghij456klmno789pqrst.@0uvwxyz_/* "
    symbols_map = {c: (i // 8, i % 8) for i, c in enumerate(screen_keyboard_symbols)}
    kb_dims = (len(screen_keyboard_symbols) // 8 + 1, 8)

    def dist(pos1, pos2):
        return sum(min(abs(p1 - p2), dim - abs(p1 - p2)) for p1, p2, dim in zip(pos1, pos2, kb_dims))

    button_presses = 0
    cur_position, next_position = (0, 0), (0, 0)
    caps_on = False

    words_to_type = []
    for ch in words:
        if ch.islower() and caps_on or ch.isupper() and not caps_on:
            words_to_type.append("*" + ch.lower())
            caps_on = not caps_on
        else:
            words_to_type.append(ch.lower())
    words_to_type = "".join(words_to_type)

    for ch in words_to_type:
        if ch in screen_keyboard_symbols:
            next_position = symbols_map[ch]
            button_presses += 1 + dist(cur_position, next_position)
            cur_position = next_position
        else:
            return -1
    return button_presses
