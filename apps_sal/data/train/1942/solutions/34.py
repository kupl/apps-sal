class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        frequency_dict = dict()
        word_tracker = dict()
        
        for index, companies in enumerate(favoriteCompanies):
            for company in companies:
                if company not in word_tracker:
                    word_tracker[company] = []
                
                for matched_index in word_tracker[company]:
                    if matched_index not in list(frequency_dict.keys()):
                        frequency_dict[matched_index] = dict()
                    if index not in list(frequency_dict[matched_index].keys()):
                        frequency_dict[matched_index][index] = 0

                    if index not in list(frequency_dict.keys()):
                        frequency_dict[index] = dict()
                    if matched_index not in list(frequency_dict[index].keys()):
                        frequency_dict[index][matched_index] = 0
                        
                    frequency_dict[matched_index][index] += 1
                    frequency_dict[index][matched_index] += 1
                    
                word_tracker[company].append(index)
        
        ret_list = []
        for index, companies in enumerate(favoriteCompanies):
            is_subset = False
            if index in list(frequency_dict.keys()):
                for key in list(frequency_dict[index].keys()):
                    if frequency_dict[index][key] >= len(companies):
                        is_subset = True
                        break
            
            if not(is_subset):
                ret_list.append(index)
        return ret_list
        

