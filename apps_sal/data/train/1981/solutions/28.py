class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        heap = []#heap
        dict = defaultdict(int)
        requests.sort()
        count = 0
        start = 0
        for i in requests:
            while heap and heap[0] < i[0]:#若在新的request進來前，有舊的request結尾更早結束
                heap_pop = heapq.heappop(heap)#必須pop掉
                dict[count] += heap_pop + 1 - start#這個舊的request結尾+1減去前一個start，這是一段interval，這段interval的重疊高度為count
                start = heap_pop + 1#同時更新這個這個request的結尾+1為新的start
                count -= 1#因為舊的request pop所以count-1
            heapq.heappush(heap, i[1])#用heap存這個request的結尾
            dict[count] += i[0] - start#當前這個request的起始減掉前一個start，這是一段interval，這段interval的重疊高度為count
            start = i[0]#同時更新這個這個request的起始為新的start
            count += 1#因為是新的request進來，所以count+1
        while heap:#把最後還在heap內的request pop掉
            heap_pop = heapq.heappop(heap)
            dict[count] += heap_pop + 1 - start
            start = heap_pop + 1
            count -= 1
        nums.sort(reverse = True)
        index = 0
        res = 0
        sort_key = sorted(list(dict.keys()), reverse = True)#最後按照count的數量多寡排序，count越多，就讓他乘上越大的值
        for key in sort_key:
            res += key*sum(nums[index:index+dict[key]])#把結果乘起來
            res %= (10**9+7)
            index += dict[key]
        return res
        
        
        # nums.sort(reverse = True)#request用來記錄每個時間點的起始跟結束數量，如過起始碰到結束剛好抵消，然後再用第二個for修改每個時間點room的數量(等於當前count的數量)，最後sort，再相乘
        # print(nums)
        # request = len(nums)*[0]
        # for i in range(len(requests)):
        #     request[requests[i][0]] += 1
        #     if requests[i][1]+1 < len(nums):
        #         request[requests[i][1]+1] -= 1
        # print(request)
        # count = 0
        # for i in range(len(request)):
        #     count += request[i]
        #     request[i] = count
        # request.sort(reverse = True)
        # res = 0
        # for i in range(len(request)):
        #     res = (res + request[i]*nums[i]) % (10**9+7)
        # return res
        
                
        
        # t = len(nums)*[0]#TLE
        # for a,b in requests:
        #     for j in range(a, b+1):
        #         t[j] += 1
        # nums.sort()
        # t.sort()
        # res = 0
        # for i in range(len(nums)-1, -1, -1):
        #     if t[i] == 0:
        #         break
        #     res += nums[i]*t[i]
        #     res %= (10**9+7)
        # return res

