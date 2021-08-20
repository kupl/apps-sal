class MemoryManager:

    def __init__(self, memory):
        """
        @constructor Creates a new memory manager for the provided array.
        @param {memory} An array to use as the backing memory.
        """
        self.mem = memory
        self.blockpointers = []
        self.blocksizes = []

    def allocate(self, size):
        """
        Allocates a block of memory of requested size.
        @param {number} size - The size of the block to allocate.
        @returns {number} A pointer which is the index of the first location in the allocated block.
        @raises If it is not possible to allocate a block of the requested size.
        """
        if size > len(self.mem):
            raise Exception('Cannot allocate more memory than exists')
        if self.blockpointers == [] or (0 not in self.blockpointers and size <= self.blockpointers[0]):
            self.blockpointers.insert(0, 0)
            self.blocksizes.insert(0, size)
            return 0
        for (i, e) in enumerate(self.blocksizes[:-1]):
            if size <= self.blockpointers[i + 1] - self.blockpointers[i] - e:
                self.blockpointers.insert(i, self.blockpointers[i] + e)
                self.blocksizes.insert(i, size)
                return self.blockpointers[i]
        if size <= len(self.mem) - self.blockpointers[-1] - self.blocksizes[-1]:
            self.blockpointers.append(self.blockpointers[-1] + self.blocksizes[-1])
            self.blocksizes.append(size)
            return self.blockpointers[-1]
        raise Exception('Cannot allocate more memory than available')

    def release(self, pointer):
        """
        Releases a previously allocated block of memory.
        @param {number} pointer - The pointer to the block to release.
        @raises If the pointer does not point to an allocated block.
        """
        if pointer not in self.blockpointers:
            raise Exception('No memory has been allocated')
        index = self.blockpointers.index(pointer)
        self.blockpointers.pop(index)
        self.blocksizes.pop(index)
        return

    def read(self, pointer):
        """
        Reads the value at the location identified by pointer
        @param {number} pointer - The location to read.
        @returns {number} The value at that location.
        @raises If pointer is in unallocated memory.
        """
        if not self.inMemory(pointer):
            raise Exception('No memory has been allocated')
        return self.mem[pointer]

    def write(self, pointer, value):
        """
        Writes a value to the location identified by pointer
        @param {number} pointer - The location to write to.
        @param {number} value - The value to write.
        @raises If pointer is in unallocated memory.
        """
        if not self.inMemory(pointer):
            raise Exception('No memory has been allocated')
        self.mem[pointer] = value

    def inMemory(self, pointer):
        """
        Checks if pointer is in allocated memory
        @param {number} pointer - The location in memory.
        @raises If pointer is in unallocated memory.
        """
        i = 0
        while pointer < self.blockpointers[i] + self.blocksizes[i]:
            if pointer >= self.blockpointers[i] and i < self.blockpointers[i] + self.blocksizes[i]:
                return True
            i += 1
        return False
