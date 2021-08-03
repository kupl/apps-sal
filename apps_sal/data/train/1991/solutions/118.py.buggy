class Solution:
    \"\"\"
    You are given an array of distinct positive integers locations where locations[i] 
    represents the position of city i. You are also given integers start, finish and fuel
    representing the starting city, ending city, and the initial amount of fuel you have,
    respectively.

    At each step, if you are at city i, you can pick any city j such that j != i and 
    0 <= j < locations.length and move to city j. Moving from city i to city j reduces
    the amount of fuel you have by |locations[i] - locations[j]|. Please notice that |x|
    denotes the absolute value of x.

    Notice that fuel cannot become negative at any point in time, and that you are allowed
    to visit any city more than once (including start and finish).

    Return the count of all possible routes from start to finish.

    Since the answer may be too large, return it modulo 10^9 + 7.

    Example 1:

    Input: locations = [2,3,6,8,4], start = 1, finish = 3, fuel = 5
    Output: 4
    Explanation: The following are all possible routes, each uses 5 units of fuel:
    1 -> 3
    1 -> 2 -> 3
    1 -> 4 -> 3
    1 -> 4 -> 2 -> 3

    Example 2:

    Input: locations = [4,3,1], start = 1, finish = 0, fuel = 6
    Output: 5
    Explanation: The following are all possible routes:
    1 -> 0, used fuel = 1
    1 -> 2 -> 0, used fuel = 5
    1 -> 2 -> 1 -> 0, used fuel = 5
    1 -> 0 -> 1 -> 0, used fuel = 3
    1 -> 0 -> 1 -> 0 -> 1 -> 0, used fuel = 5
    
    Example 3:

    Input: locations = [5,2,1], start = 0, finish = 2, fuel = 3
    Output: 0
    Explanation: It's impossible to get from 0 to 2 using only 3 units of fuel since the shortest 
                 route needs 4 units of fuel.
    
    Example 4:

    Input: locations = [2,1,5], start = 0, finish = 0, fuel = 3
    Output: 2
    Explanation: There are two possible routes, 0 and 0 -> 1 -> 0.
    
    Example 5:

    Input: locations = [1,2,3], start = 0, finish = 2, fuel = 40
    Output: 615088286
    Explanation: The total number of possible routes is 2615088300. Taking this number 
                 modulo 10^9 + 7 gives us 615088286.

    Constraints:

    2 <= locations.length <= 100
    1 <= locations[i] <= 10^9
    All integers in locations are distinct.
    0 <= start, finish < locations.length
    1 <= fuel <= 200

    Idea: Solve with dynamic programming in O(n^3 * F) where n = number of cities, F = fuel
          N[i,j,f] = number of ways to get from i to j using f units of fuel
          
          N[i,j,f] = 0 if |locations[i] - locations[j]| > f
          
          If |locations[i] - locations[j]| == f, we can either go directly from i to j, or
          stop at any (or none) of the locations in between the two, so 
          
          N[i,j,f] = 2**B(i,j) where B(i,j) = number of locations between i and j
                                            = |Rank(i) - Rank(j)| - 1
          
          Otherwise (distance < f):
          
          (A) We can go from i to k (k != i) and from k to j -> N[k,j,f-d(i,k)]
          
          N[i,j,f] = sum_{k != i} N[k,j,f-d(i,k)]
          
          Special case i == j, f >= 0:
          
          N[i,i,f] = 1 + sum_{k != i} N[k,i,f-d(i,k)]
          
          REVIEW
    \"\"\"
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        N = dict()
        n = len(locations)
        # Compute the rank of each location
        order = list(range(n))
        order.sort(key = lambda x: locations[x])
        ranks = [0]*n
        for i in range(n):
            ranks[order[i]] = i        
        def computeNumber(i, j, f, locations, ranks, N):
            distij = abs(locations[i] - locations[j])
            if distij > f:
                return 0
            if distij == f:
                if i == j:
                    return 1
                else:
                    return 2**(abs(ranks[i]-ranks[j])-1)
            if (i, j, f) not in N:
                allWays = 0 if i != j else 1
                for k in range(len(locations)):
                    d = abs(locations[i] - locations[k])
                    if d <= f and k != i:
                        allWays += computeNumber(k,j,f-d,locations,ranks,N)
                N[(i,j,f)] = allWays
            return N[(i,j,f)]
        sol =  computeNumber(start, finish, fuel, locations, ranks, N) % (10**9 + 7)
        return sol
