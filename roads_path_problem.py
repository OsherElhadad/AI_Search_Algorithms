# Osher Elhadad 318969748

class RoadsPathProblem:

    def __init__(self, start, goal, roads):
        self.start = start
        self.goal = goal
        self.roads = roads

    def actions(self, junction):
        return [link.target for link in self.roads[junction].links]

    def succ(self, junction_a, junction_b):
        if junction_b in self.actions(junction_a):
            return junction_b
        return None

    def is_goal(self, junction):
        return junction == self.goal

    def get_junction_and_goal_location(self, junction):
        return self.roads[junction].lat, self.roads[junction].lon, self.roads[self.goal].lat, self.roads[self.goal].lon

    def road_distance(self, from_junction, to_junction):
        distance = [link.distance for link in self.roads[from_junction].links if link.target == to_junction]
        if len(distance) == 0:
            return None
        return distance[0]

    def road_type(self, from_junction, to_junction):
        r_type = [link.highway_type for link in self.roads[from_junction].links if link.target == to_junction]
        if len(r_type) == 0:
            return None
        return r_type[0]
