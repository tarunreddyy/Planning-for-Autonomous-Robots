import pygame
import numpy as np
import math
import time
from tkinter import messagebox, Tk
import heapq

# Initialize pygame
pygame.init()

# Set the window dimensions and the cell size
WINDOW_WIDTH, WINDOW_HEIGHT = 1200, 500
CELL_SIZE = 10 #5mm clearance

# Create the window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Set the title of the window
pygame.display.set_caption("Dijkstra Algorithm Simulation")

# Define the number of rows and columns in the map
ROWS, COLS = WINDOW_HEIGHT // CELL_SIZE, WINDOW_WIDTH // CELL_SIZE

BOX_WIDTH = WINDOW_WIDTH // COLS
BOX_HEIGHT = WINDOW_HEIGHT // ROWS

# Create the map
MAP = np.zeros((ROWS, COLS), dtype=np.int8)

# Define the colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 191, 255)
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)
LIGHT_GRAY = (100, 100, 100)
YELLOW = (255, 255, 0)

#################################################
# Dijkstra Algorithm
#################################################
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
    
#################################################
# Visualization
#################################################
def draw_shapes():
    screen.fill(WHITE)

    # Draw the shapes
    rect1 = pygame.draw.rect(screen, RED, (200, 0, 100, 200))
    rect2 = pygame.draw.rect(screen, RED, (200, 300, 100, 200))
    
    center = (600, 250)
    # calculate the six vertices of the hexagon based on the center point and side length
    side_length = CELL_SIZE * 15
    vertices = []
    for i in range(6):
        angle_deg = 60 * i - 30
        angle_rad = math.pi / 180 * angle_deg
        x = center[0] + side_length * math.cos(angle_rad)
        y = center[1] + side_length * math.sin(angle_rad)
        vertices.append((x, y))

    # draw the hexagon on the screen
    hexagon = pygame.draw.polygon(screen, RED, vertices, 0)
    triangle = pygame.draw.polygon(screen, RED, [(920, 450), (1020, 250), (920, 50)])
   
    # Create the map
    MAP = create_map(screen)

    screen.fill(LIGHT_GRAY)
    # Display the map in the console
    for i in range(MAP.shape[0]):
        for j in range(MAP.shape[1]):
            if MAP[i][j] == 0:
                pygame.draw.rect(screen, GRAY, (j * BOX_WIDTH, i * BOX_HEIGHT, BOX_WIDTH-1, BOX_HEIGHT-1))
            elif MAP[i][j] == -1:
                pygame.draw.rect(screen, RED, (j * BOX_WIDTH, i * BOX_HEIGHT, BOX_WIDTH-1, BOX_HEIGHT-1))

    # Update the display
    pygame.display.update()
    return screen

def create_map(screen):    
    # Convert the shapes to the grid
    for i in range(0, WINDOW_HEIGHT, CELL_SIZE):
        for j in range(0, WINDOW_WIDTH, CELL_SIZE):
            # Check if the box window contains a red pixel
            box_rect = pygame.Rect(j, i, BOX_WIDTH, BOX_HEIGHT)
            box_pixels = pygame.PixelArray(screen.subsurface(box_rect))
            if RED in box_pixels:
                MAP[int(i / CELL_SIZE)][int(j / CELL_SIZE)] = -1
            else:
                MAP[int(i / CELL_SIZE)][int(j / CELL_SIZE)] = 0
    return MAP

def select_box(screen):
    # Initialize the selected box to None
    selected_box = None
    # Loop until a box is selected
    while selected_box is None:
        # Wait for a mouse movement event
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Get the mouse point location
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Turn the box blue and return the location
                box_col = mouse_x // CELL_SIZE
                box_row = mouse_y // CELL_SIZE
                box_rect = pygame.Rect(box_col * CELL_SIZE, box_row * CELL_SIZE, BOX_WIDTH-1, BOX_HEIGHT-1)
                pygame.draw.rect(screen, BLUE, box_rect)
                selected_box = (box_row, box_col)
                pygame.display.update()
                return selected_box
            elif event.type == pygame.QUIT:
                # Quit the pygame module
                pygame.quit()

def color_nodes(nodes,color):
    for box in nodes:
        rect = pygame.Rect(box[1] * CELL_SIZE, box[0] * CELL_SIZE, BOX_WIDTH-1, BOX_HEIGHT-1)
        pygame.draw.rect(screen, color, rect)
        pygame.display.update()

def main():
    # Set up the event loop
    while True:
        start_time = time.process_time()
        screen = draw_shapes()
        Tk().wm_withdraw()
        messagebox.showinfo("Select Start Node and Target Node (Avoid the obstacles)!")
        start_node = select_box(screen)
        end_node = select_box(screen)
        if MAP[start_node[0],start_node[1]] == -1 or MAP[end_node[0],end_node[1]] == -1 or start_node == end_node:
            Tk().wm_withdraw()
            messagebox.showinfo("Try Again!")
            continue
        else:
            print(f"Start node: {start_node} and End node: {end_node}")
            dijkstra = Dijkstra(ROWS, COLS, MAP)
            explored,path = dijkstra.explore(start_node, end_node)
            # print("Path:", path)
            if path is not None:
                color_nodes(explored,YELLOW)
                screen = draw_shapes()
                color_nodes(path,BLUE)
                print(f"Time taken to process: {time.process_time()-start_time}")
            break

    # Set up the event loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    
    # Quit the pygame module
    pygame.quit()


if __name__ == "__main__":
    main()