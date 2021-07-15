from math import floor
from math import ceil
from math import sqrt
from collections import deque
import numpy
from _collections import deque
#from _ast import Num # LC doesn't like this
from heapq import *
from typing import List
import random

MOD = int(1e9 + 7)
BASE = 256
\"\"\"
Maintain a v to list mapping
this is the complete stale of final answer
two states to maintain
1. ansT


\"\"\"


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        vToN = {}
        ps = 0
        vToN[0] = None

        curT = head
        ansH = None
        ansT = None

        while curT:
            newPs = ps + curT.val
            #print(newPs, vToN)

            if newPs in vToN:
                newAnsT = vToN[newPs]
                if newAnsT:

                    tempT = newAnsT
                    tempPs = newPs
                    while tempT != ansT:
                        tempT = tempT.next
                        tempPs += tempT.val
                        del vToN[tempPs]
                        
                    ansT = newAnsT
                    ansT.next = None
                else:
                    ansH = None
                    ansT = None
                    vToN.clear()
                    vToN[0] = None
            else:
                if ansT:
                    ansT.next = curT
                else:
                    ansH = curT
                ansT = curT
                vToN[newPs] = curT
            ps = newPs
            curT = curT.next
        
        
        return ansH


def toLL(l):
    head = ListNode(l[0])
    tail = head
    for i in range(1, len(l)):
        node = ListNode(l[i])
        tail.next = node
        tail = node
    return head

def pl(head):
    while head:
        print(head.val)
        head = head.next
\"\"\"
S = Solution()
head = [1,2,3,-3,-2]
head = [1,2,3,-3,3]
head = [1,2,3,-3,4]
head = [1,2,-3,3,1]
head = [1, -1]
pl(S.removeZeroSumSublists(toLL(head)))
#S.removeZeroSumSublists(None)
\"\"\"
