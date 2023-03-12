import heapq
from tkinter import messagebox, Tk

class Dijkstra:
    def __init__(self, ROWS, COLS, MAP):
        self.ROWS = ROWS
        self.COLS = COLS
        self.MAP = MAP

    def ActionMoveLeft(self, curr_node):
        r, c = curr_node
        if c > 0:
            return (r, c-1)
        return None

    def ActionMoveRight(self, curr_node):
        r, c = curr_node
        if c < self.COLS-1:
            return (r, c+1)
        return None

    def ActionMoveUp(self, curr_node):
        r, c = curr_node
        if r > 0:
            return (r-1, c)
        return None

    def ActionMoveDown(self, curr_node):
        r, c = curr_node
        if r < self.ROWS-1:
            return (r+1, c)
        return None

    def ActionMoveUpLeft(self, curr_node):
        r, c = curr_node
        if r > 0 and c > 0:
            return (r-1, c-1)
        return None

    def ActionMoveUpRight(self, curr_node):
        r, c = curr_node
        if r > 0 and c < self.COLS-1:
            return (r-1, c+1)
        return None

    def ActionMoveDownLeft(self, curr_node):
        r, c = curr_node

        if r < self.ROWS-1 and c > 0:
            return (r+1, c-1)
        return None

    def ActionMoveDownRight(self, curr_node):
        r, c = curr_node
        if r < self.ROWS-1 and c < self.COLS-1:
            return (r+1, c+1)
        return None

    def cal_cost(self, node1, node2):
        # Calculate the heuristic cost between two nodes using Manhattan distance
        return abs(node1[0] - node2[0]) + abs(node1[1] - node2[1])

    def get_neighbors(self, curr_node):
        # Define all possible actions
        actions = [self.ActionMoveLeft, self.ActionMoveRight, self.ActionMoveUp, self.ActionMoveDown,
                   self.ActionMoveUpLeft, self.ActionMoveUpRight, self.ActionMoveDownLeft, self.ActionMoveDownRight]

        # Initialize empty list of neighbors
        all_neighbors = []

        # Loop through all possible actions and add valid neighbors to the list
        for action in actions:
            n = action(curr_node)
            if n is not None and n[0] >= 0 and n[0] < self.MAP.shape[0] and n[1] >= 0 and n[1] < self.MAP.shape[1] and self.MAP[n[0]][n[1]] != -1:
                all_neighbors.append(n)

        return all_neighbors


    def generate_path(self, parents, final_node):
        # Function to generate path from initial state to final state using backtracking
        path = []
        state = final_node
        while state is not None:
            path.append(state)
            state = parents.get(state)
        path.reverse()
        return path


    def explore(self, start_node, end_node):
        # Initialize the priority queue with the starting node
        queue = [(0, start_node)]
        # Initialize the explored dictionary with the starting node and its cost
        explored = {start_node: 0}
        # Initialize the parents dictionary to keep track of the parent of each explored node
        parents = {}
        # Initialize list for all explored node
        explored_nodes = []
        # Loop until the priority queue is empty
        while queue:
            # Get the node with the lowest cost from the priority queue
            curr_cost, curr_node = heapq.heappop(queue)

            # If we have reached the end node, generate the path and return it
            if curr_node == end_node:
                print("Solution Found!")
                return explored_nodes, self.generate_path(parents, end_node)

            # Get the neighbors of the current node
            neighbors = self.get_neighbors(curr_node)

            # Loop through each neighbor of the current node
            for n in neighbors:
                # Calculate the cost to move to the neighbor node
                if abs(curr_node[0] - n[0]) == 1 and abs(curr_node[1] - n[1]) == 1:
                    cost = 1.4
                else:
                    cost = 1.0
                # Calculate the total cost to move to the neighbor node
                n_cost = curr_cost + cost

                # If the neighbor node has not been explored or the cost to reach it is less than the previously explored cost, update the explored dictionary and priority queue
                if n not in explored or n_cost < explored[n]:
                    explored[n] = n_cost
                    priority = n_cost + self.cal_cost(n, end_node)
                    heapq.heappush(queue, (priority, n))
                    parents[n] = curr_node
                    explored_nodes.append(n)

        # If the priority queue is empty and we have not found the end node, return None
        Tk().wm_withdraw()
        messagebox.showinfo("No Solution", "There is no solution!")
        return None



