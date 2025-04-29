"""Binary Tree Traversal"""


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right


def pre_order(node):
    """Pre-order traversal"""
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
    result = []
    stack = []
    current_node = node

    while stack:
        while current_node:
            stack.append(current_node)
            current_node = current_node.left

        current_node = stack.pop()
        result.append(current_node)
        current_node = current_node.right

    return result


def post_order(node):
    """Post-order traversal"""
    output = []
    current_node = node
    while current_node.left is not None:
        output.append(current_node.left.data)
        current_node = current_node.left
    current_node = node
    while current_node.right is not None:
        output.append(current_node.right.data)
        current_node = current_node.right
    output.append(node.data)
    return output
