import heapq
from tkinter import messagebox, Tk

class Dijkstra:
    def __init__(self, ROWS, COLS, MAP):
        self.ROWS = ROWS
        self.COLS = COLS
        self.MAP = MAP

    def ActionMoveLeft(self, current_node):
        row, col = current_node
        if col > 0:
            return (row, col-1)
        return None

    def ActionMoveRight(self, current_node):
        row, col = current_node
        if col < self.COLS-1:
            return (row, col+1)
        return None

    def ActionMoveUp(self, current_node):
        row, col = current_node
        if row > 0:
            return (row-1, col)
        return None

    def ActionMoveDown(self, current_node):
        row, col = current_node
        if row < self.ROWS-1:
            return (row+1, col)
        return None

    def ActionMoveUpLeft(self, current_node):
        row, col = current_node
        if row > 0 and col > 0:
            return (row-1, col-1)
        return None

    def ActionMoveUpRight(self, current_node):
        row, col = current_node
        if row > 0 and col < self.COLS-1:
            return (row-1, col+1)
        return None

    def ActionMoveDownLeft(self, current_node):
        row, col = current_node
        if row < self.ROWS-1 and col > 0:
            return (row+1, col-1)
        return None

    def ActionMoveDownRight(self, current_node):
        row, col = current_node
        if row < self.ROWS-1 and col < self.COLS-1:
            return (row+1, col+1)
        return None

    def heuristic(self, node1, node2):
        # Calculate the heuristic cost between two nodes using Manhattan distance
        return abs(node1[0] - node2[0]) + abs(node1[1] - node2[1])

    def get_neighbors(self, current_node):
        # Define all possible actions
        actions = [self.ActionMoveLeft, self.ActionMoveRight, self.ActionMoveUp, self.ActionMoveDown,
                   self.ActionMoveUpLeft, self.ActionMoveUpRight, self.ActionMoveDownLeft, self.ActionMoveDownRight]

        # Initialize empty list of neighbors
        neighbors = []

        # Loop through all possible actions and add valid neighbors to the list
        for action in actions:
            neighbor = action(current_node)
            if neighbor is not None and neighbor[0] >= 0 and neighbor[0] < self.MAP.shape[0] and neighbor[1] >= 0 and neighbor[1] < self.MAP.shape[1] and self.MAP[neighbor[0]][neighbor[1]] != -1:
                neighbors.append(neighbor)

        return neighbors


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
        pq = [(0, start_node)]
        # Initialize the explored dictionary with the starting node and its cost
        explored = {start_node: 0}
        # Initialize the parents dictionary to keep track of the parent of each explored node
        parents = {}

        explored_nodes = []
        # Loop until the priority queue is empty
        while pq:
            # Get the node with the lowest cost from the priority queue
            curr_cost, curr_node = heapq.heappop(pq)

            # If we have reached the end node, generate the path and return it
            if curr_node == end_node:
                print("Solution Found!")
                return explored_nodes, self.generate_path(parents, end_node)

            # Get the neighbors of the current node
            neighbors = self.get_neighbors(curr_node)

            # Loop through each neighbor of the current node
            for neighbor in neighbors:
                # Calculate the cost to move to the neighbor node
                if abs(curr_node[0] - neighbor[0]) == 1 and abs(curr_node[1] - neighbor[1]) == 1:
                    move_cost = 1.4
                else:
                    move_cost = 1.0
                # Calculate the total cost to move to the neighbor node
                neighbor_cost = curr_cost + move_cost

                # If the neighbor node has not been explored or the cost to reach it is less than the previously explored cost, update the explored dictionary and priority queue
                if neighbor not in explored or neighbor_cost < explored[neighbor]:
                    explored[neighbor] = neighbor_cost
                    priority = neighbor_cost + self.heuristic(neighbor, end_node)
                    heapq.heappush(pq, (priority, neighbor))
                    parents[neighbor] = curr_node
                    explored_nodes.append(neighbor)

        # If the priority queue is empty and we have not found the end node, return None
        Tk().wm_withdraw()
        messagebox.showinfo("No Solution", "There is no solution!")
        return None



