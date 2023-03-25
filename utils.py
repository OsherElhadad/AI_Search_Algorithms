# Osher Elhadad 318969748

import random
import main
from ways import load_map_from_csv, draw
from ways import info
from ways import tools
import roads_path_problem as prob
import junction_node as jn
import search_algorithms as sa


def g(junction_node, problem):
    return junction_node.path_cost


def h(junction_node, problem):
    lat1, lon1, lat2, lon2 = problem.get_junction_and_goal_location(junction_node.state)
    return main.huristic_function(lat1, lon1, lat2, lon2)


def g_and_h_cost(current_junction, problem):
    return g(current_junction, problem) + h(current_junction, problem)


def get_air_time(lat1, lon1, lat2, lon2):
    return tools.compute_distance(lat1, lon1, lat2, lon2)/110


def get_junctions_from_csv():
    return load_map_from_csv()


def time_cost(dis, road_type):
    return (dis/1000)/(info.SPEED_RANGES[road_type][1])


def find_ucs_rout_with_roads(source, target, roads):
    f = g
    problem = prob.RoadsPathProblem(source, target, roads)
    start_node = jn.JunctionNode(problem.start, step_cost_func=time_cost)
    return sa.graph_search(start_node, problem, f)


def find_astar_route_with_roads(source, target, roads):
    f = g_and_h_cost
    problem = prob.RoadsPathProblem(source, target, roads)
    start_node = jn.JunctionNode(problem.start, step_cost_func=time_cost)
    path, time = sa.graph_search(start_node, problem, f)
    return path, time, h(start_node, problem)


def find_idastar_route_with_roads(source, target, roads):
    f = g_and_h_cost
    problem = prob.RoadsPathProblem(source, target, roads)
    return sa.ida_star(problem, f)


def draw_IDAStar_10_examples():
    roads = load_map_from_csv()
    with open('problems.csv', 'r') as problems_file:
        lines = problems_file.readlines()

    rand_indexes = [5, 14, 17, 36, 47, 51, 59, 73, 82, 89]
    for i in rand_indexes:
        junctions = lines[i].split(',')
        if len(junctions) != 2:
            continue
        path, time = find_idastar_route_with_roads(int(junctions[0]), int(junctions[1]), roads)
        if path is None:
            continue
        draw.plot_path(roads, path)


def draw_IDAStar_fixed_10_examples():
    roads = load_map_from_csv()

    lines = ['261410,261419', '806087,806097', '122393,122413', '369012,369018', '59457,59451',
             '291494,291498', '292890,292895', '757669,757675', '459731,459739', '546072,546078']
    for line in lines:
        junctions = line.split(',')
        if len(junctions) != 2:
            continue
        path, time = find_idastar_route_with_roads(int(junctions[0]), int(junctions[1]), roads)
        if path is None:
            continue
        draw.plot_path(roads, path)


def run_by_search_func(roads, junctions, search_func):
    if search_func == 1:
        path, time = find_ucs_rout_with_roads(int(junctions[0]), int(junctions[1]), roads)
        if path is None:
            return
    elif search_func == 2:
        path, time, heuristic = find_astar_route_with_roads(int(junctions[0]), int(junctions[1]), roads)
        if path is None:
            return
    elif search_func == 3:
        path, time = find_idastar_route_with_roads(int(junctions[0]), int(junctions[1]), roads)
        if path is None:
            return


@tools.timed
def run_10_fixed_examples_with_roads(roads, search_func):
    lines = ['261410,261419', '806087,806097', '122393,122413', '369012,369018', '59457,59451',
             '291494,291498', '292890,292895', '757669,757675', '459731,459739', '546072,546078']
    for line in lines:
        junctions = line.split(',')
        if len(junctions) != 2:
            continue
        run_by_search_func(roads, junctions, search_func)


def run_10_fixed_examples(search_func):
    roads = load_map_from_csv()
    run_10_fixed_examples_with_roads(roads, search_func)


@tools.timed
def run_10_examples_with_roads(roads, search_func):
    with open('problems.csv', 'r') as problems_file:
        lines = problems_file.readlines()

    rand_indexes = [5, 14, 17, 36, 47, 51, 59, 73, 82, 89]
    for i in rand_indexes:
        junctions = lines[i].split(',')
        if len(junctions) != 2:
            continue
        run_by_search_func(roads, junctions, search_func)


def run_10_examples(search_func):
    roads = load_map_from_csv()
    run_10_examples_with_roads(roads, search_func)


def run_examples(out_file, search_func):
    roads = load_map_from_csv()
    with open('problems.csv', 'r') as problems_file:
        lines = problems_file.readlines()

    results = []
    for line in lines:
        junctions = line.split(',')
        if len(junctions) != 2:
            continue
        if search_func == 1:
            path, time = find_ucs_rout_with_roads(int(junctions[0]), int(junctions[1]), roads)
            if path is None:
                continue
            results.append(' '.join(str(j) for j in path) + '-' + str(float("{:.4f}".format(time))))
        elif search_func == 2:
            path, time, heuristic = find_astar_route_with_roads(int(junctions[0]), int(junctions[1]), roads)
            if path is None:
                continue
            results.append(' '.join(str(j) for j in path) + '-' + str(float("{:.4f}".format(time)))
                           + "-" + str(float("{:.4f}".format(heuristic))))

    with open(out_file, 'w') as f:
        f.write('\n'.join(results))


def create_problems_csv():
    roads_map = load_map_from_csv()
    rows = []
    for _ in range(100):
        start_junction = roads_map[random.randint(0, len(roads_map) - 1)]
        while len(start_junction.links) == 0:
            start_junction = roads_map[random.randint(0, len(roads_map) - 1)]
        max_depth = random.randint(200, 250)
        last_junction = start_junction
        for _ in range(max_depth):
            links = last_junction.links
            if len(links) == 0:
                break
            last_junction = roads_map[links[random.randint(0, len(links) - 1)].target]
            while start_junction.index == last_junction.index and len(links) > 1:
                last_junction = roads_map[links[random.randint(0, len(links) - 1)].target]
        rows.append(str(start_junction.index) + ',' + str(last_junction.index))
    with open('problems.csv', 'w') as problems_file:
        problems_file.write('\n'.join(rows))

