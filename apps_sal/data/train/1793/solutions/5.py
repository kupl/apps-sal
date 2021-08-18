import itertools as it
import math
import string


class PlayingCards:

    def __init__(self):
        self.cards = ['AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', 'TC', 'JC', 'QC', 'KC', 'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', 'TD', 'JD', 'QD', 'KD', 'AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', 'TH', 'JH', 'QH', 'KH', 'AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', 'TS', 'JS', 'QS', 'KS']
        self.alphabet = [' '] + [letter for letter in string.ascii_uppercase]

    def message_to_cypher_value(self, clear_string):
        alphabet_size = len(self.alphabet)
        output = 0
        for letter in clear_string:
            output = output * alphabet_size + self.alphabet.index(letter)
        return output

    def encode(self, message):
        for letter in message:
            if letter not in self.alphabet:
                return None
        remaining_cards = list(self.cards)
        n = self.message_to_cypher_value(message)
        if n > math.factorial(52) - 1:
            return None
        output = []
        while remaining_cards:
            permutations_per_card = math.factorial(len(remaining_cards)) // len(remaining_cards)
            current_index = n // permutations_per_card
            output.append(remaining_cards.pop(current_index))
            n -= current_index * permutations_per_card
        return output

    def deck_to_cypher_value(self, deck):
        remaining_cards = list(self.cards)
        output = 0
        for card in deck:
            permutations_per_card = math.factorial(len(remaining_cards)) // len(remaining_cards)
            current_index = remaining_cards.index(card)
            output += current_index * permutations_per_card
            remaining_cards.pop(current_index)
        return output

    def decode(self, deck):
        printDeck(deck, False)
        if len(deck) > len(self.cards):
            return None
        if len(set(deck)) < len(self.cards):
            return None
        for card in deck:
            if not card in self.cards:
                return None
        n = self.deck_to_cypher_value(deck)
        alphabet_size = len(self.alphabet)
        output = []
        while n > 0:
            output.append(n % alphabet_size)
            n = (n - output[-1]) // alphabet_size
        return ''.join([self.alphabet[x] for x in output[::-1]])
