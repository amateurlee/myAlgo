# -*- coding: utf-8 -*-
# !/env/python
# @auther: mjli
# @date:
class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Traverse:
    def __init__(self):
        self.root = self.buildTree();

    '''
          A
        |   |
       B     C
      | |   | |
      D E   F G
     
    preorder:
           A 1
         |   |
        B 2  C 3
    midorder:
           A 2
         |   |
        B 1  C 3
    midorder:
           A 3
         |   |
        B 1  C 2
          
    '''

    def buildTree(self):
        nodeD = Node("D")
        nodeE = Node("E")
        nodeF = Node("F")
        nodeG = Node("G")
        nodeB = Node("B", nodeD, nodeE)
        nodeC = Node("C", nodeF, nodeG)
        nodeA = Node("A", nodeB, nodeC)
        return nodeA

    def preorder_traverse(self, tree):
        if tree == None:
            return
        else:
            print(tree.data)
            self.preorder_traverse(tree.left)
            self.preorder_traverse(tree.right)

    def midorder_traverse(self, tree):

        if tree == None:
            return
        else:
            self.midorder_traverse(tree.left)
            print(tree.data)
            self.midorder_traverse(tree.right)

    def afterorder_traverse(self, tree):

        if tree == None:
            return
        else:
            self.afterorder_traverse(tree.left)
            self.afterorder_traverse(tree.right)
            print(tree.data)

if __name__ == '__main__':
    traverse = Traverse()
    print("Preorder traverse")
    traverse.preorder_traverse(traverse.root)
    print("Midorder traverse")
    traverse.midorder_traverse(traverse.root)
    print("Afterorder traverse")
    traverse.afterorder_traverse(traverse.root)
