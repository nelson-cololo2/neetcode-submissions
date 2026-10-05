# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = None

        def inorder(node):
            nonlocal prev
            if not node:
                return True
            
            # Left subtree
            if not inorder(node.left):
                return False
            
            # Current node
            if prev is not None and node.val <= prev:
                return False
            prev = node.val

            # Right subtree
            return inorder(node.right)

        return inorder(root)