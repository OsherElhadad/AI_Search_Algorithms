# Osher Elhadad 318969748
'''
This file should be runnable to print map_statistics using 
$ python stats.py
'''
from collections import namedtuple
from collections import Counter
import numpy as np
from ways import load_map_from_csv


def map_statistics(roads):
    '''return a dictionary containing the desired information
    You can edit this function as you wish'''
    Stat = namedtuple('Stat', ['max', 'min', 'avg'])
    num_of_links = np.array([len(junction.links) for junction in roads.values()])
    link_distance = np.array([link.distance for junction in roads.values() for link in junction.links])
    link_type = [link.highway_type for junction in roads.values() for link in junction.links]

    return {
        'Number of junctions': len(roads),
        'Number of links': num_of_links.sum(),
        'Outgoing branching factor': Stat(max=num_of_links.max(), min=num_of_links.min(), avg=num_of_links.mean()),
        'Link distance': Stat(max=link_distance.max(), min=link_distance.min(), avg=link_distance.mean()),
        # value should be a dictionary
        # mapping each road_info.TYPE to the no' of links of this type
        'Link type histogram': Counter(link_type),  # tip: use collections.Counter
    }


def print_stats():
    for k, v in map_statistics(load_map_from_csv()).items():
        print('{}: {}'.format(k, v))


if __name__ == '__main__':
    from sys import argv
    assert len(argv) == 1

    # Question number 2- map_statistics
    print_stats()

