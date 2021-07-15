class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        dic={req_skills[rs]:2**rs for rs in range(len(req_skills))}
        dp=[[] for i in range(2**len(req_skills))]
        m_pp=[]
        for pp in range(len(people)):
            res=0
            for itr_pp in people[pp]:
                res+=dic[itr_pp]
            # print(res, people[pp])
            if res!=0:
                dp[res]=[pp]
            m_pp.append(res)
        # def recur(idx,val,res):
        #     if len(dp[val])==0 or len(dp[val])>len(res):
        #         dp[val]=res
        #     if len(dp[val])<len(res):return
        #     if idx==len(m_pp):return
        #     for i in range(idx,len(m_pp)):
        #         # print(res,[i])
        #         if m_pp[i]==0:continue
        #         recur(i+1,val|m_pp[i],res+[i])
        for i in range(len(m_pp)):
            if m_pp[i]==0:continue
            # print('-------')
            dp[m_pp[i]]=[i]
            for j in range(len(dp)):
                if len(dp[j])>0:
                    sum_=j|m_pp[i]
                    # # if sum_==0:continue
                    # if j==len(dp)-1:
                    #     print(j,m_pp[i],j^sum_)
                    if len(dp[sum_])==0 or len(dp[sum_])>len(dp[j]+[i]):
                            dp[sum_]=dp[j]+[i]
                
#                 # tgt=dp[res|i]
#                 dp[m_pp[j]|m_pp[i]]=list(set(dp[m_pp[j]]+dp[m_pp[i]]))
#                 # if len(tgt)==0 or len(tgt)>len(new):dp[res|i]=new
        # recur(0,0,[])
        # for i in range(len(dp)):
        #     print(i,dp[i])
        # print(dp[-1])
        return dp[-1]

