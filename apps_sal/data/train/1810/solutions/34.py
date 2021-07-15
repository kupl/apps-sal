class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        name_times = {}
        used_names = set()
        result = []
        for name in names:
            # first time file
            if name not in used_names:
                result.append(name)
                used_names.add(name)
                name_times[name] = 1
            else:
                index = name_times[name]
                rename = name + \"(\" + str(index) + \")\"
                while rename in used_names:
                    index += 1
                    rename=name + \"(\" + str(index) + \")\"
                name_times[name] = index
                used_names.add(rename)
                name_times[rename] = 1
                result.append(rename)
        return result
    
#     public String[] getFolderNames(String[] names) {
#     Map<String,Integer> map=new HashMap<>(); // 记录每种文件名出现的次数
#     Set<String> set=new HashSet<>(); // 记录所有出现过的显示名称
#     String[] res = new String[names.length]; // 返回结果
#     for(int i=0;i<names.length;i++){ // 循环每一个文件名
#         String name = names[i]; // 当前文件名
#         if(!set.contains(name)){ // 当前文件名首次出现
#             res[i]=name; // 直接使用当前文件名
#             set.add(name); // 将文件名加入set
#             map.put(name,1); // 记录当前文件名出现次数为1
#         }else{ // 当前文件名已经出现过
#             int index=map.get(name); // 查看当前文件名出现过的次数
#             String rename=name+\"(\"+index+\")\"; // 组成新的显示名称
#             while(set.contains(rename)){ // 如果新的显示名称仍出现过
#                 index++; // 出现次数加一
#                 rename=name+\"(\"+index+\")\"; // 更新显示名称
#             }
#             map.put(name,index); // 更新该文件名出现次数
#             set.add(rename); // 将新的显示名称加入set
#             map.put(rename,1); // 记录新的显示名称出现次数为1
#             res[i]=rename; // 当前返回结果为该新的显示名称
#         }
#     }
#     return res;
# }
                
