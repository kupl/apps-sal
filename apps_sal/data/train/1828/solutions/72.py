class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        freq = dict()
        
        for i in range(len(barcodes)):
            freq[barcodes[i]] = freq.get(barcodes[i], 0)+1
        
        heap = list()
        reverse = collections.defaultdict(list)
        
        for el in freq:
            heap.append(-freq[el])
            reverse[freq[el]].append(el)
        
        heapq.heapify(heap)
        
        temp_list = list()
        answer = list()
        
        while True:
            if len(temp_list)>1:
                temp = temp_list.pop(0)
                if temp[0]>0:
                    heapq.heappush(heap, -temp[0])
                    reverse[temp[0]].append(temp[1])
            
            if len(heap)>0:
                cur_freq = -heapq.heappop(heap)
                cur_el = reverse[cur_freq].pop(0)
                answer.append(cur_el)
                temp_list.append([cur_freq-1, cur_el])
            else:
                break
            
        while len(temp_list)>0:
            temp = temp_list.pop(0)
            if temp[0]>0:
                answer.append(temp[1])
                
        return answer

