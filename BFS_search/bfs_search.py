import numpy as np
import time


def ActionMoveLeft(curr_node):
    # Move blank tile left, if possible
    i, j = np.where(curr_node == 0)
    if j == 0:
        return None
    else:
        new_node = np.copy(curr_node)
        new_node[i, j], new_node[i, j-1] = new_node[i, j-1], new_node[i, j]
        return new_node


def ActionMoveRight(curr_node):
    # Move blank tile right, if possible
    i, j = np.where(curr_node == 0)
    if j == 2:
        return None
    else:
        new_node = np.copy(curr_node)
        new_node[i, j], new_node[i, j+1] = new_node[i, j+1], new_node[i, j]
        return new_node


def ActionMoveUp(curr_node):
    # Move black tile up, if possible
    i, j = np.where(curr_node == 0)
    if i == 0:
        return None
    else:
        new_node = np.copy(curr_node)
        new_node[i, j], new_node[i-1, j] = new_node[i-1, j], new_node[i, j]
        return new_node


def ActionMoveDown(curr_node):
    # Move blank tile down, if possible
    i, j = np.where(curr_node == 0)
    if i == 2:
        return None
    else:
        new_node = np.copy(curr_node)
        new_node[i, j], new_node[i+1, j] = new_node[i+1, j], new_node[i, j]
        return new_node


def print_matrix():
    # Print Matrix by reading nodePath.txt file
    fname = 'nodePath.txt'
    data = np.loadtxt(fname)
    if len(data[1]) != 9:
        print("Format of the text file is incorrect, retry ")
    else:
        for i in range(0, len(data)):
            if i == 0:
                print("Start Node")
            elif i == len(data)-1:
                print("Achieved Goal Node")
            else:
                print("Step ", i)
            counter = 0
            node = data[i]
            # print(node)
            for row in range(0, 3):
                if counter == 0:
                    print("-------------")
                for element in range(counter, counter+3):
                    if element <= counter:
                        print("|", end=" ")
                    print(int(node[element]), "|", end=" ")
                counter = counter + 3
                print("\n-------------")
            print()
            print()


def write_files(path, explored, parents):
    # Write path and explored nodes to files nodePath.txt and nodeInfo.txt
    with open("nodePath.txt", 'w') as f:
        for node in path:
            f.write(' '.join(str(x)
                    for x in [elem for tup in node for elem in tup]) + "\n")
    with open("Nodes.txt", 'w') as f:
        for node in list(explored.keys()):
            f.write(' '.join(str(x)
                    for x in [elem for tup in node for elem in tup]) + "\n")
    with open("NodesInfo.txt", 'w') as f:
        f.write("Node_Index\tParent_Node_Index\tNode\n")
        i = 0
        for node in path:
            f.write(f"{i}\t\t\t{explored.get(tuple(map(tuple, node)))}\t\t\t\t\t" +
                    ' '.join(str(x) for x in [elem for tup in node for elem in tup]) + "\n")
            i += 1


def generate_path(parents, final_node, explored):
    # Function to generate path from initial state to final state using backtracking
    path = []
    state = final_node
    while state is not None:
        path.append(state)
        state = parents.get(tuple(map(tuple, state)))
    path.reverse()
    return write_files(path, explored, parents)


def solve_puzzle(initial_node, final_node):
    # Function to solve puzzle
    queue = [initial_node]
    explored = {tuple(map(tuple, initial_node)): 0}
    parents = {}
    while queue:
        curr_node = queue.pop(0)
        if np.array_equal(curr_node, final_node):
            print("Solution Found")
            return generate_path(parents, final_node, explored)
        parent_index = 0
        for action_move in [ActionMoveLeft, ActionMoveRight, ActionMoveUp, ActionMoveDown]:
            new_nodes = action_move(curr_node)
            if new_nodes is not None and tuple(map(tuple, new_nodes)) not in explored:
                queue.append(new_nodes)
                explored[tuple(map(tuple, new_nodes))] = parent_index
                parents[tuple(map(tuple, new_nodes))] = curr_node
            parent_index += 1
    return print("Solution not found")


if __name__ == "__main__":
    start_node = np.array([[1, 6, 7], [2, 0, 5], [4, 3, 8]])
    goal_node = np.array([[1, 4, 7], [2, 5, 8], [3, 0, 6]])

    st_time = time.process_time()
    solve_puzzle(start_node, goal_node)
    print_matrix()
    print("Time taken to solve the puzzle: " +
          str(time.process_time() - st_time) + " seconds")
