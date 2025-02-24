# The Python code contained in this file solves the 8-Puzzle problem with the breadth-first search (BFS) algorithm.
# Author: Ronen Aniti

import queue # For BFS

def flatten_2d_list_to_tuple(list_2d):
    """
    Given a 2d list, returns a flattened (1D tuple) containing the same elements. 

    Args:
        list_2d (list of lists): A 2d list
    
    Returns:
        flattened_tuple (tuple): A 1d tuple containing the same elements as the input 2d list
    """
    # 1. Initializes an empty list
    flattened_list = []
    # 2. Iterates through the elements of the input list, adding each, one by on, the the flattened list
    for row in list_2d:
        for element in row:
            flattened_list.append(element)
    # 3. Convert the flattened list to a flattened tuple
    flattened_tuple = tuple(flattened_list)
    return flattened_tuple

def flatten_2d_list_to_tuple_column(list_2d):
    """
    Given a 2d list, returns a flattened (1D tuple) containing the same elements--column-wise. I am creating this as a helper function to aid with integration with Animate.py.

    Args:
        list_2d (list of lists): A 2d list
    
    Returns:
        flattened_tuple (tuple): A 1d tuple containing the same elements as the input 2d list
    """
    # 1. Initializes an empty list
    flattened_list = []
    # 2. Determine the number of rows and columns
    num_rows = len(list_2d)
    num_columns = len(list_2d[0])
    # 3. Iterate column-wise: for each column, loop through all rows.
    for j in range(num_columns):
        for i in range(num_rows):
            flattened_list.append(list_2d[i][j])
    # 4. Convert the flattened list to a tuple
    flattened_tuple = tuple(flattened_list)
    return flattened_tuple


def is_move_valid(blank_tile_index, action):
    """
    Returns whether a given move is valid. For a given move to be valid, it must result in the blank tile remaining on the 3x3 board. 

    Args:
        blank_tile_index (tuple): the (i, j) index of the blank tile
        action (tuple): the (di, dj) tuple describing change in position
    
    Returns: 
        bool: whether the move is valid
    """
    # 1. Unpack the blank tile index
    i, j = blank_tile_index
    # 2. Unpack the action
    di, dj = action
    # 3. Compute the target index
    target_index_i = i + di 
    target_index_j = j + dj
    # 4. Defines the lower and upper index limits of a 3x3 board
    lower_limit = 0
    upper_limit = 2
    # 5. Returns True if and only if the target index is on the board, otherwise returns False
    if target_index_i < lower_limit or target_index_i > upper_limit:
        return False
    if target_index_j < lower_limit or target_index_j > upper_limit:
        return False 
    return True
    
def find_the_blank(board_state):
    """
    Returns the index of the blank tile, given the board's state.

    Args:
        board_state (list of lists): The board's 3x3 state
    
    Returns: 
        blank_tile_index: the (i, j) index of the blank tile
    """
    for i in range(3):
        for j in range(3):
            if board_state[i][j] == 0:
                blank_tile_index = (i, j)
                return blank_tile_index

def move_left(board_state):
    """
    Moves the blank tile to the left.

    Args:
        board_state (list of lists): The board's 3x3 state
    
    Returns: 
        bool: Whether or not the move was a success 
        new_board_state (list of lists): The board's state after a successful move. When the move is not successful, this return is None.  
    """
    # 1. Define's moving left
    action_left = (0, -1)
    action_left_i = action_left[0]
    action_left_j = action_left[1]
    # 2. Tries to move the board state left
    # 2.1 Finds the blank tile
    blank_tile_index = find_the_blank(board_state)
    blank_tile_i = blank_tile_index[0]
    blank_tile_j = blank_tile_index[1]
    # 2.2 Checks if moving the blank tile by action is valid
    is_valid = is_move_valid(blank_tile_index, action_left)
    # 2.3 Returns False and None board state if the move is invalid
    if not is_valid:
        return False, None
    # 2.4 If the move is valid...
    # 2.4.1 Copy the existing board state to preserve it
    new_board_state = [row[:] for row in board_state]
    # 2.4.2 Compute the new tile index
    new_tile_i = blank_tile_i + action_left_i 
    new_tile_j = blank_tile_j + action_left_j 
    # 2.4.3 Swap the blank tile with the tile to its left
    new_board_state[blank_tile_i][blank_tile_j], new_board_state[new_tile_i][new_tile_j] = new_board_state[new_tile_i][new_tile_j], new_board_state[blank_tile_i][blank_tile_j]
    # 2.4.4 Return a success with the board's new state
    return True, new_board_state 


