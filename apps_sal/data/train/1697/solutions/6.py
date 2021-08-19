from functools import reduce
from typing import Tuple, List, Optional, Sequence


class Box:

    def __init__(self, x: int, y: int, value: Optional[int]):
        self.value = value
        self.x = x
        self.y = y

    def to_int(self):
        return self.value if self.value else 0

    def mapper(self) -> str:
        if self.value is None:
            return 'S'
        elif self.value == 0:
            return '#'
        else:
            return '█'


class Clue:

    def __init__(self, index: int, clue: Sequence[int], elements: List[Box]):
        self.index: int = index
        self.clue: Sequence[int] = clue
        self.elements: List[Box] = elements

    @staticmethod
    def match_constrains(initial: Sequence[int], constrains: List[Box]):

        def tmp(element: int, constrain: Box):
            if constrain.value is None:
                return True
            return constrain.value == element
        ddd = all((tmp(data, req) for (data, req) in zip(initial, constrains)))
        return ddd

    def generate_combinations(self, initial: Sequence[int] = (), to_be_marked: int = -1) -> List[Sequence[int]]:
        if to_be_marked == -1:
            to_be_marked = sum(self.clue)
        if not Clue.match_constrains(initial, self.elements):
            return []
        elif len(initial) > len(self.elements):
            return []
        elif len(initial) == len(self.elements):
            arr = [it for it in initial if it == 1]
            if to_be_marked != len(arr):
                return []
            return [initial]
        elif len(self.clue) == 0:
            ret: List[int] = [i for i in initial]
            for i in range(0, len(self.elements) - len(initial)):
                ret.append(0)
            if Clue.match_constrains(ret, self.elements):
                return [ret]
            return []
        new_initial: List[int] = [i for i in initial]
        new_initial.append(0)
        zero: List[Sequence[int]] = self.generate_combinations(new_initial, to_be_marked)
        if self.clue:
            new_clue: Clue = Clue(self.index, self.clue[1:], self.elements)
            tab: List[int] = [i for i in initial]
            tab.extend([1 for __ in range(0, self.clue[0])])
            if len(tab) < len(self.elements):
                tab.append(0)
            one = new_clue.generate_combinations(tab, to_be_marked)
            zero.extend(one)
        return zero

    @staticmethod
    def get_marked_size(clue: Sequence[int]):
        return reduce(lambda x, y: x + y, clue, 0)

    @staticmethod
    def get_minimal_size(clue: Sequence[int]):
        return len(clue) + Clue.get_marked_size(clue) - 1

    def contains_all(self, stripe):
        return len([1 for element in stripe if element == 1]) == self.get_marked_size(self.clue)

    @staticmethod
    def get_commons(possible_solutions):

        def check_all_the_same(lst):
            if lst.count(lst[0]) == len(lst):
                return lst[0]
            return None
        return [check_all_the_same(lst) for lst in zip(*possible_solutions)]


def get_v_stripe(board, index):
    return [element[index] for element in board]


def get_h_stripe(board, index):
    return board[index]


class Nonogram:

    def __init__(self, clues: Tuple[Sequence[Sequence[int]], Sequence[Sequence[int]]]):
        (h_clues, v_clues) = clues
        self.width: int = len(h_clues)
        self.height: int = len(v_clues)
        self.board: List[List[Box]] = [[Box(x, y, None) for y in range(0, self.width)] for x in range(0, self.height)]
        self.v_clues = [Clue(index, clue, [line[index] for line in self.board]) for (index, clue) in enumerate(clues[0])]
        self.h_clues = [Clue(index, clue, self.board[index]) for (index, clue) in enumerate(clues[1])]

    def solve(self) -> List[List[int]]:
        missing = [(self.width - clue.get_minimal_size(clue.clue), clue) for clue in self.v_clues]
        missing.sort(key=lambda x: x[0])
        for i in range(0, 10):
            self.print_board()
            print(('loop ', i))
            for clue in self.v_clues:
                comb = clue.generate_combinations()
                print('v: %s : %s ' % (clue.clue, Clue.get_commons(comb)))
                for (index, value) in enumerate(Clue.get_commons(comb)):
                    if value is not None:
                        self.board[index][clue.index].value = value
            for clue in self.h_clues:
                comb = clue.generate_combinations()
                print('h: %s : %s ' % (clue.clue, Clue.get_commons(comb)))
                for (index, value) in enumerate(Clue.get_commons(comb)):
                    if value is not None:
                        self.board[clue.index][index].value = value
        self.print_board()
        return tuple([tuple([box.to_int() for box in line]) for line in self.board])

    def print_board(self) -> None:
        max_size: int = max((len(clue.clue) for clue in self.v_clues))
        max_width: int = max((len(clue.clue) for clue in self.h_clues))
        prefix: str = ' ' * (2 * max_width + 3)

        def expand_empty_header(clues: Sequence[int], size: int, ending: str) -> List[str]:
            empty_header = [' ' for __ in range(0, size)]
            empty_header.extend(list(map(str, clues)))
            empty_header.append(ending)
            return empty_header
        headers = [expand_empty_header(clue.clue, max_size, '-')[-max_size - 1:] for clue in self.v_clues]
        for index in range(0, max_size):
            print(prefix + ' '.join([str(e[index]) for e in headers]))
        borders = [expand_empty_header(clue.clue, max_width, '|')[-max_size - 1:] for clue in self.h_clues]
        for (border, line) in zip(borders, self.board):
            d = ' '.join([str(d) for d in border]) + ' '.join([d.mapper() for d in line])
            print(d)


def solve(clues, width: int, height: int) -> List[List[int]]:
    """
    :param height:
    :type width: object
    """
    return Nonogram(clues).solve()
