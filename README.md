Osher Elhadad 318969748

#Homework 1 - Heuristic Search

##Directory Structure

Add your source files here, and insert calls for the functions in them inside main.py.

You can add directories for 3rd party libraries. Remember to declare `dir your_directory` in docs/dependencies.txt.


__init__.py: A hint for the interpreter - ignore this file

main.py: Minimal interface to the command line: `$ python main.py [args]`

stats.py: Gather and print statistics: `$ python stats.py`

utils.py: Gather the all functions that help the functions in main.py

junction_node.py: defines a junction node in our roads path problem

priority_queue.py: defines a priority queue by a cost function

roads_path_problem.py: defines a problem of roads paths

search_algorithms.py: Gather the all search algorithms functions

problems.csv: 100 search problems (a problem like '22,44' in every row)

___
ways/
Primary library. Basic usage: 
```python
from ways import load_map_from_csv
roads = load_map_from_csv()
````
ways/README.md: Library documentation

ways/__init__.py: Defines the functions accessible using `import ways`

ways/graph.py: Code to load the map from the database

ways/info.py: Constants

ways/tools.py: Arbitrary, possibly useful tools

ways/draw.py: Helper file for drawing paths using matplotlib

___

docs/
Documentation

[`docs/dependencies.txt`](docs/dependencies.txt) Declarations of dependencies in 3rd party libraries. For example:

> pip numpy
>

___
db/
Database. Do not change.

db/israel.csv Roads description. primary database file

___		
results/
Put your experiment results (text and images) here

Has UCSRuns.txt and AStarRuns.txt solution paths to problems.csv

___		
sulotions_img/
The 10 img maps of IDA Star algorithm solutions