def move_right(board_state):
    """
    Moves the blank tile to the right.

    Args:
        board_state (list of lists): The board's 3x3 state
    
    Returns: 
        bool: Whether or not the move was a success 
        new_board_state (list of lists): The board's state after a successful move. When the move is not successful, this return is None.  
    """
    # 1. Define's moving right
    action_right = (0, 1)
    action_right_i = action_right[0]
    action_right_j = action_right[1]
    # 2. Tries to move the board state right
    # 2.1 Finds the blank tile
    blank_tile_index = find_the_blank(board_state)
    blank_tile_i = blank_tile_index[0]
    blank_tile_j = blank_tile_index[1]
    # 2.2 Checks if moving the blank tile by action is valid
    is_valid = is_move_valid(blank_tile_index, action_right)
    # 2.3 Returns False and None board state if the move is invalid
    if not is_valid:
        return False, None
    # 2.4 If the move is valid...
    # 2.4.1 Copy the existing board state to preserve it
    new_board_state = [row[:] for row in board_state]
    # 2.4.2 Compute the new tile index
    new_tile_i = blank_tile_i + action_right_i 
    new_tile_j = blank_tile_j + action_right_j 
    # 2.4.3 Swap the blank tile with the tile to its right
    new_board_state[blank_tile_i][blank_tile_j], new_board_state[new_tile_i][new_tile_j] = new_board_state[new_tile_i][new_tile_j], new_board_state[blank_tile_i][blank_tile_j]
    # 2.4.4 Return a success with the board's new state
    return True, new_board_state 

def move_down(board_state):
    """
    Moves the blank tile to the down.

    Args:
        board_state (list of lists): The board's 3x3 state
    
    Returns: 
        bool: Whether or not the move was a success 
        new_board_state (list of lists): The board's state after a successful move. When the move is not successful, this return is None.  
    """
    # 1. Define's moving down
    action_down = (1, 0)
    action_down_i = action_down[0]
    action_down_j = action_down[1]
    # 2. Tries to move the board state down
    # 2.1 Finds the blank tile
    blank_tile_index = find_the_blank(board_state)
    blank_tile_i = blank_tile_index[0]
    blank_tile_j = blank_tile_index[1]
    # 2.2 Checks if moving the blank tile by action is valid
    is_valid = is_move_valid(blank_tile_index, action_down)
    # 2.3 Returns False and None board state if the move is invalid
    if not is_valid:
        return False, None
    # 2.4 If the move is valid...
    # 2.4.1 Copy the existing board state to preserve it
    new_board_state = [row[:] for row in board_state]
    # 2.4.2 Compute the new tile index
    new_tile_i = blank_tile_i + action_down_i 
    new_tile_j = blank_tile_j + action_down_j 
    # 2.4.3 Swap the blank tile with the tile to its down
    new_board_state[blank_tile_i][blank_tile_j], new_board_state[new_tile_i][new_tile_j] = new_board_state[new_tile_i][new_tile_j], new_board_state[blank_tile_i][blank_tile_j]
    # 2.4.4 Return a success with the board's new state
    return True, new_board_state 

