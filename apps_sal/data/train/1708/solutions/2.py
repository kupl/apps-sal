import copy


class MemoryManager:

    def __init__(self, memory: list):
        """
        @constructor Creates a new memory manager for the provided array.
        @param {memory} An array to use as the backing memory.
        """
        self.memory = memory
        self.Firstindex = copy.copy(memory)
        self.lens = len(self.Firstindex)

    def allocate(self, size):
        """
        Allocates a block of memory of requested size.
        @param {number} size - The size of the block to allocate.
        @returns {number} A pointer which is the index of the first location in the allocated block.
        @raises If it is not possible to allocate a block of the requested size.
        """
        if size > self.lens:
            raise Exception('allocate size ERROR')
        else:
            tempindex = self.Firstindex
            while tempindex:
                if tempindex.count(None) == 0:
                    break
                else:
                    index = self.Firstindex.index(None)
                if index + size > self.lens:
                    break
                else:
                    last = index + size
                if self.Firstindex[index:last] == [None] * size:
                    self.Firstindex[index:last] = [index] * size
                    return index
                else:
                    needlist = self.Firstindex[index:last]
                    s2 = list(filter(None, needlist))
                    tempindex = tempindex[tempindex.index(s2[-1]) + 1:]
            raise Exception('allocate END ERROR')

    def release(self, pointer: int):
        """
        Releases a previously allocated block of memory.
        @param {number} pointer - The pointer to the block to release.
        @raises If the pointer does not point to an allocated block.
        """
        if pointer not in self.Firstindex:
            raise Exception('pointer release ERROR')
        counts = self.Firstindex.count(pointer)
        first = self.Firstindex.index(pointer)
        last = first + counts
        self.memory[first:last] = [None] * counts
        self.Firstindex[first:last] = [None] * counts

    def read(self, pointer):
        """
        Reads the value at the location identified by pointer
        @param {number} pointer - The location to read.
        @returns {number} The value at that location.
        @raises If pointer is in unallocated memory.
        """
        if pointer >= self.lens:
            raise Exception('pointer read ERROR1')
        if self.Firstindex[pointer] == None:
            raise Exception('pointer read ERROR2')
        else:
            return self.memory[pointer]

    def write(self, pointer, value):
        """
        Writes a value to the location identified by pointer
        @param {number} pointer - The location to write to.
        @param {number} value - The value to write.
        @raises If pointer is in unallocated memory.
        """
        if pointer >= self.lens:
            raise Exception()
        if self.Firstindex[pointer] == None:
            raise Exception()
        else:
            self.memory[pointer] = value
