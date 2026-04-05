class Graph:
    """
    Representation of a graph (directed or undirected, with positive edge weights).
    You may choose the internal representation, e.g., adjacency list (with weights) or
    adjacency/distance matrix.
    """

    def __init__(self, number_of_nodes, directed=True):
        """Initialize the graph with a given number of nodes and orientation.

        Args:
            number_of_nodes (int): Number of nodes in the graph.
            directed (bool): True for a directed graph, False for undirected.

        Exception handling:
            Check that number_of_nodes is a non-negative integer. Raise ValueError if invalid.
        """
        if number_of_nodes < 0:
            raise ValueError("number_of_nodes must be a non-negative integer.")
        self.nodesNum = number_of_nodes
        self.directed = directed
        self.graph = []

        for i in range(number_of_nodes):
            self.graph.append([])
            for j in range(number_of_nodes):
                self.graph[i].append(None)

    def add_or_change_edge(self, u, v, weight=1):
        """Add a new edge or change the weight of an existing edge from node u to node v.

        To remove an edge, set weight = None.
        Behavior may differ depending on whether the graph is directed or not.

        Exception handling:
           Check that 0 <= u, v < number_of_nodes.
           Check that weight is positive number or None (for removal).
           Raise ValueError or IndexError if invalid.

        """
        if self._checkIndex(u) or self._checkIndex(v):
            raise IndexError("Nodes must exists.")
        if weight < 0 and weight is not None:
            raise ValueError("Weight must be non-negative.")

        self.graph[u][v] = weight
        if not self.directed:
            self.graph[v][u] = weight

    def _checkIndex(self, u):
        return u < 0 or u >= self.nodesNum

    def get_edge_weight(self, u, v):
        """Return the weight of the edge from u to v.

        Returns None if the edge does not exist.

        Exception handling:
            Check valid node indices. Raise ValueError or IndexError if invalid.
        """
        if self._checkIndex(u) or self._checkIndex(v):
            raise ValueError("Nodes must exists.")
        return self.graph[u][v]

    def get_number_of_nodes(self):
        """Return the total number of nodes in the graph."""
        return self.nodesNum

    def get_neighbors(self, u):
        """Return a list of all neighbors (reachable nodes) from node u.

        Example: [1, 3, 8]

        Exception handling:
            Raise ValueError or IndexError if u is out of range.
            Return empty list if u has no neighbors.
        """
        out = []

        if self._checkIndex(u):
            raise ValueError("Node must exists.")

        for i in range(self.nodesNum):
            if self.graph[u][i] is not None and u != i:
                out.append(i)
        return out

    def __str__(self):
        """Return a string representation of the graph 
        based on the internal structure (e.g., adjacency matrix or list).
        """
        out = ""
        for i in self.graph:
            out += str(i) + "\n"
        return out

    def get_edges(self):
        """Return a list of all edges in the graph.

        Each edge is represented as a tuple: ((u, v), weight)

        Example output:
        [((0, 1), 1), ((1, 2), 1)]         # directed
        or
        [((0, 1), 1), ((1, 2), 1)]         # undirected (only one per pair, u <= v)
        """
        out = []
        for i in range(self.nodesNum):
            for j in range(1,self.nodesNum):
                if self.graph[i][j] is not None and i != j:
                    out.append(((i, j), self.graph[i][j]))
        return out

    def find_connected_components(self):
        """Return a list of connected components in the undirected graph.

        Each component is represented as a list or set of nodes.

        Example:
            [[0, 2], [1, 3, 7], [4], [5, 6]]
            or
            [{0, 2}, {1, 3, 7}, {4}, {5, 6}]

        Exception handling:
            Raise ValueError if the graph is directed.
        """
        if self.directed:
            raise ValueError("Graph is directed.")

        out = []
        for i in range(self.nodesNum):
            canContinue = True
            for path in out:
                if i in path:
                    canContinue = False
            if canContinue:
                out.append(self.dfs(i, []))

        return out

    def dfs(self, u, out):
        if u in out:
            return out
        out.append(u)
        for i in range(self.nodesNum):
            if self.graph[u][i] is not None and u != i:
                self.dfs(i, out)
        return out
    #
    def shortest_paths(self, start):
        """Compute the shortest paths from a start node to all other nodes using the Dijksra algorithm.

        Returns:
            tuple:
                distances (list): distances[i] is the shortest distance from start to node i (or float('inf')).
                previous (list): previous[i] == j means j is the predecessor of i on the shortest path.

        Example:
            ([0, 1, inf, 2], [0, 0, -1, 1])
            for start node 0 and edges (0, 1), (1, 3).

        Exception handling:
            Raise IndexError or ValueError if start is invalid.
            Check for negative weights (if using Dijkstra, weights must be non-negative). Raise ValueError if invalid.

        """
        ...

#
    def reconstruct_the_shortest_path(self, destination, previous):
        """Return the list of nodes forming the shortest path to node destination.

        'previous' is the list returned by self.shortest_paths(start).

        Example:
            [0, 1, 3] for node 3,
            [] for unreachable node 2
            in a graph with edges (0, 1), (1, 3) and start node 0.

        Exception handling:
            Raise ValueError or IndexError if destination is out of range.
            Check that previous is a list of valid indices or -1. Raise ValueError if invalid.
            Return [] if node is unreachable.
        """
        ...

if __name__ == "__main__":
    g = Graph(6, False)
    g.add_or_change_edge(0, 2)
    g.add_or_change_edge(2, 3)
    g.add_or_change_edge(4, 5)

    print(g)
    print(g.find_connected_components())