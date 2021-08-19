import math


class PlayingCards:

    def encode(self, message):
        list_char = list(' ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        list_card_val = list('A23456789TJQK')
        list_card_col = list('CDHS')
        list_card0 = [val + col for col in list_card_col for val in list_card_val]
        for c in message:
            if c not in list_char:
                return None
        sort_list_message = list(message)
        sort_list_message.sort()
        n = 0
        list_ind = []
        for (ii, c) in enumerate(message):
            ind = list_char.index(c)
            n += ind * 27 ** (len(message) - 1 - ii)
        if n >= math.factorial(52):
            return None
        dec = []
        n2 = n
        for ii in range(51, 0, -1):
            (n_i, n2) = (n2 // math.factorial(ii), n2 % math.factorial(ii))
            dec.append(n_i)
        dec.append(0)
        list_card = list_card0.copy()
        deck_code = []
        for ii in dec:
            deck_code.append(list_card[ii])
            list_card.remove(list_card[ii])
        return deck_code

    def decode(self, deck):
        list_char = list(' ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        list_card_val = list('A23456789TJQK')
        list_card_col = list('CDHS')
        list_card0 = [val + col for col in list_card_col for val in list_card_val]
        test_deck = list(set(deck))
        test_deck.sort()
        test_list_card0 = list_card0.copy()
        test_list_card0.sort()
        if test_deck != test_list_card0:
            return None
        list_card = list_card0.copy()
        n = 0
        for (ii, c) in enumerate(deck[:-1]):
            ind = list_card.index(c)
            if ind > 0:
                n += ind * math.factorial(len(deck) - 1 - ii)
            list_card.remove(c)
        n2 = n
        if n == 0:
            return ''
        dec = []
        nchar = math.floor(math.log10(n) / math.log10(27))
        for ii in range(nchar, 0, -1):
            (n_i, n2) = (n2 // 27 ** ii, n2 % 27 ** ii)
            dec.append(n_i)
        dec.append(n2)
        message = ''.join([list_char[ii] for ii in dec])
        return message
