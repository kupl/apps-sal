# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    '''
    Algo:
    Iterate through the tree and restore the values of each node
    Add the node to a stack
        - with height of root
        - left or right info
            - left = 0, right = 1
            - (node, root_height, isRight)
    Iterate through the stack and calculate the value for the node
    using val = 2 * root_height + (1 + isRight)
    
    After nodes are fixed then iterate through the tree to find the node
    by adding all nodes to a stack
    '''

    def __init__(self, root: TreeNode):
        self.root = root
        node_list = []
        self.val_list = []
        if root:
            root.val = 0
            self.val_list.append(root.val)
            node_list.append((root.left, 0, 0))
            node_list.append((root.right, 0, 1))
            while len(node_list) > 0:
                cur_node, root_val, isRight = node_list.pop(-1)
                if cur_node:
                    print(f\"root_val: {root_val}, isRight: {isRight}\")
                    cur_node.val = 2 * root_val + (1 + isRight)
                    self.val_list.append(cur_node.val)
                    node_list.append((cur_node.left, cur_node.val,
                                     0))
                    node_list.append((cur_node.right, cur_node.val,
                                     1))
        

    def find(self, target: int) -> bool:
        # def dfs(node, val_list):
        #     if node:
        #         dfs(node.left, val_list)
        #         val_list.append(node.val)
        #         dfs(node.right, val_list)
        # val_list = []
        # dfs(self.root, val_list)
        # print(val_list)
        return target in self.val_list
                
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
