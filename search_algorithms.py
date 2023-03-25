# Osher Elhadad 318969748

import junction_node as jn
import priority_queue as pq
import utils
from ways import tools


def graph_search(start_node, problem, f=lambda y: y):
    frontier = pq.PriorityQueue(problem, f)
    frontier.push(start_node)
    closed_list = set()
    while frontier:
        j_node = frontier.pop()
        if problem.is_goal(j_node.state):
            return j_node.solution(), f(j_node, problem)
        closed_list.add(j_node.state)
        for child in j_node.expand(problem):
            if child.state not in closed_list and child not in frontier:
                frontier.push(child)
            elif child in frontier:
                if f(child, problem) < frontier[child]:
                    del frontier[child]
                    frontier.push(child)
    return None, 0


def dfs_f(j_node, problem, f_limit, f=lambda y: y):
    new_limit = f(j_node, problem)
    if new_limit > f_limit:
        return new_limit, None, False
    if problem.is_goal(j_node.state):
        return new_limit, j_node, True
    min_next_f_limit = float("inf")
    for child in j_node.expand(problem):
        new_limit, goal, finish = dfs_f(child, problem, f_limit, f)
        if finish:
            return new_limit, goal, finish
        elif new_limit < min_next_f_limit:
            min_next_f_limit = new_limit
    return min_next_f_limit, j_node, False


def ida_star(problem, f=lambda y: y):
    start_node = jn.JunctionNode(problem.start, step_cost_func=utils.time_cost)
    f_limit = f(start_node, problem)
    while True:
        new_limit, goal, finish = dfs_f(start_node, problem, f_limit, f)
        if finish:
            return goal.solution(), f(goal, problem)
        if new_limit == float("inf"):
            return None, 0
        f_limit = new_limit
