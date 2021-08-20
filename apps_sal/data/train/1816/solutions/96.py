def time_to_min(etime):
    (hours, minutes) = etime.split(':')
    return int(hours) * 60 + int(minutes)


def add_time_sorted(etime, time_list):
    ii = 0
    while ii < len(time_list) and time_to_min(etime) > time_to_min(time_list[ii]):
        ii += 1
    time_list.insert(ii, etime)


def add_name_sorted(name, alert_list):
    ii = 0
    while ii < len(alert_list) and name > alert_list[ii]:
        ii += 1
    alert_list.insert(ii, name)


def check_for_alert(time_list):
    if len(time_list) <= 2:
        return False
    else:
        delta = []
        for ii in range(0, len(time_list) - 1):
            first_time = time_to_min(time_list[ii])
            second_time = time_to_min(time_list[ii + 1])
            delta.append(second_time - first_time)
            if len(delta) > 1:
                if delta[ii] + delta[ii - 1] <= 60:
                    return True
        return False


class Solution:

    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        entry = {}
        alert = []
        for ii in range(0, len(keyName)):
            name = keyName[ii]
            etime = keyTime[ii]
            if name not in alert:
                if name not in entry:
                    entry[name] = [etime]
                else:
                    add_time_sorted(etime, entry[name])
                    if check_for_alert(entry[name]):
                        add_name_sorted(name, alert)
        return alert
