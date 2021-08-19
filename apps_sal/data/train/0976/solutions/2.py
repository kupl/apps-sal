class Stack:

    def __init__(self):
        self.items = []

    def empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __iter__(self):
        return self

    def __next__(self):
        return _StackIterator(list(self.items()))


class _StackIterator:

    def __init__(self, stack):
        self.stackRef = stack
        self.curInd = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.curInd < self.size():
            entry = self.stackRef[self.curInd]
            self.curInd += 1
            return entry
        else:
            raise StopIteration


def main():
    n = int(input())
    Symbol = Stack()
    Index = Stack()
    FirstBracket = ThirdBracket = 0
    arr = list(map(int, input().split()))
    for i in range(n):
        if arr[i] == 1 or arr[i] == 3:
            Symbol.push(arr[i])
            Index.push(i)
        else:
            temp = Symbol.pop()
            if temp == 1:
                FirstBracket = max(FirstBracket, i - Index.pop() + 1)
            elif temp == 3:
                ThirdBracket = max(ThirdBracket, i - Index.pop() + 1)
    seq = Stack()
    AlterDepth = 0
    curDepth = Stack()
    for i in range(n):
        if (arr[i] == 1 or arr[i] == 3) and seq.empty():
            curDepth.push(1)
            seq.push(arr[i])
            AlterDepth = max(AlterDepth, curDepth.top())
        elif arr[i] == 1 and seq.top() == 3:
            curDepth.push(curDepth.top() + 1)
            seq.push(arr[i])
            AlterDepth = max(AlterDepth, curDepth.top())
        elif arr[i] == 3 and seq.top() == 1:
            curDepth.push(curDepth.top() + 1)
            seq.push(arr[i])
            AlterDepth = max(AlterDepth, curDepth.top())
        elif arr[i] == 1 or arr[i] == 3:
            curDepth.push(curDepth.top())
            seq.push(arr[i])
            AlterDepth = max(curDepth.top(), AlterDepth)
        elif arr[i] == 2 or arr[i] == 4:
            curDepth.pop()
            seq.pop()
    print(AlterDepth, FirstBracket, ThirdBracket)


def __starting_point():
    main()


__starting_point()
