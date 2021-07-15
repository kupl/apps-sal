correct_polish_letters = lambda s: ''.join({'ą': 'a', 'ć': 'c', 'ę': 'e',
                                            'ł': 'l', 'ń': 'n', 'ó': 'o',
                                            'ś': 's', 'ź': 'z', 'ż': 'z'}.get(c, c) for c in s)
