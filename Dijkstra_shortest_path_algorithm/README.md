# Dijkstra Shortest Path Algorithm

## Description

This program implements Dijkstra's algorithm for determining the shortest path between two points on a map. The map is represented as a grid of cells, with each cell having the option of being blocked or unblocked. The map has also been scaled up by two times for greater viewing and to accommodate for robot clearance (5mm). The user can select a start node and a goal node by clicking on cells (it prompts the user to above the obstacles, if obstacle is selected it prompts the user to select again). The program will then locate and display the shortest path between the start and end cells on the map.

"main.py" and "dijkstra.py" are the two files. The algorithm class is contained in the "dijkstra.py" file.


The Dijkstra class contains several helper methods for calculating the cost of moving between two adjacent cells in the grid (ActionMoveLeft, ActionMoveRight, etc.), a heuristic function for estimating the cost of moving from one node to another (heuristic), a method for getting the neighboring nodes of a given node (get_neighbors), and a method for generating the path from the starting node to the ending node (generate_path).

The explore technique is the primary approach for using Dijkstra's algorithm to discover the shortest path between two nodes. It creates a priority queue with the starting node, an explored dictionary with the starting node and its cost, and a parents dictionary to keep track of each explored node's parent. The program then repeats until the priority queue is empty. For each loop iteration, it retrieves the node with the lowest cost from the priority queue, determines whether it is the end node, and generates the path if it is. If it is not, it obtains the current node's neighbors and computes the cost of moving to each of them. It updates the explored dictionary and priority queue if the neighbor has not been examined or if the cost to reach it is less than the previously explored cost. Ultimately, if the priority queue is empty and the end node has not been discovered, a message indicating that there is no solution is displayed.

The "main.py" file imports the dijkstra class and retrieves the produced path as well as the nodes that have been investigated. They are then utilized to display the algorithm's operation and the final path on the pygame window.

## Requirements

-   Python 3.x
-   NumPy library
-   Time module
-   tkinter
-   pygame
-   math
-   heapq

## Installation

1.  Install Python 3.x on your computer.
2.  Install NumPy library using the following command:
    ```
    pip install numpy
    ``` 
3.  The math, heapq and time module comes with Python’s standard utility module, so there is no need to install it externally.
4.  Install tkinter using the following command:
    ```
    pip install tk
    ```
5.  Install pygame using the following command:
    ```
    pip install pygame
    ```

## Usage

1.  Open the file `main.py` in any Python IDE or text editor.
2.  Run the code `main.py` and user is prompted by tkinter window to select start and end node.
3.  Close the prompt and select the start and end nodes.
4.  The explored nodes are animated and the final path is plotted.
5.  The source code can also be cloned from github repositiory. To clone the repository: git clone https://github.com/tarunreddyy/Planning-for-Autonomous-Robots.git
6.  Navigate to the "Dijkstra_Shortest_Path_Algorithm" directory and follow the instructions.
7.  Video has been attached for reference on how to run the code.


## Output

The output of the program displays the animation and the final path on the pygame window. 