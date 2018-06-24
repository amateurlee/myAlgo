# -*- coding: utf-8 -*-
# !/env/python
# @auther: mjli
# @date:

class Graph:
    def __init__(self):
        self.graph = {
            'A': ['B', 'C'],
            'B': ['C', 'D'],
            'C': 'D',
            'D': 'C',
            'E': ['F'],
            'F': ['C']
        }

    def find_all_paths(self, start, end, paths=[]):
        '''
        find all paths from node start to node end
        :param node:
        :return:
        '''
        path = paths + [start]

        if start == end:
            return start

        for node in self.graph[start]:
            pathtmp = self.find_all_paths(node, end, path)
            if pathtmp:
                path.append(pathtmp)
                #TODO: add graph traverse


if __name__=='__main__':
    graph = Graph()
    path = []
    pathret = []
    pathret = graph.find_all_paths('E', 'F', path)
    print "path:{}".format(path)
    print "pathret:{}".format(pathret)
