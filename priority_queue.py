# Osher Elhadad 318969748

import heapq


class PriorityQueue:

    def __init__(self, problem, cost_func=lambda y: y):
        self.heap = []
        self.cost_func = cost_func
        self.problem = problem

    def push(self, item):
        heapq.heappush(self.heap, (self.cost_func(item, self.problem), item))

    def push_items(self, items):
        for item in items:
            self.push(item)

    def pop(self):
        if self.heap:
            return heapq.heappop(self.heap)[1]
        else:
            raise Exception('Cannot pop from empty PriorityQueue')

    def __len__(self):
        return len(self.heap)

    def __contains__(self, key):
        if len([val for val, item in self.heap if item == key]) > 0:
            return True
        return False

    def __getitem__(self, key):
        item = [val for val, item in self.heap if item == key]
        if len(item) == 0:
            raise KeyError(str(key) + " is not in the priority queue")
        return item[0]

    def __delitem__(self, key):
        try:
            del self.heap[[item == key for _, item in self.heap].index(True)]
        except ValueError:
            raise KeyError(str(key) + " is not in the priority queue")
        heapq.heapify(self.heap)
