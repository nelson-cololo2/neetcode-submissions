# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Map each value to its index in inorder for o(1) splits
        index_map = {value: i for i, value in enumerate(inorder)}

        # Pointer to current root in preorder
        self.pre_idx = 0

        def build(left, right):
            # No nodes in this subtree
            if left > right:
                return None
            
            # Root is the next element in preorder
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)

            # Split inorder into left/right subtrees
            mid = index_map[root_val]

            # Build left subtree
            root.left = build(left, mid - 1)

            # Build right subtree
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)