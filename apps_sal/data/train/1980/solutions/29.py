import random


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.down = None


class Skiplist:

    def __init__(self):
        self.levels = [Node(-1) for i in range(16)]
        for i in range(0, 15):
            self.levels[i].down = self.levels[i + 1]
        self.arr = []

    def coinflip(self):
        a = random.random() > 0.5
        return a

    def searchpath(self, value):
        self.arr = []
        for i in range(16):
            self.arr.append(self.levels[i])
        curlevelhead = self.levels[0]
        i = 0
        while(i < 16):
            while(curlevelhead):
                if curlevelhead.val < value:
                    self.arr[i] = curlevelhead
                    prev = curlevelhead
                    curlevelhead = curlevelhead.__next__
                else:
                    break

            i += 1
            if i != 16:
                curlevelhead = prev.down

    def search(self, target: int) -> bool:
        self.searchpath(target)
        if self.arr[15].__next__ and self.arr[15].next.val == target:
            return True
        return False

    def add(self, num: int) -> None:
        self.searchpath(num)
        if self.arr[15].__next__ and self.arr[15].__next__ == num:
            a = 1
        else:
            i = 1
            prev = None
            check = True
            while(i <= 16):
                temp = self.arr[16 - i].__next__
                self.arr[16 - i].next = Node(num)
                self.arr[16 - i].next.next = temp

                if prev:
                    self.arr[16 - i].next.down = prev
                prev = self.arr[16 - i].__next__
                check = self.coinflip()
                if check == True:
                    i += 1
                elif check == False:
                    return

    def erase(self, num: int) -> bool:
        self.searchpath(num)
        i = 1
        check = False
        while(i <= 16):
            temp = self.arr[16 - i].__next__
            if temp and temp.val == num:
                check = True
                self.arr[16 - i].next = self.arr[16 - i].next.__next__
            i += 1
        return check
