class Solution:
    memory = {}
    largest = [0]
    trackerForLargest = {}
    largestSize = [0]
    numGroups = [0]

    def countLargestGroup(self, n: int) -> int:
        if n > self.largest[0]:
            for num in range(self.largest[0] + 1, n + 1):
                curr = num
                currSum = 0
                while curr != 0:
                    currSum += curr % 10
                    curr //= 10

                if currSum not in self.trackerForLargest:
                    self.trackerForLargest[currSum] = []

                self.trackerForLargest[currSum].append(num)

                if len(self.trackerForLargest[currSum]) == self.largestSize[0]:
                    self.numGroups[0] += 1
                elif len(self.trackerForLargest[currSum]) > self.largestSize[0]:
                    self.numGroups[0] = 1
                    self.largestSize[0] = len(self.trackerForLargest[currSum])

                self.memory[num] = self.numGroups[0]

            self.largest[0] = n

        return self.memory[n]
