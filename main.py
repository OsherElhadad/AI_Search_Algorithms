# Osher Elhadad 318969748
'''
Parse input and run appropriate code.
Don't use this file for the actual work; only minimal code should be here.
We just parse input and call methods from other modules.
'''

import utils
import roads_path_problem as prob
import junction_node as jn
import search_algorithms as sa


#do NOT import ways. This should be done from other files
#simply import your modules and call the appropriate functions

def huristic_function(lat1, lon1, lat2, lon2):
    'Question number 7- huristic_function'
    return utils.get_air_time(lat1, lon1, lat2, lon2)


def find_ucs_rout(source, target):
    'Question number 4- find_ucs_rout'
    roads = utils.get_junctions_from_csv()
    f = utils.g
    problem = prob.RoadsPathProblem(source, target, roads)
    start_node = jn.JunctionNode(problem.start, step_cost_func=utils.time_cost)
    path, _ = sa.graph_search(start_node, problem, f)
    return path


def find_astar_route(source, target):
    'Question number 6- find_astar_route'
    roads = utils.get_junctions_from_csv()
    f = utils.g_and_h_cost
    problem = prob.RoadsPathProblem(source, target, roads)
    start_node = jn.JunctionNode(problem.start, step_cost_func=utils.time_cost)
    path, _ = sa.graph_search(start_node, problem, f)
    return path


def find_idastar_route(source, target):
    'Question number 11- find_astar_route'
    roads = utils.get_junctions_from_csv()
    f = utils.g_and_h_cost
    problem = prob.RoadsPathProblem(source, target, roads)
    path, _ = sa.ida_star(problem, f)
    return path
    

def dispatch(argv):
    from sys import argv
    source, target = int(argv[2]), int(argv[3])
    path = None
    if argv[1] == 'ucs':
        path = find_ucs_rout(source, target)
    elif argv[1] == 'astar':
        path = find_astar_route(source, target)
    elif argv[1] == 'idastar':
        path = find_idastar_route(source, target)
    if path:
        print(' '.join(str(j) for j in path))


if __name__ == '__main__':
    from sys import argv

    # Question number 3- create_problems_csv
    # utils.create_problems_csv()

    if len(argv) >= 4:
        dispatch(argv)

    # Question number 5- run 100 times UCS
    # utils.run_examples('results/UCSRuns.txt', 1)

    # Question number 9- run 100 times A star
    # utils.run_examples('results/AStarRuns.txt', 2)

    # Question number 12- draw IDAStar 10 maps
    # utils.draw_IDAStar_10_examples()
    # if you changed problem.csv so there are other problems and maybe ida star will take a long time,
    # so I saved the 10 problems that ida star can rum fast here in draw_IDAStar_fixed_10_examples
    # utils.draw_IDAStar_fixed_10_examples()

    # Question number 13- find the run time of every algorithm
    # print("UCS total time of solving 10 problems (for average divide by 10):")
    # utils.run_10_examples(1)
    # print("A Star total time of solving 10 problems (for average divide by 10):")
    # utils.run_10_examples(2)
    # print("IDA Star total time of solving 10 problems (for average divide by 10):")
    # utils.run_10_examples(3)
    # if you changed problem.csv so there are other problems and maybe ida star will take a long time,
    # so I saved the 10 problems that ida star can rum fast here in run_10_fixed_examples
    # print("UCS total time of solving 10 problems (for average divide by 10):")
    # utils.run_10_fixed_examples(1)
    # print("A Star total time of solving 10 problems (for average divide by 10):")
    # utils.run_10_fixed_examples(2)
    # print("IDA Star total time of solving 10 problems (for average divide by 10):")
    # utils.run_10_fixed_examples(3)
