class Solution:

    def avoidFlood(self, rains: List[int]) -> List[int]:
        rains_over_city = {}
        lake_drying_days = []
        ind = 0
        for rain in rains:
            if rain > 0:
                rain_index = rains_over_city.get(rain, -1)
                if rain_index != -1:
                    len_lak = len(lake_drying_days)
                    j = 0
                    while j < len_lak and lake_drying_days[j] <= rain_index:
                        j += 1
                    if j >= len_lak:
                        return []
                    rains[lake_drying_days[j]] = rain
                    lake_drying_days.remove(lake_drying_days[j])
                    rains_over_city.pop(rain)
                rains_over_city[rain] = ind
                rains[ind] = -1
            else:
                lake_drying_days.append(ind)
                rains[ind] = 1
            ind += 1
        return rains
