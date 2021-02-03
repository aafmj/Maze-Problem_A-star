


class Node:

    def __init__(self, location):
        self.g = None
        self.h = None
        self.f = None
        self.location = location
        self.parent = None


def get_maze(address='maze.txt'):
    
    with open('maze.txt', 'r') as maze_file:
        maze_string = maze_file.readlines()
    
    maze = []
    for line in maze_string:
        row = list (line.rstrip("\n"))
        maze.append(row)

    return maze


def get_location(maze, spot):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == spot:
                return (i, j)
    raise Exception('You should declare \"{}\" in the Maze.txt'.format(spot))


def get_h(current_location, goal_location):
    """
    get manhattan distance of every node.

    """
    return abs(goal_location[0]-current_location[0]) + abs(goal_location[1]-current_location[1])


def get_path(node):
    """
    return a list of location (tuples) that is path to 
    given node from start node.
    """
    path = []
    current = node
    while current is not None:
        path.append(current.location)
        current = current.parent
    return path[::-1] # Return reversed path


def create_successors(location, goal_location, parent):
    node = Node(location)
    node.g = parent.g + 1
    node.h = get_h(location, goal_location)//2
    node.f = node.g + node.h
    node.parent = parent

    # PATHMAX quation
    if node.f < parent.f:
        node.f = parent.f

    return node


def get_successors(maze, node, goal_location):
    """
    return a list of given node's successors (children with Node type).
    """
    successors = []

    up_lock = True if node.parent and node.location[0] > node.parent.location[0] else False
    down_lock = True if node.parent and node.location[0] < node.parent.location[0] else False
    right_lock = True if node.parent and node.location[1] < node.parent.location[1] else False
    left_lock = True if node.parent and node.location[1] > node.parent.location[1] else False
    

    if node.location[1]-1 > 0 and maze[node.location[0]][node.location[1]-1] == ' ' and not left_lock:
        successor = create_successors((node.location[0], node.location[1]-2), goal_location, node)
        successors.append(successor)
    if node.location[1]+1 < 2*len(maze[0])-1 and maze[node.location[0]][node.location[1]+1] == ' ' and not right_lock:
        successor = create_successors((node.location[0], node.location[1]+2), goal_location, node)
        successors.append(successor)
    if node.location[0]-1 > 0 and maze[node.location[0]-1][node.location[1]] == ' ' and not up_lock:
        successor = create_successors((node.location[0]-2, node.location[1]), goal_location, node)
        successors.append(successor)
    if node.location[0]+1 < 2*len(maze)-1 and maze[node.location[0]+1][node.location[1]] == ' ' and not down_lock:
        successor = create_successors((node.location[0]+2, node.location[1]), goal_location, node)
        successors.append(successor)

    return successors


def a_star_search(maze, start_location, goal_location):

    open_list = []

    # Initialize Start Node
    start_node = Node(start_location)
    start_node.g = 0
    start_node.h = start_node.f = get_h(start_location, goal_location)
    open_list.append(start_node)

    while (len(open_list) > 0):
        current_node = open_list.pop(0)

        if current_node.location == goal_location:
            return get_path(current_node)

        open_list.extend(get_successors(maze, current_node, goal_location))
        
        open_list.sort(key=lambda x: x.f)
            

    print('There is no way!!')


def fill_maze(maze, path):
    
    for item in path:
        maze[item[0]][item[1]] = '#' if maze[item[0]][item[1]] == '.' else maze[item[0]][item[1]]

    maze_string = ''
    for row in maze:
        for col in row:
            maze_string += col
        maze_string += '\n'

    with open('maze.txt', 'w') as maze_file:
        maze_file.write(maze_string)


def main():
    maze = get_maze()  # Make a 2D array of char.
    path = a_star_search(maze, get_location(maze, 'S'), get_location(maze, 'G'))  # list of indexes as optimal path from "S" to "G" (declared in the maze) if exists.
    fill_maze(maze, path)  # filling the maze with path founded by A* algorithm.
    

if __name__ == '__main__': main()