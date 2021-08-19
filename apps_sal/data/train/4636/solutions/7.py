def tv_remote(words: str):

    class Mode:
        LOWERCASE, UPPERCASE, SYMBOLIC = range(3)
        mode = LOWERCASE

        def islowercase(self):
            return self.mode == self.LOWERCASE

        def isuppercase(self):
            return self.mode == self.UPPERCASE

        def isalphanumeric(self):
            return self.mode in [self.LOWERCASE, self.UPPERCASE]

        def issymbolic(self):
            return self.mode == self.SYMBOLIC

        def switch_to_new_mode(self, other):
            if isinstance(other, int):
                button_presses = (other - self.mode) % 3
                self.mode = other
                return button_presses

    def dist(pos1, pos2):
        return sum(min(abs(p1 - p2), dim - abs(p1 - p2)) for p1, p2, dim in zip(pos1, pos2, kb_dims))

    screen_keyboard_alphanumeric = "abcde123fghij456klmno789pqrst.@0uvwxyz_/⇑ "
    symbols_map_alphanumeric = {c: (i // 8, i % 8) for i, c in enumerate(screen_keyboard_alphanumeric)}
    kb_dims = (len(screen_keyboard_alphanumeric) // 8 + 1, 8)
    screen_keyboard_symbolic = "^~?!\'\"()-:;+&%*=<>€£$¥¤\[]{},.@§#¿¡ΦΨΩ_/⇑ "
    symbols_map_symbolic = {c: (i // 8, i % 8) for i, c in enumerate(screen_keyboard_symbolic)}
    common_symbols = "".join(set(screen_keyboard_alphanumeric) & set(screen_keyboard_symbolic))

    button_presses = 0
    cur_position, next_position = (0, 0), (0, 0)
    mode = Mode()

    words_to_type = []
    for ch in words:
        if ch in common_symbols:
            words_to_type.append(ch.lower())

        elif ch in screen_keyboard_symbolic:
            words_to_type.append("⇑" * mode.switch_to_new_mode(Mode.SYMBOLIC) + ch)

        elif ch.lower() in screen_keyboard_alphanumeric:
            if ch.isalpha():
                if ch.islower():
                    words_to_type.append("⇑" * mode.switch_to_new_mode(mode.LOWERCASE) + ch.lower())
                elif ch.isupper():
                    words_to_type.append("⇑" * mode.switch_to_new_mode(mode.UPPERCASE) + ch.lower())
            elif not mode.isalphanumeric():
                words_to_type.append("⇑" * mode.switch_to_new_mode(mode.LOWERCASE) + ch)
            else:
                words_to_type.append(ch)        # mode.isalphanumeric() and not ch.isalpha()

    words_to_type = "".join(words_to_type)

    for ch in words_to_type:
        if ch in screen_keyboard_alphanumeric:
            next_position = symbols_map_alphanumeric[ch]
            button_presses += 1 + dist(cur_position, next_position)
            cur_position = next_position

        elif ch in screen_keyboard_symbolic:
            next_position = symbols_map_symbolic[ch]
            button_presses += 1 + dist(cur_position, next_position)
            cur_position = next_position

        else:
            return -1

    return button_presses
