class Solution:
     def findShortestSubArray(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         r={}
         for i,j in enumerate(nums):
             if j not in r:
                 r[j]=1+100000*i
             else:
                 r[j]=r[j]%10000000000+1+10000000000*i
         tem=1
         dist=500000
         print(r)
         for i in list(r.values()):
             print(i)
             if i%100000==tem:
                 if tem==1:
                     dist=1
                 else:
                     dist_tem=i//10000000000-(i//100000)%100000+1
                     if dist_tem<dist:
                         dist=dist_tem
             elif i%100000>tem:
                 tem=i%100000
                 dist=i//10000000000-(i//100000)%100000+1
         return dist
             
                 
        #  x=[0 for i in range(50000)]
        #  for i in range(len(nums)):
        #      x[nums[i]]=x[nums[i]]+1
        #      if x[nums[i]]==1:
        #          x[nums[i]]=x[nums[i]]+100000*i
        #      else:
        #          x[nums[i]]=x[nums[i]]%10000000000+10000000000*i
        #  tem=1
        # # print(x)
        #  dist=50000
        #  for i in x:
        #     # print(i)
        #      if i>0:
        #          if i%100000==tem:
        #              tem=i%100000
        #              if tem==1:
        #                  dist=1
        #              else:
        #                  dist_tem=i//10000000000-(i//100000)%100000+1
        #                  if dist_tem<dist:
        #                      dist=dist_tem
        #          elif i%100000>tem:
        #              tem=i%100000
        #              dist=i//10000000000-(i//100000)%100000+1
        #         # print(dist)
        #  return dist
     
             

