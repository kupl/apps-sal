class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def _selection_sort(a):
            for i in range(len(a)):
                m = i
                for j in range(i + 1, len(a)):
                    if a[m] > a[j]:
                        m = j
                a[i], a[m] = a[m], a[i]

        def _bubble_sort(a):
            for i in range(len(a)):
                for j in range(len(a) - 1 - i):
                    if a[j] > a[j + 1]:
                        a[j], a[j + 1] = a[j + 1], a[j]

        def _insertion_sort(a):
            for i in range(1, len(a)):
                v = a[i]
                j = i
                while j > 0 and a[j - 1] > v:
                    a[j] = a[j - 1]
                    j -= 1
                a[j] = v

        def _quick_sort(a, s, e):
            def _partition(a, s, e):
                f = l = s
                while l < e:
                    if a[l] <= a[e]:
                        a[f], a[l] = a[l], a[f]
                        f += 1
                    l += 1
                a[f], a[e] = a[e], a[f]
                return f

            if s < e:
                p = _partition(a, s, e)
                _quick_sort(a, s, e=p - 1)
                _quick_sort(a, s=p + 1, e=e)

        def _merge_sort(a):

            def _merge(a, b):
                result = []
                i = j = 0
                while i < len(a) and j < len(b):
                    if a[i] <= b[j]:
                        result.append(a[i])
                        i += 1
                    else:
                        result.append(b[j])
                        j += 1
                result.extend(a[i:])
                result.extend(b[j:])
                return result

            result = []
            if len(a) <= 1:
                result = a.copy()
                return result

            m = len(a) // 2
            _left = a[:m]
            _right = a[m:]
            _new_left = _merge_sort(_left)
            _new_right = _merge_sort(_right)
            result = merge(_new_left, _new_right)
            return result

        _quick_sort(nums, s=0, e=len(nums) - 1)
        return nums
