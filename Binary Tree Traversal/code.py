# Pre-order traversal
def pre_order(node):
    res = []
    if node:
        res.append(node.data)
        res.extend(pre_order(node.left))
        res.extend(pre_order(node.right))
    return res

# In-order traversal
def in_order(node):
    res = []
    if node:
        res.extend(in_order(node.left))
        res.append(node.data)
        res.extend(in_order(node.right))
    return res

# Post-order traversal
def post_order(node):
    res = []
    if node:
        res.extend(post_order(node.left))
        res.extend(post_order(node.right))
        res.append(node.data)
    return res
