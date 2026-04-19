# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:

            if not root.left:
                return root.right

            if not root.right:
                return root.left

            next_node = root.right
            while next_node.left:
                next_node = next_node.left

            root.val = next_node.val
            root.right = self.deleteNode(root.right, next_node.val) 

        return root
