class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        self.d1 = self.d2 = self.d3 = 0
        reservedSeats = sorted(reservedSeats, key=lambda x:x[0])
        ptr = 0
        i = 0
        ans  = 0
        while i < len(reservedSeats):
            if reservedSeats[i][0] != ptr:
                if self.d1 ^ 15 == 15:
                    ans += 1
                    if self.d3 ^ 15 == 15:
                        ans += 1
                elif self.d2 ^ 15 == 15:
                    ans += 1
                elif self.d3 ^ 15 == 15:
                    ans += 1
                ans += 2 * (reservedSeats[i][0] - ptr - 1)
                self.d1 = self.d2 = self.d3 = 0
                ptr = reservedSeats[i][0]
            self.seat(reservedSeats[i][1])
            i += 1
        
        if self.d1 ^ 15 == 15:
            ans += 1
            if self.d3 ^ 15 == 15:
                ans += 1
        elif self.d2 ^ 15 == 15:
            ans += 1
        elif self.d3 ^ 15 == 15:
            ans += 1
        ans += 2 * (n - ptr)
        
        return ans - 2
                
    def seat(self, i):
        if i == 2 or i == 3:
            self.d1 += 2 ** (i - 2)
        elif i == 4 or i == 5:
            self.d1 += 2 ** (i - 2)
            self.d2 += 2 ** (i - 4)
        elif i == 6 or i == 7:
            self.d2 += 2 ** (i - 4)
            self.d3 += 2 ** (i - 6)
        elif i == 8 or i == 9:
            self.d3 += 2 ** (i - 6)

