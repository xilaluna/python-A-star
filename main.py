from Node import Node


def astar(maze, start, end):
    """create list with shortest path"""

    # init the start and end node objects
    start_node = Node(None, start)
    start_node.h = 0
    start_node.g = 0
    start_node.f = 0

    end_node = Node(None, end)
    end_node.h = 0
    end_node.g = 0
    end_node.f = 0

    # init open list and closed list and add start node for starting point
    unvisited = [start_node]
    visited = []

    # loop until we have finished visting the path
    while len(unvisited) > 0:
        # get current node
        current = unvisited[0]
        current_index = 0

        # check to see if the current node has the loweset f cost then assign loweset cost node.
        for index, next_node in enumerate(unvisited):
            if next_node.f < current.f:
                current = next_node
                current_index = index

        # remove current node form unvisited and put it into visited.
        unvisited.pop(current_index)
        visited.append(current)

        # check to see if the current node equals the end node then return path list.
        if current == end_node:
            path = []
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path.reverse()  # return reversed path

        # generate the nodes neighbors.
        neighbors = []
        # Adjacent squares
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:

            node_position = (current.position[0] + new_position[0],
                             current.position[1] + new_position[1])

            # check to see if in the range and if walkable
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) - 1) or node_position[1] < 0:
                continue
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # create new node and append to neighbor list.
            neighbor_node = Node(current, node_position)
            neighbors.append(neighbor_node)

        for neighbor in neighbors:
            for closed_neighbor in visited:
                if neighbor == closed_neighbor:
                    continue

            neighbor.h = current.h + 1
            neighbor.g = ((neighbor.position[0] - end_node.position[0]) ** 2) + (
                (neighbor.position[1] - end_node.position[1]) ** 2)
            neighbor.f = neighbor.g + neighbor.h

            for unvisited_node in unvisited:
                if neighbor == unvisited_node and neighbor.g > unvisited_node.g:
                    continue

            unvisited.append(neighbor)
