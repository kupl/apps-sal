class Solution:

    def addToHashmap(self, hashmap, key, val):
        if hashmap.get(key) is None:
            hashmap[key] = [val]
        else:
            x = hashmap[key]
            x.append(val)
            hashmap[key] = x

    def nextLargerNodes(self, head: ListNode) -> List[int]:
        stack = []
        curr = head
        new = []
        i = 0
        hashmap = {}
        while curr is not None:
            while i > 0 and stack[i - 1] < curr.val:
                x = stack.pop()
                self.addToHashmap(hashmap, x, curr.val)
                i -= 1
            stack.append(curr.val)
            i += 1
            curr = curr.next
        temp = head
        while temp is not None:
            if hashmap.get(temp.val) is not None:
                x = hashmap.get(temp.val)
                if len(x) > 0:
                    new.append(x[0])
                    x.remove(x[0])
                else:
                    new.append(0)
            else:
                new.append(0)
            temp = temp.next
        return new
