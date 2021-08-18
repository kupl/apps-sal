class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        stack = []

        from collections import defaultdict
        data_dict = defaultdict(list)

        for index in range(0, len(s)):
            char = s[index]

            if char == '(':
                data_dict['('].append(index)
                stack.append('(')

            if char == ')':
                if '(' in stack:
                    stack.pop()
                    data_dict['('].pop()
                else:
                    stack.append(')')
                    data_dict[')'].append(index)

        s_list = list(s)

        for char in stack:
            parentheses_index_list = data_dict[char]
            remove_char_index = parentheses_index_list.pop()
            s_list.pop(remove_char_index)

            if char == '(':
                parentheses_index_list = data_dict[')']
                for index in range(0, len(parentheses_index_list)):
                    position_in_s = parentheses_index_list[index]
                    if position_in_s > remove_char_index:
                        position_in_s -= 1
                        parentheses_index_list[index] = position_in_s
            else:
                parentheses_index_list = data_dict['(']
                for index in range(0, len(parentheses_index_list)):
                    position_in_s = parentheses_index_list[index]
                    if position_in_s > remove_char_index:
                        position_in_s -= 1
                        parentheses_index_list[index] = position_in_s

        return_s = ''
        for char in s_list:
            return_s += char

        return return_s
