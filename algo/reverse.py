# -*- coding: utf-8 -*-
# !/env/python

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse(head):
    if head == None or head.next == None:
        return head
    cur = head
    after = None
    while cur != None:
        pre = cur.next
        cur.next = after
        after = cur
        cur = pre
    return after


def init():
    head = Node(0)
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    head.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    return head


def printLink(head):
    if head != None and head.next != None:
        p = head
        while p:
            if p.next is None:
                array = ""
            else:
                array = "-->"
            print("{}{}".format(p.data, array)),
            p = p.next
        print("")


if __name__ == "__main__":
    head = init()
    printLink(head)
    newhead = reverse(head)
    printLink(newhead)