def move_up(board_state):
    """
    Moves the blank tile to the up.

    Args:
        board_state (list of lists): The board's 3x3 state
    
    Returns: 
        bool: Whether or not the move was a success 
        new_board_state (list of lists): The board's state after a successful move. When the move is not successful, this return is None.  
    """
    # 1. Define's moving up
    action_up = (-1, 0)
    action_up_i = action_up[0]
    action_up_j = action_up[1]
    # 2. Tries to move the board state up
    # 2.1 Finds the blank tile
    blank_tile_index = find_the_blank(board_state)
    blank_tile_i = blank_tile_index[0]
    blank_tile_j = blank_tile_index[1]
    # 2.2 Checks if moving the blank tile by action is valid
    is_valid = is_move_valid(blank_tile_index, action_up)
    # 2.3 Returns False and None board state if the move is invalid
    if not is_valid:
        return False, None
    # 2.4 If the move is valid...
    # 2.4.1 Copy the existing board state to preserve it
    new_board_state = [row[:] for row in board_state]
    # 2.4.2 Compute the new tile index
    new_tile_i = blank_tile_i + action_up_i 
    new_tile_j = blank_tile_j + action_up_j 
    # 2.4.3 Swap the blank tile with the tile to its up
    new_board_state[blank_tile_i][blank_tile_j], new_board_state[new_tile_i][new_tile_j] = new_board_state[new_tile_i][new_tile_j], new_board_state[blank_tile_i][blank_tile_j]
    # 2.4.4 Return a success with the board's new state
    return True, new_board_state 


def backtrack(search_tree, goal_node_index):
    """
    Given the search tree and the goal node index, this function executes a backtracking loop and returns both the start-to-goal sequence of board states and the sequence of board actions taken.  

    Args:
        search_tree (dict): The dictionary data structure holding the entire BFS search tree.
        goal_node_index (int): The node index of the goal state

    Returns:
        path_of_states (list): The start-to-goal path of board states
        path_of_actions (list): The sequence of actions taken in traversing the search tree from start to goal. 
    """
    print("Backtracking...")
    # 1. Define a list to store a path of states and a path of actions.
    # 1.1 Place the goal state and action taken to reach the goal as the first element of these respective lists. 
    goal_state = search_tree[goal_node_index][1] 
    path_of_states = [goal_state]
    action_to_goal = search_tree[goal_node_index][2]
    path_of_actions = [action_to_goal]
    # 2. Backtrack from goal state to state state using the input search tree data structure
    # 2.1 Define an index to track the child node
    current_index = goal_node_index
    # 2.2 While the parent to current is not None
    while search_tree[current_index][0] != None: 
        # 2.2.1 Extract the parent index to current
        parent_index = search_tree[current_index][0]
        # 2.2.2 Extract the parent state to current
        parent_state = search_tree[parent_index][1]
        # 2.2.3 Extract the action that resulted in parent
        parent_action = search_tree[parent_index][2]
        # 2.2.4 Append parent's state and parent's action to respective lists
        path_of_states.append(parent_state)
        if parent_action != None: # A check to avoid adding a None to the action path when parent action is none (when current is one away from the start node)
            path_of_actions.append(parent_action)
        # 2.2.4 Update the current index 
        current_index = parent_index
    # 2.3 Reverse the lists
    path_of_states = path_of_states[::-1]
    path_of_actions = path_of_actions[::-1]
    # 2.4 Return both lists
    print(path_of_actions)
    return path_of_states, path_of_actions

def generate_nodes_txt(search_tree):
    with open("Nodes.txt", "w") as file:
        for value in search_tree.values():
            board_state = value[1]
            flattened_board_state = flatten_2d_list_to_tuple_column(board_state)
            file.write(' '.join(map(str, flattened_board_state)) + "\n")

def generate_nodes_info_txt(search_tree):
    with open("NodesInfo.txt", "w") as file:
        file.write("Node_Index\tParent_Node_Index\tNode\n")
        for key, value in search_tree.items():
            node_index = key 
            parent_node_index = value[0] if value[0] is not None else "None"
            node = value[1]
            flattened_board_state = flatten_2d_list_to_tuple_column(node)
            flattened_string = " ".join(map(str, flattened_board_state))
            file.write(f"{node_index}\t{parent_node_index}\t{flattened_string}\n")

def generate_nodes_path(path_of_states):
    with open("nodePath.txt", "w") as file:
        for board_state in path_of_states:
            flattened_board_state = flatten_2d_list_to_tuple_column(board_state)
            file.write(' '.join(map(str, flattened_board_state)) + "\n")

