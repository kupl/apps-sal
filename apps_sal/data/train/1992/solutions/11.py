class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.input_string = characters
        self.queue = []
        self.combinationLength = combinationLength
        self.generate(0, '')

    def generate(self, start_index, acc_string):
        if len(acc_string) == self.combinationLength:
            self.queue.append(acc_string)
            return
        for i in range(start_index, len(self.input_string)):
            self.generate(i + 1, acc_string + self.input_string[i])

    def __next__(self) -> str:
        return self.queue.pop(0)

    def hasNext(self) -> bool:
        return len(self.queue) != 0
