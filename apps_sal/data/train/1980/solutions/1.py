class Node:
    def __init__(self, value=None, next=None, down=None):
        self.value = value
        self.next = next
        self.down = down


class Skiplist:

    def __init__(self):
        self.dict1 = dict()

    def search(self, target: int) -> bool:
        return target in list(self.dict1.keys())

    def add(self, num: int) -> None:
        self.dict1[num] = self.dict1.get(num, 0) + 1

    def erase(self, num: int) -> bool:
        if(num in list(self.dict1.keys())):
            self.dict1[num] -= 1
            if(self.dict1[num] == 0):
                del self.dict1[num]
            return True
        return False


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
