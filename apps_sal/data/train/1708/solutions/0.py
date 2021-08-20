"""
some useful information about memory allocation in operating system

->There are various algorithms which are implemented by the Operating System in order to find out the holes(continuous empy blocks)   in the linked list(array in this kata) and allocate them to the processes.

->various algorithms used by operating system:
    1. First Fit Algorithm => First Fit algorithm scans the linked list and whenever it finds the first big enough hole to store a process, it stops scanning and load the process into that hole.
    
    2. Next Fit Algorithm  => Next Fit algorithm is similar to First Fit algorithm except the fact that, Next fit scans the linked list from the node where it previously allocated a hole.
                              ( if i have allocated memory of size 8 in previous turn and initial pointer is 3                                 then in next turn os will start searching for next empty hole from position 11(3+8=11) )
    
    3. Best Fit Algorithm  => The Best Fit algorithm tries to find out the smallest hole possible in the list that can accommodate the size requirement of the process.
    
    4. Worst Fit Algorithm => it is opposite of Best Fit Algorithm meaning that                               (The worst fit algorithm scans the entire list every time and tries to find out the biggest hole in the list which can fulfill the requirement of the process.)
    
    The first fit and best fit algorithms are the best algorithm among all

PS. I HAVE IMPLEMENTED Best Fit Algorithm IN JAVASCRIPT AND IMPLEMENTED Next Fit Algorithm in PYTHON :)
"""


class MemoryManager:

    def __init__(self, memory):
        self.storage = [True] * len(memory)
        self.previous_allocated_index = 0
        self.allocated = {}
        self.data = memory

    def allocate(self, size):
        find_next = self.process_allocate(self.previous_allocated_index, len(self.data) - size + 1, size)
        if find_next is not None:
            return find_next
        from_start = self.process_allocate(0, self.previous_allocated_index - size + 1, size)
        if from_start is not None:
            return from_start
        raise IndexError('caused by insufficient space in storage')

    def process_allocate(self, initial, end, size):
        for i in range(initial, end):
            if all(self.storage[i:i + size]):
                self.previous_allocated_index = i
                self.storage[i:i + size] = [False] * size
                self.allocated[i] = i + size
                return i

    def release(self, pointer):
        if self.storage[pointer]:
            raise RuntimeError('caused by providing incorrect pointer for releasing memory')
        size = self.allocated[pointer] - pointer
        self.storage[pointer:size] = [True] * size
        self.data[pointer:size] = [None] * size
        del self.allocated[pointer]

    def read(self, pointer):
        if self.storage[pointer]:
            raise RuntimeError('caused by providing incorrect pointer for reading memory')
        return self.data[pointer]

    def write(self, pointer, value):
        if self.storage[pointer]:
            raise RuntimeError('caused by providing incorrect pointer for writing memory')
        self.data[pointer] = value
