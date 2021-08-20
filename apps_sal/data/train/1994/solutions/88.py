class Solution:

    def numComponents(self, head: ListNode, G: List[int]) -> int:
        """
        # approach 1
        # traverse ll, if node in G, put in components as another list or extending the list

        num_components=0
        components=[]

        cur=head
        dummy=ListNode(-1)
        dummy.next=cur

        while cur:
            if cur.val in G:
                if dummy.val in G:
                    component=components[-1]
                    components.pop()
                    component.append(cur.val)
                    components.append(component)
                else:
                    components.append([cur.val])
            dummy=cur
            cur=cur.next

        print(len(components))
        return len(components)
        """
        cur = head
        prev_in = False
        count = 0
        while cur:
            if cur.val in G:
                if not prev_in:
                    count += 1
                prev_in = True
            else:
                prev_in = False
            cur = cur.__next__
        return count
