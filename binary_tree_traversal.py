"""Binary Tree Traversal"""


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right


def pre_order(node):
    """Pre-order traversal"""
    if node is None:
        return []

    result = []
    stack = [node]

    while stack:
        current_node = stack.pop()
        result.append(current_node.data)

        if current_node.right:
            stack.append(current_node.right)
        if current_node.left:
            stack.append(current_node.left)

    return result


def in_order(node):
    """In-order traversal"""
    if node is None:
        return []

    result = []
    stack = []
    current_node = node

    while stack or current_node:
        while current_node:
            stack.append(current_node)
            current_node = current_node.left

        current_node = stack.pop()
        result.append(current_node.data)
        current_node = current_node.right

    return result


def post_order(node):
    """Post-order traversal"""
    if node is None:
        return []

    stack1 = [node]
    stack2 = []
    result = []

    while stack1:
        node = stack1.pop()
        stack2.append(node)

        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)

    while stack2:
        result.append(stack2.pop().data)

    return result