def solve(start, goal):
    """
    Solves the 8-Puzzle problem for a given start and goal configuration, returning the solution. 

    Args:
        start (list of list of int): the starting board state
        goal (list of list of int): the goal board state

    Returns: 
        path (list of tuple): the path from start to goal
    """
    # 0. Define a flag for whether the goal state is found
    goal_is_found = False 
    # 1. Configure a data structure for the search tree
    # 1.1 Initialize a dictionary 
    search_tree = dict() 
    # 1.2 Assign the start state an index within the search tree
    start_index = 0
    # 1.3 Define the parent node of the start node
    start_parent = None
    # 1.4 Define the action that resulted in the start node
    start_action = None
    # 1.5 Define an entry for the start node in the search tree's data structure
    search_tree[start_index] = (start_parent, start, start_action)
    # 4. Define a data structure for the BFS visited nodes
    visited = set()
    # 5. Add the start node to the visited set
    visited.add(flatten_2d_list_to_tuple(start))
    # 2. Define a FIFO queue for the BFS nodes awaiting visits
    fifo_queue = queue.Queue()
    # 3. Add the start node to the FIFO queue
    fifo_queue.put(start_index)
    # 5. Define a variable for assigning indices to new nodes
    node_index = start_index
    # 6. Begin the main BFS loop
    while not fifo_queue.empty():
        # 6.1 Remove the next node index from the FIFO queue
        current_index = fifo_queue.get()
        # 6.2 Look up the corresponding board state for this index
        current_state = search_tree[current_index][1]

        # 6.4 Checks whether this node is the goal node
        if flatten_2d_list_to_tuple(current_state) == flatten_2d_list_to_tuple(goal):
            print("The BFS algorithm found the goal node")
            goal_is_found = True
            goal_node_index = current_index
            path_of_states, path_of_actions = backtrack(search_tree, goal_node_index)
            break
        # 6.5 Evaluate the board state over all hypothetical moves
        right_status, right_neighbor_state = move_right(current_state)
        left_status, left_neighbor_state = move_left(current_state)
        up_status, up_neighbor_state = move_up(current_state)
        down_status, down_neighbor_state = move_down(current_state)
        # 6.6 Add the new board states that are valid to the FIFO queue if and only if they have not been visited
        if right_status and flatten_2d_list_to_tuple(right_neighbor_state) not in visited:
            node_index +=1
            visited.add(flatten_2d_list_to_tuple(right_neighbor_state))
            fifo_queue.put(node_index)
            delta_right = (0, 1)
            search_tree[node_index] = (current_index, right_neighbor_state, delta_right)
        if left_status and flatten_2d_list_to_tuple(left_neighbor_state) not in visited:
            node_index +=1
            visited.add(flatten_2d_list_to_tuple(left_neighbor_state))
            fifo_queue.put(node_index)
            delta_left = (0, -1)
            search_tree[node_index] = (current_index, left_neighbor_state, delta_left)
        if up_status and flatten_2d_list_to_tuple(up_neighbor_state) not in visited:
            node_index += 1
            visited.add(flatten_2d_list_to_tuple(up_neighbor_state))
            fifo_queue.put(node_index)
            delta_up = (-1, 0)
            search_tree[node_index] = (current_index, up_neighbor_state, delta_up)
        if down_status and flatten_2d_list_to_tuple(down_neighbor_state) not in visited:
            node_index += 1
            visited.add(flatten_2d_list_to_tuple(down_neighbor_state))
            fifo_queue.put(node_index)
            delta_down = (1, 0)
            search_tree[node_index] = (current_index, down_neighbor_state, delta_down)
        print(node_index)
    # 7. Return the path of states and the path of actions iff the goal is found. If the goal isn't found, inform the user and return empty paths.
    if goal_is_found:
        return path_of_states, path_of_actions, search_tree
    else:
        print("BFS failed to find the goal node")
        return [], []
        
if __name__ == "__main__":
    # 1. Define the start state
    start = [
        [2, 8, 3],
        [1,  6, 4],
        [7, 0, 5]              
    ]

    # 2. Define the goal sate
    goal = [
        [1, 2, 3],
        [8, 0, 4],
        [7, 6, 5]
    ]
    # 3. Solve the puzzle
    path_of_states, path_of_actions, search_tree = solve(start, goal)
    # 4. Save solution data to files
    # 4.1 Save tree nodes of search tree to file
    generate_nodes_txt(search_tree)
    # 4.2 Save all data from search tree to file
    generate_nodes_info_txt(search_tree)
    # 4.3 Save the path to a file
    generate_nodes_path(path_of_states)



