# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        result = []
        q = queue.Queue()
        
        if not root:
            return None
        
        q.put(root)
        
        while not q.empty():
            a = []
            size = q.qsize()
            
            while size != 0:
                current = q.get()
                a.append(current.val)
                
                if current.left:
                    q.put(current.left)
                
                if current.right:
                    q.put(current.right)
                
                size -= 1
            
            if len(a) != 0:
                result.append(a)
        
        return result