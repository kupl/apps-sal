class MemoryManager:

    def __init__(self, memory):
        """
        @constructor Creates a new memory manager for the provided array.
        @param {memory} An array to use as the backing memory.
        """
        self.memory = memory
        self.allocationStarts = []
        self.allocationSizes = []

    def allocate(self, size):
        """
        Allocates a block of memory of requested size.
        @param {number} size - The size of the block to allocate.
        @returns {number} A pointer which is the index of the first location in the allocated block.
        @raises If it is not possible to allocate a block of the requested size.
        """
        for i in range(len(self.memory)):
            ok = True
            for j in range(i, i + size):
                if j >= len(self.memory):
                    ok = False
                    break
                    raise Exception('No allocation available')
                for k in range(len(self.allocationStarts)):
                    if j >= self.allocationStarts[k] and j < self.allocationStarts[k] + self.allocationSizes[k]:
                        ok = False
                        break
            if ok:
                self.allocationStarts.append(i)
                self.allocationSizes.append(size)
                return i
        raise Exception('No allocation available')

    def release(self, pointer):
        """
        Releases a previously allocated block of memory.
        @param {number} pointer - The pointer to the block to release.
        @raises If the pointer does not point to an allocated block.
        """
        index = self.allocationStarts.index(pointer)
        del self.allocationStarts[index]
        del self.allocationSizes[index]

    def read(self, pointer):
        """
        Reads the value at the location identified by pointer
        @param {number} pointer - The location to read.
        @returns {number} The value at that location.
        @raises If pointer is in unallocated memory.
        """
        if len(self.allocationStarts) == 0:
            raise Exception('No memory has been allocated')
        for i in range(len(self.allocationStarts)):
            if not (pointer < self.allocationStarts[i] + self.allocationSizes[i] and pointer >= self.allocationStarts[i]):
                raise Exception('Cannot read from unallocated area')
        return self.memory[pointer]

    def write(self, pointer, value):
        """
        Writes a value to the location identified by pointer
        @param {number} pointer - The location to write to.
        @param {number} value - The value to write.
        @raises If pointer is in unallocated memory.
        """
        if len(self.allocationStarts) == 0:
            raise Exception('No memory has been allocated')
        for i in range(len(self.allocationStarts)):
            if not (pointer < self.allocationStarts[i] + self.allocationSizes[i] and pointer >= self.allocationStarts[i]):
                raise Exception('Cannot write to unallocated area')
        self.memory[pointer] = value
