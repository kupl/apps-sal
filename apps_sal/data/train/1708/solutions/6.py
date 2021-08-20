class MemoryManager:

    def __init__(self, memory):
        self.memory = [None] * len(memory)
        self.disk = memory

    def allocate(self, size):
        previous = 0
        for i in range(len(self.memory)):
            if self.memory[i] == None:
                previous += 1
            else:
                previous = 0
            if previous == size:
                start_index = i + 1 - size
                for x in range(start_index, i + 1):
                    self.memory[x] = start_index
                return start_index
        raise Exception('No space available')

    def release(self, pointer):
        if pointer not in self.memory:
            raise Exception('pointer not in memory')
        for i in range(len(self.memory)):
            if self.memory[i] == pointer:
                self.memory[i] = None

    def read(self, pointer):
        if self.memory[pointer] == None:
            raise Exception('No space alocated')
        return self.disk[pointer]

    def write(self, pointer, value):
        if self.memory[pointer] == None:
            raise Exception('No space alocated')
        self.disk[pointer] = value
