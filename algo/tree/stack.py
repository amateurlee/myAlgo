# -*- coding: utf-8 -*-
# !/env/python
# @auther: mjli
# @date: 20180623

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.isEmpty():
            raise Exception("stack is empty")
        else:
            self.stack.pop()

    def isEmpty(self):
        return len(self.stack) <= 0

    def listStack(self):
        return self.stack


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    print s.listStack()
    s.pop()
    print s.listStack()
    s.pop()
    print s.listStack()
    if not s.isEmpty():
        s.pop()