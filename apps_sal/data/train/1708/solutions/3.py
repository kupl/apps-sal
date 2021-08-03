class MemoryManager:
    def __init__(self, memory):
        """
        @constructor Creates a new memory manager for the provided array.
        @param {memory} An array to use as the backing memory.
        """
        self.memory = memory
        self.allocated = {}
        self.free_memory = {0: len(memory)}

    def allocate(self, size):
        """
        Allocates a block of memory of requested size.
        @param {number} size - The size of the block to allocate.
        @returns {number} A pointer which is the index of the first location in the allocated block.
        @raises If it is not possible to allocate a block of the requested size.
        """
        if size > len(self.memory):
            raise 'Cannot allocate more memory than exists'
        for pointer, block_size in list(self.free_memory.items()):
            if block_size >= size:
                self.allocated[pointer] = size
                self.free_memory[pointer + size] = block_size - size
                del self.free_memory[pointer]
                return pointer
        raise 'Cannot allocate more memory than available'

    def release(self, pointer):
        """
        Releases a previously allocated block of memory.
        @param {number} pointer - The pointer to the block to release.
        @raises If the pointer does not point to an allocated block.
        """
        self.free_memory[pointer] = self.allocated[pointer]
        del self.allocated[pointer]
        for p, b_size in sorted(self.free_memory.items()):
            if self.free_memory.get(p + b_size):
                self.free_memory[p] += self.free_memory[p + b_size]
                del self.free_memory[p + b_size]

    def read(self, pointer):
        """
        Reads the value at the location identified by pointer
        @param {number} pointer - The location to read.
        @returns {number} The value at that location.
        @raises If pointer is in unallocated memory.
        """
        for p, b_size in list(self.allocated.items()):
            if p <= pointer < p + b_size:
                return self.memory[pointer]
        raise 'No memory has been allocated'

    def write(self, pointer, value):
        """
        Writes a value to the location identified by pointer
        @param {number} pointer - The location to write to.
        @param {number} value - The value to write.
        @raises If pointer is in unallocated memory.
        """
        for p, b_size in list(self.allocated.items()):
            if p <= pointer < p + b_size:
                self.memory[pointer] = value
                return None
        raise 'No memory has been allocated'
