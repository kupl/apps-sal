class Solution:
    ## since mine always has bug and I can not find the reason so I just checked other people solution.
    
    ## general point is the similar to mine but much easier and has less unnecessary consideration
    # 1. no need to check what is his children, since my map always going to have the childrean
    
    def getFolderNames(self, names: List[str]) -> List[str]:
        folder = {} # name to next int
        res = []
        for name in names:
            if name not in folder:
                folder[name] = 1
                res.append(name)
            else:
                current_number = folder[name]
                new_folder_name = name + \"(\" + str(current_number) + \")\"
                while  new_folder_name in folder:
                    current_number += 1
                    new_folder_name = name + \"(\" + str(current_number) + \")\"
                res.append(new_folder_name)
                folder[new_folder_name] = 1
                folder[name] = current_number + 1
        return res
#     def getFolderNames(self, names: List[str]) -> List[str]:
#         # prepare a folder map:{name: (has_built_name, next_index, set(children))}
#         # when a new folder name entered, first check if you already has this created
#         # for each folder name: you need maintian its next interger
        
#         folder = {}
#         res = []
#         new_name = \"\"
#         for name in names:
#             print(name)
#             if name not in folder:
#                 new_name = name
#                 #res.append(name)
#                 print(\"1-\")
#                 # update parent
#                 # check if this name's parent is in foler:
#                 if self.has_parent(name):
#                     splitted = name.rsplit(\"(\", 1)
#                     parent_name = splitted[0]
#                     cur_child = int(splitted[1].rsplit(\")\", 1)[0])
#                     if parent_name not in folder:
#                         print(\"11-\")
#                         folder[parent_name] = [False, 1, set(cur_child)]
#                         # update next index
#                         self.update_next_index(folder, parent_name)
#                     else:
#                         print(\"12-\")
#                         # update parent info
#                         ## update children for this parent:
#                         folder[parent_name][2].add(cur_child)
#                         # update next index
#                         self.update_next_index(folder, parent_name)
          
#             else:
#                 print(\"2-\")
#                 if not folder[name][0]:
#                     print(\"21-\")
#                     folder[name][0] = True
#                     new_name = name
#                     #res.append(name)
#                 else:
#                     print(\"22-\")
#                     cur_index = folder[name][1]
#                     new_name = name + \"(\" + str(cur_index) + \")\"
#                     #res.append(name)
#                     #res.append(name + \"(\" + str(cur_index) + \")\")
#                     folder[name][2].add(cur_index)
#                     folder[name][1] += 1
#                     # update next index
#                     self.update_next_index(folder, name)
            
#             #
#             res.append(new_name)
#             folder[new_name] = [True, 1, set()] # the first is the next integer can try, second is the subffix it has so far
#         return res
                
#     def update_next_index(self, folder, parent_name):
#         next_int = folder[parent_name][1]
#         while next_int in folder[parent_name][2]:
#                 next_int += 1
#         folder[parent_name][1] = next_int
#         # 
                
#     def has_parent(self, name):
#         return True if \"(\" in name and name.rsplit(\"(\", 1)[1][0] != '0'  else False
