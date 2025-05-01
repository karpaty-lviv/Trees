"""Delete Node in a BST"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root, key: int):
        if root is None:
            return root
        current_node = root
        prev_node = None
        direction = ''
        if key == root.val:
            if current_node.right is None:
                return current_node.left
            current_node = current_node.right
            new_root = current_node
            while current_node.left is not None:
                current_node = current_node.left
            current_node.left = root.left
            return new_root
        while current_node.val != key:
            if root.val == key:
                break
            if current_node.val > key:
                prev_node = current_node
                direction = 'left'
                current_node = current_node.left
            else:
                prev_node = current_node
                direction = 'right'
                current_node = current_node.right
            if current_node is None:
                return root
        if direction == 'left':
            temp_node = current_node
            if current_node is None:
                return root
            if current_node.right is not None:
                prev_node.left = current_node.right
                current_node = current_node.right
            else:
                prev_node.left = current_node.left
                return root
            if current_node is None:
                return root
            while current_node.left is not None:
                current_node = current_node.left
            current_node.left = temp_node.left
            return root
        if direction == 'right':
            temp_node = current_node
            if current_node is None:
                return root
            prev_node.right = current_node.right
            current_node = current_node.right
            if current_node is None:
                prev_node.right = temp_node.left
                return root
            while current_node.left is not None:
                current_node = current_node.left
            current_node.left = temp_node.left
            return root
