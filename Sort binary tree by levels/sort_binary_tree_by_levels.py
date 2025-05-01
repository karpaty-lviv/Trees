"""Sort binary tree by levels"""


class Node:
    def __init__(self, left, right, val):
        self.value = val
        self.left = left
        self.right = right


def tree_by_levels(node):
    """Sort tree by levels"""
    if node is None:
        return []
    result = []
    stack = [node]
    for nod in stack:
        if nod.left is not None:
            stack.append(nod.left)
        if nod.right is not None:  
            stack.append(nod.right)
    while stack:
        result.append(stack.pop(0).value)
    return result

print(tree_by_levels(Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1)))