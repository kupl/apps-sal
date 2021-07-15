import time
def pack_bagpack(scores, weights, capacity):
    """
    求最大分数
    :param scores:   行李评分列表
    :param weights:  行李重量列表
    :param capacity: 限制重量
    :return: 最大分数

    1）按照均分倒序排列
    2) 递归组合
        max_value = max(包含自己的最大值, 跳过自己的最大值)
    3) 得出最优
    """
    start_time = time.time()
    # 组合
    lst = list(zip(scores, weights))

    # 1) 倒序排列 >> 均分 = 分数/重量
    lst_sorted = sorted(lst, key=lambda x: x[0], reverse=True)

    cache_dict = {}

    def calc_item(index, weight_last):
        if index >= len(lst_sorted) or weight_last <= 0:
            return 0
        current = lst_sorted[index]

        cache_key = "{}-{}".format(index, weight_last)

        if cache_key not in cache_dict:
            # 算上当前的最大结果
            score_with_current = 0
            if weight_last >= current[1]:
                score_with_current = current[0] + calc_item(index + 1, weight_last - current[1])
            # 跳过当前的最大结果
            score_no_current = calc_item(index + 1, weight_last)

            # 缓存当前的位置和剩余重量的值, 让以后的递归不再重复计算类似结果
            cache_dict[cache_key] = max(score_with_current, score_no_current)
            
        return cache_dict[cache_key]

    final_score = calc_item(0, capacity)

    print("score: {}  duration---> {}".format(final_score,time.time() - start_time))
    # 3) 得出最优
    return final_score
