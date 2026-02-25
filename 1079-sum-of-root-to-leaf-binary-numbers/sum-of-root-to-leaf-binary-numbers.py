# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        total = 0
        def solve(root, curSum):
            nonlocal total
            if not root.left and (not root.right):
                curSum *= 2
                curSum += 1 if root.val == 1 else 0
                total += curSum
                return 
            curSum *= 2
            curSum += 1 if root.val == 1 else 0
            if root.left:
                solve(root.left, curSum)
            if root.right:
                solve(root.right, curSum)

        solve(root, 0)
        return total