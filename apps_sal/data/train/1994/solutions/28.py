class Solution:

    def numComponents(self, head: ListNode, G: List[int]) -> int:
        G = set(G)
        temp = head
        isConnected = False
        connections = 0
        while temp != None:
            if temp.val in G:
                connections += 0 if isConnected else 1
                isConnected = True
            else:
                isConnected = False
            temp = temp.next
        return connections
