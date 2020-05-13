Problem : https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/928/

Solution : Python3

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        output = []

        if not root:
            return output

        stack.append(root)

        while stack:
            node = stack.pop()
            output.append(node.val)

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

        return output
```
