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
    
