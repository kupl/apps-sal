'''
I think Idea is to consider for all possible starting pairs (so number1,startingIndex1,number2,startingIndex2), what is longest pair we can get moving forward
'''
class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        BIG_NUMBER = 2**31-1##python can interpret long numbers so we will use this to compute.
        numSplits = {}##tells what the number is represented by the substring from a to b b exclusive.
        sLength = len(S)
        reverseSplits = {}
        for i in range(sLength):
            currentNum = 0
            for j in range(i+1,sLength+1):
                currentNum *= 10
                currentNum += int(S[j-1])
                if currentNum == 0:
                    numSplits[(i,j)] = currentNum
                    if currentNum not in reverseSplits:
                        reverseSplits[currentNum] = {}
                    if i not in reverseSplits[currentNum]:
                        reverseSplits[currentNum][i] = set([j])
                    else:
                        reverseSplits[currentNum][i].add(j)
                    break
                elif currentNum > BIG_NUMBER:
                    break
                else:
                    numSplits[(i,j)] = currentNum
                    if currentNum not in reverseSplits:
                        reverseSplits[currentNum] = {}
                    if i not in reverseSplits[currentNum]:
                        reverseSplits[currentNum][i] = set([j])
                    else:
                        reverseSplits[currentNum][i].add(j)
        fibonacciSequences = {}
        def computeFibonacciSequences(startingIndex):##if startingIndex == 
            if startingIndex not in fibonacciSequences:
                if startingIndex == sLength:
                    answer = [[]]
                else:
                    answer = []
                    for i in range(startingIndex+1,sLength+1):
                        if (startingIndex,i) in numSplits:##so this is a valid number.
                            nextNumber = numSplits[(startingIndex,i)]
                            ithFibonaccis = computeFibonacciSequences(i)
                            for fibSeq in ithFibonaccis:
                                if len(fibSeq) > 1:
                                    largeNumber = fibSeq[-2]
                                    smallNumber = fibSeq[-1]
                                    if nextNumber == largeNumber-smallNumber:
                                        appended = fibSeq+[nextNumber]
                                        answer.append(appended)
                                else:
                                    appended = fibSeq + [nextNumber]
                                    answer.append(appended)
                        else:
                            break
                fibonacciSequences[startingIndex] = answer
                return answer
            else:
                return fibonacciSequences[startingIndex]
        computeFibonacciSequences(0)
        for sequence in fibonacciSequences[0]:
            if len(sequence) >= 3:
                sequence.reverse()
                return sequence
        else:
            return []

                                    
                                

