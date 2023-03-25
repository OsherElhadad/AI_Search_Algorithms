# Osher Elhadad 318969748


class JunctionNode:

    def __init__(self, state, parent=None, action=None, path_cost=0, step_cost_func=lambda y: y):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.step_cost_func = step_cost_func

    def expand(self, problem):
        return [self.child_junction(problem, action) for action in problem.actions(self.state)]

    def child_junction(self, problem, action):
        next_state = problem.succ(self.state, action)
        next_junction = JunctionNode(next_state, self, action, self.path_cost
                                     + self.step_cost_func(problem.road_distance(self.state, action),
                                                      problem.road_type(self.state, action)), self.step_cost_func)
        return next_junction

    def solution(self):
        return [junction.state for junction in self.path()]

    def path(self):
        junction = self
        reversed_path = []
        while junction is not None:
            reversed_path.append(junction)
            junction = junction.parent
        return list(reversed(reversed_path))

    def __lt__(self, node):
        return self.path_cost < node.path_cost

    def __eq__(self, other):
        return isinstance(other, JunctionNode) and self.state == other.state

    def __ne__(self, other):
        return not (self == other)
