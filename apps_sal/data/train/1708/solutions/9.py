class MemoryManager:
    def __init__(self, memory):
        """
        @constructor Creates a new memory manager for the provided array.
        @param {memory} An array to use as the backing memory.
        """

        self.cache = {}
        self.memory = memory

    def allocate(self, size):
        """
        Allocates a block of memory of requested size. Strategy: 

        1) assert that size is less than memory size, 
        2) add if memory is empty,
        3) allocate memory before the first index,
        4) in between each block, 
        5) Lastly try after the last index + length
        6) Throw error

        @param {number} size - The size of the block to allocate.
        @returns {number} A pointer which is the index of the first location in the allocated block.
        @raises If it is not possible to allocate a block of the requested size.
        """

        if size > len(self.memory):
            raise Exception("Cannot allocate mory memory than exists")
        elif len(self.cache.items()) == 0:
            self.cache[0] = size - 1
            return 0

        for start, length in self.cache.items():
            index = list(self.cache.keys()).index(start)
            next_block = list(self.cache.items())[index + 1] if index + 1 < len(self.cache.items()) else None
            if index == 0 and (size - 1) < start:
                self.cache[0] = size - 1
                return 0
            elif next_block and next_block[0] - (start + length + 1) >= size:
                self.cache[start + length + 1] = size - 1
                return start + length + 1
            elif next_block is None and len(self.memory) - (start + length + 1) >= size:
                self.cache[start + length + 1] = size - 1
                return start + length + 1

        raise Exception("Failed to allocate memory")

    def release(self, pointer):
        """
        Releases a previously allocated block of memory.
        @param {number} pointer - The pointer to the block to release.
        @raises If the pointer does not point to an allocated block.
        """
        if pointer not in list(self.cache.keys()):
            raise Exception("Pointer does not point towards allocated block")

        del self.cache[pointer]

    def read(self, pointer):
        """
        Reads the value at the location identified by pointer
        @param {number} pointer - The location to read.
        @returns {number} The value at that location.
        @raises If pointer is in unallocated memory.
        """

        if len(self.cache.items()) == 0:
            raise Exception("No memory has been allocated")

        for start, length in self.cache.items():
            if pointer not in range(start, start + length):
                raise Exception("Pointer does not point towards allocated block")

        return self.memory[pointer]

    def write(self, pointer, value):
        """
        Writes a value to the location identified by pointer
        @param {number} pointer - The location to write to.
        @param {number} value - The value to write.
        @raises If pointer is in unallocated memory.
        """

        if len(self.cache.items()) == 0:
            raise Exception("No memory has been allocated")

        for start, length in self.cache.items():
            if pointer not in range(start, start + length + 1):
                raise Exception("Pointer does not point towards allocated block")

        self.memory[pointer] = value
