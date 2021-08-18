numerals = {
    "0": "零",
    "1": "一",
    "2": "二",
    "3": "三",
    "4": "四",
    "5": "五",
    "6": "六",
    "7": "七",
    "8": "八",
    "9": "九",
}


def to_chinese_numeral(n):
    tempdivide = 10000
    allweishu = []
    allxiaoshu = []
    n = str(n)
    if("-" in n):
        allweishu.append("负")
        n = n[1:]
    else:
        allweishu.append("")
    if("." in n):
        tempxiaoshu = n.split(".")[1]
        n = n.split(".")[0]
        for xiaoshu in tempxiaoshu:
            allxiaoshu.append(numerals[xiaoshu])
    n = int(n)
    while(tempdivide != 0.1):
        weishu = str(int(n // tempdivide))
        n = n % tempdivide
        allweishu.append(numerals[weishu])
        tempdivide = tempdivide / 10
    start = 0
    nums = ["万", "千", '百', '十', '']
    allstrs = allweishu[0]
    for weishu in range(len(allweishu[1:])):
        if(start == 1 and allweishu[weishu + 1] == "零" and nums[weishu] != "" and allstrs[-1] != "零"):
            allstrs += "零"
        elif(allweishu[weishu + 1] != "零"):

            start = 1
            if(nums[weishu] == "十" and allweishu[weishu + 1] == "一"):
                if((allstrs == "" or allstrs == "负")):
                    allstrs += "十"
                elif(allweishu[-1] == "零"):
                    allstrs += "一十"
                elif((allstrs == "" or allstrs == "负") and allweishu[-1] == "零"):
                    allstrs += "十"
                else:
                    allstrs += "一十"

            else:
                allstrs += allweishu[weishu + 1]
                allstrs += nums[weishu]
        elif(allweishu[weishu + 1] == "零" and nums[weishu] == ""):
            continue

    if(len(allstrs) > 1 and allstrs[-1] == "零"):
        allstrs = allstrs[:-1]
    if(allstrs == "负" or allstrs == ""):
        allstrs += "零"
    if(allxiaoshu):
        allstrs += "点"
        for i in allxiaoshu:
            allstrs += i
    if(allstrs == ""):
        return "零"
    if(allstrs[-1] == "零" and len(allstrs) > 1):
        return allstrs[:-1]
    return allstrs
