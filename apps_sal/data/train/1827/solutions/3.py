from math import log
 class Solution:
     def smallestGoodBase(self, n):
         """
         :type n: str
         :rtype: str
         """
         num = int(n)
         
         #use binary search the base
         for size in range(int(log(num+1,2)), 1, -1):
             #find the base
             l,r = 2, int(pow(num, 1.0 / (size - 1)) +1)
             while l<r:
                 mid = l+(r-l)//2
                 sum=0
                 for i in range(size):
                     sum=sum*mid+1
                 if sum==num:
                     return str(mid)
                 elif sum<num:
                     l=mid+1
                 else:
                     r=mid
         return str(num-1)
         
     #           long long num = stol(n);
     #     for (int i = log(num + 1) / log(2); i >= 2; --i) {
     #         long long left = 2, right = pow(num, 1.0 / (i - 1)) + 1;
     #         while (left < right) {
     #             long long mid = left + (right - left) / 2, sum = 0;
     #             for (int j = 0; j < i; ++j) {
     #                 sum = sum * mid + 1;
     #             }
     #             if (sum == num) return to_string(mid);
     #             else if (sum < num) left = mid + 1;
     #             else right = mid;
     #         }
     #     }
     #     return to_string(num - 1);
     # }
         
