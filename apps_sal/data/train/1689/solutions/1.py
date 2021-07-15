# import all important libraries and inbuilt functions

from fractions import Fraction
import numpy as np
import sys,bisect,copyreg,copy,statistics,os
from math import *
from collections import Counter,defaultdict,deque,OrderedDict   
from itertools import combinations,permutations,accumulate 
from numpy.linalg import matrix_power as mp
from bisect import bisect_left,bisect_right,bisect,insort,insort_left,insort_right
from statistics import mode
from functools import reduce,cmp_to_key 
from io import BytesIO, IOBase
from scipy.spatial import ConvexHull
from heapq import *
from decimal import *
from queue import Queue,PriorityQueue
from re import sub,subn

# end of library import

# map system version faults
if sys.version_info[0] < 3:
    from builtins import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip

# template of many functions used in competitive programming can add more later 
# based on need we will use this commonly.

# bfs in a graph
def bfs(adj,v): # a schema of bfs
    visited=[False]*(v+1);q=deque()
    while q:pass

# definition of vertex of a graph
def graph(vertex): return [[] for i in range(vertex+1)]

def powermodulo(x, y, p) : 
    res = 1;x = x % p        
    if (x == 0) : return 0  
    while (y > 0) : 
        if ((y & 1) == 1) :   res = (res * x) % p 
        y = y >> 1 
        x = (x * x) % p           
    return res

def lcm(a,b): return (a*b)//gcd(a,b)

# most common list in a array of lists
def most_frequent(List):return Counter(List).most_common(1)[0][0]

# element with highest frequency
def most_common(List):return(mode(List))

#In number theory, the Chinese remainder theorem states that 
#if one knows the remainders of the Euclidean division of an integer n by 
#several integers, then one can determine uniquely the remainder of the 
#division of n by the product of these integers, under the condition 
#that the divisors are pairwise coprime.
def chinese_remainder(a, p):
    prod = reduce(op.mul, p, 1);x = [prod // pi for pi in p]
    return sum(a[i] * powermodulo(x[i], p[i] - 2, p[i]) * x[i] for i in range(len(a))) % prod

# make a matrix
def createMatrix(rowCount, colCount, dataList):   
    mat = []
    for i in range (rowCount):
        rowList = []
        for j in range (colCount):
            if dataList[j] not in mat:rowList.append(dataList[j])
        mat.append(rowList) 
    return mat

# input for a binary tree
def readTree(): 
    v=int(inp());adj=[set() for i in range(v+1)]
    for i in range(v-1):u1,u2=In(); adj[u1].add(u2);adj[u2].add(u1)
    return adj,v
    
# sieve of prime numbers    
def sieve():
    li=[True]*1000001;li[0],li[1]=False,False;prime=[]
    for i in range(2,len(li),1):
        if li[i]==True:
            for j in range(i*i,len(li),i):li[j]=False    
    for i in range(1000001):
        if li[i]==True:prime.append(i)
    return prime

#count setbits of a number.
def setBit(n):
    count=0
    while n!=0:n=n&(n-1);count+=1
    return count

# sum of digits of a number
def digitsSum(n):
    if n == 0:return 0
    r = 0
    while n > 0:r += n % 10;n //= 10
    return r

# ncr efficiently
def ncr(n, r):
    r = min(r, n - r);numer = reduce(op.mul, list(range(n, n - r, -1)), 1);denom = reduce(op.mul, list(range(1, r + 1)), 1)
    return numer // denom  # or / in Python 2

#factors of a number
def factors(n):return list(set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))

#prime fators of a number
def prime_factors(n):
    i = 2;factors = []
    while i * i <= n:
        if n % i:i += 1
        else:n //= i;factors.append(i)
    if n > 1:factors.append(n)
    return len(set(factors))

def prefixSum(arr):
    for i in range(1, len(arr)):arr[i] = arr[i] + arr[i-1]
    return arr    

def binomial_coefficient(n, k):
    if 0 <= k <= n:
        ntok = 1;ktok = 1
        for t in range(1, min(k, n - k) + 1):ntok *= n;ktok *= t;n -= 1
        return ntok // ktok
    else:return 0
 
def powerOfK(k, max):
    if k == 1:return [1]
    if k == -1:return [-1, 1] 
    result = [];n = 1
    while n <= max:result.append(n);n *= k
    return result

