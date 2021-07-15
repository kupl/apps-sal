class TweetCounts:

    def __init__(self):
        self.tweet2time = {}

    def recordTweet(self, tweetName: str, time: int) -> None:
        if tweetName not in self.tweet2time:
            self.tweet2time[tweetName] = [time]
        else:
            arr = self.tweet2time[tweetName]
            index = self.binary_search(arr, time)
            arr.insert(index, time)
            
            

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if tweetName not in self.tweet2time:
            return []
        
        arr = self.tweet2time[tweetName]
        
        if freq == 'minute':
            interval = 60
        elif freq == 'hour':
            interval = 3600
        else:
            interval = 3600 * 60
        
        
        time = startTime
        result = []
        while time <= endTime:
            end_time = time + interval
            start_index = self.binary_search(arr, time)
            end_index = self.binary_search(arr, min(end_time, endTime + 1))
            # if start_index == end_index and arr[-1] == time:
                # end_index += 1
            
            result.append(end_index - start_index)
            
            time = end_time
            
        return result    
    
    def binary_search(self, arr, num):
        # if num <= arr[0]:
            # return 0
        # elif num >= arr[-1]:
            # return len(arr)
        # elif num > arr[-1]:
            # return len(arr) + 1
        # else:
        left = 0
        right = len(arr)

        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] > num:
                right = mid
            elif arr[mid] < num:
                left = mid + 1
            else:
                return mid

        return left    
        


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)

