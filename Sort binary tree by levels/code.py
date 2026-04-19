from collections import deque

def tree_by_levels(node):
    if not node:
        return []
    
    res = []
    queue = deque([node])
    
    while queue:
        curr = queue.popleft()
        res.append(curr.value)
        
        if curr.left:
            queue.append(curr.left)
            
        if curr.right:
            queue.append(curr.right)
            
    return res