# maximum subarray sum use kadane's algorithm
def kadane(a,size):
    max_so_far = 0;max_ending_here = 0 
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):max_so_far = max_ending_here 
        if max_ending_here < 0:max_ending_here = 0
    return max_so_far                                    
                  
def divisors(n):
    result = []
    for i in range(1,ceil(sqrt(n))+1):
        if n%i == 0:
            if n/i == i:result.append(i)
            else:result.append(i);result.append(n/i)
    return result

def sumtilln(n): return ((n*(n+1))//2)

def isPrime(n) : 
	if (n <= 1) :return False
	if (n <= 3) :return True
	if (n % 2 == 0 or n % 3 == 0) :return False
	for i in range(5,ceil(sqrt(n))+1,6):
		if (n % i == 0 or n % (i + 2) == 0) :return False
	return True

def isPowerOf2(n):
    while n % 2 == 0:n //= 2
    return (True if n == 1 else False)

def power2(n):
    k = 0
    while n % 2 == 0:k += 1;n //= 2
    return k

def sqsum(n):return ((n*(n+1))*(2*n+1)//6)
    
def cusum(n):return ((sumn(n))**2)

def pa(a):
    for i in range(len(a)):print(a[i], end = " ")
    print()

def pm(a,rown,coln):
    for i in range(rown):
        for j in range(coln):print(a[i][j],end = " ")
        print()

def pmasstring(a,rown,coln):
    for i in range(rown):
        for j in range(coln):print(a[i][j],end = "")
        print()
        
def isPerfectSquare(n):return pow(floor(sqrt(n)),2) == n

def nC2(n,m):return (((n*(n-1))//2) % m)

def modInverse(n,p):return powermodulo(n,p-2,p)

def ncrmodp(n, r, p):  
	num = den = 1
	for i in range(r):num = (num * (n - i)) % p ;den = (den * (i + 1)) % p 
	return (num * powermodulo(den,p - 2, p)) % p 

def reverse(string):return "".join(reversed(string))        

def listtostr(s):return ' '.join([str(elem) for elem in s]) 

def binarySearch(arr, l, r, x): 
	while l <= r: 
		mid = l + (r - l) // 2; 
		if arr[mid] == x:return mid 
		elif arr[mid] < x:l = mid + 1
		else:r = mid - 1
	return -1

def isarrayodd(a):
    r = True
    for i in range(len(a)):
        if a[i] % 2 == 0:
            r = False
            break
    return r

def isPalindrome(s):return s == s[::-1] 

def gt(x,h,c,t):return ((x*h+(x-1)*c)/(2*x-1))

def CountFrequency(my_list): 
    freq = {} 
    for item in my_list:freq[item] = (freq[item] + 1 if (item in freq) else 1)
    return freq

def CountFrequencyasPair(my_list1,my_list2,freq): 
    for item in my_list1:freq[item][0] = (freq[item][0] + 1 if (item in freq) else 1)
    for item in my_list2:freq[item][1] = (freq[item][1] + 1 if (item in freq) else 1)     
    return freq 
 
def binarySearchCount(arr, n, key):   
    left = 0;right = n - 1;count = 0  
    while (left <= right):  
        mid = int((right + left) / 2) 
        if (arr[mid] <= key):count,left = mid + 1,mid + 1
        else:right = mid - 1      
    return count

def primes(n):
  sieve,l = [True] * (n+1),[]
  for p in range(2, n+1):
    if (sieve[p]):
      l.append(p)
      for i in range(p, n+1, p):sieve[i] = False
  return l

def Next_Greater_Element_for_all_in_array(arr): 
	s,n,reta,retb = list(),len(arr),[],[];arr1 = [list([0,i]) for i in range(n)]
	for i in range(n - 1, -1, -1): 
		while (len(s) > 0 and s[-1][0] <= arr[i]):s.pop() 
		if (len(s) == 0):arr1[i][0] = -1					
		else:arr1[i][0] = s[-1]	 
		s.append(list([arr[i],i]))		
	for i in range(n):reta.append(list([arr[i],i]));retb.append(arr1[i][0])
	return reta,retb

def polygonArea(X,Y,n):   
    area = 0.0;j = n - 1
    for i in range(n):area += (X[j] + X[i]) * (Y[j] - Y[i]);j = i   
    return abs(area / 2.0)
 
#defining a LRU Cache
# where we can set values and get values based on our requirement
class LRUCache: 
	# initialising capacity 
	def __init__(self, capacity: int): 
		self.cache = OrderedDict() 
		self.capacity = capacity 

	# we return the value of the key 
	# that is queried in O(1) and return -1 if we 
	# don't find the key in out dict / cache. 
	# And also move the key to the end 
	# to show that it was recently used. 
	def get(self, key: int) -> int: 
		if key not in self.cache:return -1
		else:self.cache.move_to_end(key);return self.cache[key] 

	# first, we add / update the key by conventional methods. 
	# And also move the key to the end to show that it was recently used. 
	# But here we will also check whether the length of our 
	# ordered dictionary has exceeded our capacity, 
	# If so we remove the first key (least recently used) 
	def put(self, key: int, value: int) -> None: 
		self.cache[key] = value;self.cache.move_to_end(key) 
		if len(self.cache) > self.capacity:self.cache.popitem(last = False)

class segtree:
    def __init__(self,n):
        self.m = 1
        while self.m < n:self.m *= 2
        self.data = [0] * (2 * self.m)
    def __setitem__(self,i,x):
        x = +(x != 1);i += self.m;self.data[i] = x;i >>= 1
        while i:self.data[i] = self.data[2 * i] + self.data[2 * i + 1];i >>= 1
    def __call__(self,l,r):
        l += self.m;r += self.m;s = 0
        while l < r:
            if l & 1:s += self.data[l];l += 1
            if r & 1:r -= 1;s += self.data[r]
            l >>= 1;r >>= 1
        return s        

class FenwickTree:
  def __init__(self, n):self.n = n;self.bit = [0]*(n+1)  
  def update(self, x, d):
    while x <= self.n:self.bit[x] += d;x += (x & (-x))  
  def query(self, x):
    res = 0
    while x > 0:res += self.bit[x];x -= (x & (-x))
    return res
  def range_query(self, l, r):return self.query(r) - self.query(l-1)        
# can add more template functions here
    
# end of template functions

# To enable the file I/O i the below 2 lines are uncommented.
# read from in.txt if uncommented
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
# will print on Console if file I/O is not activated
if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')

# inputs template
#for fast input we areusing sys.stdin
def inp(): return sys.stdin.readline().strip()

#for fast output, always take string
def out(var): sys.stdout.write(str(var))  

# cusom base input needed for the program
def I():return (inp())
def II():return (int(inp()))
def FI():return (float(inp()))
def SI():return (list(str(inp())))
def MI():return (map(int,inp().split()))
def LI():return (list(MI()))
def SLI():return (sorted(LI()))
def MF():return (map(float,inp().split()))
def LF():return (list(MF()))

# end of inputs template

# common modulo values used in competitive programming
MOD = 998244353
mod = 10**9+7

# any particular user-defined functions for the code.
# can be written here.  
def solve():
    n,m = MI()
    ss = []
    for _ in range(n):
        ss.append(list(I()) + ['#'])
    ss.append(['#']*(m+1))
    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            if ss[i+1][j] == '#' and ss[i][j+1] == '#' and (i,j) != (n-1, m-1):
                ss[i][j] = '#'
    res = [ss[0][0]]
    cend = {(0,0)}
    for _ in range(n+m-2):
        ncend = set()
        mn = 'z'
        for i,j in cend:
            if ss[i+1][j] != '#' and ss[i+1][j] <= mn:
                ncend.add((i+1, j))
                mn = ss[i+1][j]
            if ss[i][j+1] != '#' and ss[i][j+1] <= mn:
                ncend.add((i, j+1))
                mn = ss[i][j+1]
        res.append(mn)
        cend = {(i,j) for (i,j) in ncend if ss[i][j] == mn}

    print(''.join(res))
# end of any user-defined functions

# main functions for execution of the program.
def __starting_point():  
    # execute your program from here.
    # start your main code from here
        
    # Write your code here
    for _ in range(II()):solve()
                    
    # end of main code
    # end of program

# This program is written by :
#   Shubham Gupta
#   B.Tech (2019-2023)
#   Computer Science and Engineering,
#   Department of EECS
#   Contact No:8431624358
#   Indian Institute of Technology(IIT),Bhilai
#   Sejbahar,
#   Datrenga,
#   Raipur,
#   Chhattisgarh
#   492015

#   THANK YOU FOR 
#YOUR KIND PATIENCE FOR READING THE PROGRAM.    
__starting_point()
