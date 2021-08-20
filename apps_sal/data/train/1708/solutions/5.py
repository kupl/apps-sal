class MemoryManager:

    def __init__(self, memory):
        """
        @constructor Creates a new memory manager for the provided array.
        @param {memory} An array to use as the backing memory.
        """
        self._memory = memory
        self._capacity = len(memory)
        self._allocated = {i: False for i in range(self._capacity)}
        self._pointers = dict()

    def allocate(self, size):
        """
        Allocates a block of memory of requested size.
        @param {number} size - The size of the block to allocate.
        @returns {number} A pointer which is the index of the first location in the allocated block.
        @raises If it is not possible to allocate a block of the requested size.
        """
        if size > self._capacity:
            raise Exception('Request exceeds max system capacity')
        block_start = self._find_empty_block(size)
        if block_start is None:
            raise Exception('No free block of sufficient size found')
        self._pointers[block_start] = size
        for i in range(size):
            self._allocated[block_start + i] = True
        return block_start

    def release(self, pointer):
        """
        Releases a previously allocated block of memory.
        @param {number} pointer - The pointer to the block to release.
        @raises If the pointer does not point to an allocated block.
        """
        if pointer not in self._pointers:
            raise Exception('Pointer was not allocated')
        pointer_size = self._pointers[pointer]
        for i in range(pointer_size):
            self._allocated[pointer + i] = False
        del self._pointers[pointer]

    def read(self, pointer):
        """
        Reads the value at the location identified by pointer
        @param {number} pointer - The location to read.
        @returns {number} The value at that location.
        @raises If pointer is in unallocated memory.
        """
        if not self._allocated[pointer]:
            raise Exception('Memory space not allocated')
        return self._memory[pointer]

    def write(self, pointer, value):
        """
        Writes a value to the location identified by pointer
        @param {number} pointer - The location to write to.
        @param {number} value - The value to write.
        @raises If pointer is in unallocated memory.
        """
        if not self._allocated[pointer]:
            raise Exception('Cannot write at unallocated memory space')
        self._memory[pointer] = value

    def _find_empty_block(self, size):
        """
        Find an free block of size size
        :param size: Pointer size
        :return: index of block start
        """
        contiguous_size = 0
        index = 0
        start_index = None
        while index < self._capacity:
            if index in self._pointers:
                start_index = None
                size_to_skip = self._pointers[index]
                index = index + size_to_skip
                continue
            else:
                if start_index is None:
                    start_index = index
                contiguous_size += 1
                if contiguous_size == size:
                    return start_index
                index += 1
        return None
