from typing import Tuple


class Card:

    def __init__(self, name: str, begins_with: Tuple[int, ...], number_length: Tuple[int, ...]):
        self.name = name
        self.begins_with = list(map(str, begins_with))
        self.number_length = number_length

    def is_valid(self, number: str) -> bool:
        return any((number.startswith(b) for b in self.begins_with)) and len(number) in self.number_length


CARDS = (Card('AMEX', (34, 37), (15,)), Card('Discover', (6011,), (16,)), Card('Mastercard', (51, 52, 53, 54, 55), (16,)), Card('VISA', (4,), (13, 16)))


def get_issuer(number: int):
    n = str(number)
    return next((c.name for c in CARDS if c.is_valid(n)), 'Unknown')
