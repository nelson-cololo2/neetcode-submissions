class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        # If subRoot is empty, it's always a subtree
        if not subRoot:
            return True
        
        # If root is empty but subRoot isn't, impossible
        if not root:
            return False
        
        # Check if trees match at this node
        if isSameTree(root, subRoot):
            return True
        
        # Otherwise search left or right subtree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
