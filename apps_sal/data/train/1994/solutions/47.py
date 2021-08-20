class Solution:

    def binarySearch(self, val, G):
        start = 0
        end = len(G) - 1
        while start <= end:
            mid = (start + end) // 2
            if G[mid] == val:
                return True
            elif G[mid] > val:
                end = mid - 1
            else:
                start = mid + 1
        return False

    def numComponents(self, head: ListNode, G: List[int]) -> int:
        G.sort()
        curr = head
        i = 0
        dict_clusters = {}
        while curr is not None:
            if i not in dict_clusters:
                dict_clusters[i] = []
            if self.binarySearch(curr.val, G):
                dict_clusters[i].append(curr.val)
            if curr.val not in G:
                i += 1
            curr = curr.__next__
        count = 0
        for i in dict_clusters:
            if len(dict_clusters[i]) > 0:
                count += 1
        return count
