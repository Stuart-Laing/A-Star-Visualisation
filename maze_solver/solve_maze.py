

class NodeList:
    def __init__(self):
        self.nodes = {}

    def __repr__(self):
        return repr(self.nodes)

    def add_node_values(self, node_coords, end_coords, parent_g_cost, parent_coords):
        self.nodes[node_coords] = Node(node_coords, end_coords, parent_g_cost, parent_coords)

    def add_node_node(self, node):
        self.nodes[node.node_coords] = node

    def get_lowest_f_cost_node(self):
        lowest_f_cost = list(self.nodes.values())[0]

        for node in self.nodes.values():
            if node.f_cost < lowest_f_cost.f_cost:
                lowest_f_cost = node

        self.nodes.pop(lowest_f_cost.node_coords)

        return lowest_f_cost

    def remove(self, node_coords):
        self.nodes.pop(node_coords)

    def contains(self, node_coords):
        if node_coords in self.nodes:
            return True
        else:
            return False

    def shorter_path(self, neighbor_coords, finish, parent_g_cost):
        if self.contains(neighbor_coords):
            new_node = Node(neighbor_coords, finish, parent_g_cost, None)

            if new_node.f_cost < self.nodes[neighbor_coords].f_cost:
                return True

            else:
                return False

        return False


class Node:
    def __init__(self, node_coords, end_coords, parent_g_cost, parent_coords):
        self.node_coords = node_coords
        self.parent_coords = parent_coords

        if parent_coords is None:
            self.f_cost = self.node_distance(node_coords, end_coords)
            self.g_cost = 0

        else:
            self.f_cost = parent_g_cost + self.node_distance(node_coords, end_coords)
            self.g_cost = self.node_distance(node_coords, parent_coords)

    def __repr__(self):
        output_string = f"Node(node_coords={self.node_coords}, "
        output_string += f"f_cost={self.f_cost}, "
        output_string += f"parent_coords={self.parent_coords})"

        return output_string

    @staticmethod
    def node_distance(node1, node2):
        return (((node2[0] - node1[0]) ** 2) + ((node2[1] - node1[1]) ** 2)) ** 0.5


def find_path(end_node, closed_nodes):
    path = []

    current_node = end_node
    while True:
        path = [current_node.node_coords] + path

        if current_node.parent_coords is None:
            break

        else:
            current_node = closed_nodes.nodes[current_node.parent_coords]

    return path


def solve_maze(maze, start, finish):
    open_nodes = NodeList()
    closed_nodes = NodeList()

    open_nodes.add_node_values(start, finish, None, None)

    while True:
        current_node = open_nodes.get_lowest_f_cost_node()
        closed_nodes.add_node_node(current_node)

        if current_node.node_coords == finish:
            break

        for neighbor_coords in get_neighbors(current_node.node_coords, maze):
            if closed_nodes.contains(neighbor_coords):
                continue

            if open_nodes.shorter_path(neighbor_coords, finish, current_node.f_cost) or \
                    not open_nodes.contains(neighbor_coords):

                if open_nodes.contains(neighbor_coords):
                    open_nodes.remove(neighbor_coords)
                    open_nodes.add_node_values(neighbor_coords, finish, current_node.g_cost, current_node.node_coords)

                else:
                    open_nodes.add_node_values(neighbor_coords, finish, current_node.g_cost, current_node.node_coords)

    return find_path(current_node, closed_nodes)


def get_neighbors(node, maze):
    possible_neighbors = [(node[0] + 1, node[1]), (node[0] - 1, node[1]),
                          (node[0], node[1] + 1), (node[0], node[1] - 1)]

    real_neighbors = []

    for possible_neighbor in possible_neighbors:
        if 0 < possible_neighbor[0] < len(maze) or 0 < possible_neighbor[1] < len(maze[0]):
            if not maze[possible_neighbor[0]][possible_neighbor[1]]:
                real_neighbors.append(possible_neighbor)

    return real_neighbors
