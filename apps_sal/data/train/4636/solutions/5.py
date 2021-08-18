KEYPADS = (
    (
        'a', 'b', 'c', 'd', 'e', '1', '2', '3',
        'f', 'g', 'h', 'i', 'j', '4', '5', '6',
        'k', 'l', 'm', 'n', 'o', '7', '8', '9',
        'p', 'q', 'r', 's', 't', '.', '@', '0',
        'u', 'v', 'w', 'x', 'y', 'z', '_', '/', 'aA
    ),
    (
        'A', 'B', 'C', 'D', 'E', '1', '2', '3',
        'F', 'G', 'H', 'I', 'J', '4', '5', '6',
        'K', 'L', 'M', 'N', 'O', '7', '8', '9',
        'P', 'Q', 'R', 'S', 'T', '.', '@', '0',
        'U', 'V', 'W', 'X', 'Y', 'Z', '_', '/', 'aA
    ),
    (
        '^', '~', '?', '!', '\'', '"', '(', ')',
        '-', ':', ';', '+', '&', '%', '*', '=',
        '<', '>', '€', '£', '$', '¥', '¤', '\\',
        '[', ']', '{', '}', ',', '.', '@', '§', '
        'aA
    )
)


class Tv:
    def __init__(self, words):
        self.words = words
        self.OK = 1
        self.MAX_H = 7
        self.MAX_V = 5
        self.count = 0
        self.keypad_pos = 0
        self.current_pos = (0, 0)
        self.CHANGE_KEY_IDX = 40

    def count_best_path(self, index: int):

        temp_pos = ((index // 8), (index % 8))

        result = []

        for current_val, temp_val, max_l in zip(self.current_pos, temp_pos, [self.MAX_V, self.MAX_H]):
            v_1 = current_val
            v_2 = current_val
            count = 0

            while v_1 != temp_val and v_2 != temp_val:
                v_1 -= 1
                v_2 += 1
                if v_1 < 0:
                    v_1 = max_l
                if v_2 > max_l:
                    v_2 = 0
                count += 1

            result.append(count)

        self.current_pos = temp_pos

        self.count += sum(result) + self.OK

    def count_total_moves(self):
        for letter in self.words:

            letter = 'SP' if letter == ' ' else letter
            while letter not in KEYPADS[self.keypad_pos]:
                self.count_best_path(self.CHANGE_KEY_IDX)
                if self.keypad_pos < 2:
                    self.keypad_pos += 1
                else:
                    self.keypad_pos = 0

            index = KEYPADS[self.keypad_pos].index(letter)
            self.count_best_path(index)
        return self.count


def tv_remote(words):
    return Tv(words).count_total_moves()


print(tv_remote('ciao'))
