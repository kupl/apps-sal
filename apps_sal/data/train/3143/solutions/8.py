def sort_by_name(arr):
    num_dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'therteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 0: 'zero', -1: '', -10: ''}
    raw_list = []
    for i in arr:
        if i in num_dict:
            raw_list.append(tuple([num_dict[i], i]))
        else:
            raw_i = str(i)
            nums = len(raw_i)
            if nums == 2:
                j = int(raw_i[1])
                if 10 < i < 20:
                    raw_list.append(tuple([num_dict[i], i]))
                    continue
                if j != 0:
                    raw_list.append(tuple(['{} {}'.format(num_dict[int(raw_i[0]) * 10], num_dict[int(raw_i[1])]), i]))
                    continue
                else:
                    raw_list.append(tuple(['{}'.format(num_dict[int(raw_i[0]) * 10]), i]))
                    continue
            else:
                z = int(raw_i[1])
                k = int(raw_i[2])
                if z == 0:
                    z = -1
                if k == 0:
                    k = -1
                if 10 < int(raw_i[1] + raw_i[2]) < 20:
                    raw_list.append(tuple(['{} hundred {}'.format(num_dict[int(raw_i[0])], num_dict[int(raw_i[1] + raw_i[2])]).replace('  ', ' '), i]))
                    continue
                raw_list.append(tuple(['{} hundred {} {}'.format(num_dict[int(raw_i[0])], num_dict[z * 10], num_dict[k]).replace('  ', ' '), i]))
    raw_list.sort(key=lambda x: x[0])
    out_list = []
    for i in raw_list:
        out_list.append(i[1])
    return out_list
