class MemoryManager:
    def __init__(self, memory):
        """
        @constructor Creates a new memory manager for the provided array.
        @param {memory} An array to use as the backing memory.
        """
        self.memory = memory
        self.available_memory = len(memory)
        self.pointer_list = {0:0}
        self.pointer = 0

    def allocate(self, size):
        """
        Allocates a block of memory of requested size.
        @param {number} size - The size of the block to allocate.
        @returns {number} A pointer which is the index of the first location in the allocated block.
        @raises If it is not possible to allocate a block of the requested size.
        """
        if self.available_memory >= size:
            self.pointer_list[self.pointer] = size
            _pointer = self.pointer
            self.pointer += size
            self.available_memory -= size
            return _pointer
        else:
            raise Exception

    def release(self, pointer):
        """
        Releases a previously allocated block of memory.
        @param {number} pointer - The pointer to the block to release.
        @raises If the pointer does not point to an allocated block.
        """
        free_memory = self.pointer_list[pointer]
        self.available_memory += free_memory
#         self.pointer -= free_memory
        self.pointer = pointer if pointer < self.pointer else self.pointer
        del self.pointer_list[pointer]

    def read(self, pointer):
        """
        Reads the value at the location identified by pointer
        @param {number} pointer - The location to read.
        @returns {number} The value at that location.
        @raises If pointer is in unallocated memory.
        """
        for p, memory_block in self.pointer_list.items():
            if pointer <= memory_block:
                return self.memory[pointer]
        raise Exception

    def write(self, pointer, value):
        """
        Writes a value to the location identified by pointer
        @param {number} pointer - The location to write to.
        @param {number} value - The value to write.
        @raises If pointer is in unallocated memory.
        """
        for p, memory_block in self.pointer_list.items():
            if pointer < memory_block:
                self.memory[pointer] = value
                return
        raise Exception
