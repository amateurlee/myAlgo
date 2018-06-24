# -*- coding: utf-8 -*-
# !/env/python
# @auther: mjli
# @date:


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class ReverseTree:
    '''
        二叉树的镜像
    '''
    def __init__(self):
        self.root = self.buildTree();

    '''
          A
        |   |
       B     C
      | |   | |
      D E   F G
    after reverse:
    
          A
        |   |
       C     B
      | |   | |
      G F   E D
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

    def reverseTree(self, tree):
        if tree == None:
            return
        else:
            tree.left, tree.right = tree.right, tree.left
            self.reverseTree(tree.left)
            self.reverseTree(tree.right)

    def preorder_traverse(self, tree):
        if tree == None:
            return
        else:
            print(tree.data)
            self.preorder_traverse(tree.left)
            self.preorder_traverse(tree.right)

if __name__=='__main__':
    re = ReverseTree()
    re.preorder_traverse(re.root)
    re.reverseTree(re.root)
    print ("after reverse")
    re.preorder_traverse(re.root)
