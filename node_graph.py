class NodeEdgeGraph:

    # ---------- The Node class --------------------
    class Node:
        def __init__(self, label: str):
            self.label = label
            self._next_nodes = [] # Empty list (ArrayList)

        def has_edge(self, node) -> bool:
            return node in self._next_nodes

        def add_edge(self, node):
            self._next_nodes.append(node)

        
    # -------------------------------------------

    def __init__(self, graph_name: str):
        self.name = graph_name
        
        # Create an empty dict (Hashmap) of string -> Node
        self._all_nodes = {}  # type: dict[str,Node]
        
    def get_node(self, label: str, create=False) -> Node:
        """
        Retrieve a node object for a label

        Parameters:
            label  -- the label for the node we want
            create -- if create=True, node will be created if it doesn't exist,
                      otherwise, will raise ValueError if node is missing (default)
                      (This is a "keyword argument", used to create optional arguments)
        """
        if label not in self._all_nodes:
            if create:
                self.add_node(label)
            else:
                raise ValueError(f"Node {label} does not exist")
            
        return self._all_nodes[label]

    def add_node(self, label: str):
        """
        Add a node to the graph.  Throws ValueError if the node already exists.

        Parameters:
            label -- label for the node to add
        """
        if label in self._all_nodes:
            raise ValueError(f"Node {label} already exists in graph")

        new_node = self.Node(label)  # Could also just write Node(label)
        self._all_nodes[label] = new_node

    def add_directed_edge(self, label1: str, label2: str):
        """
        Add a directed edge from label1 -> label2

        Parameters:
            label1 -- label for the starting edge ("from here")
            label2 -- label for the ending edge ("to here")
        """
        # Find the nodes, create them if they don't exist
        node1 = self.get_node(label1, create=True)
        node2 = self.get_node(label2, create=True)

        if not node1.has_edge(node2):
            node1.add_edge(node2)
        
    def add_undirected_edge(self, label1, label2):
        """
        Add an undirected edge from label1 -> label2

        Parameters:
            label1 -- label for the starting edge ("from here")
            label2 -- label for the ending edge ("to here")
        """
        self.add_directed_edge(label1, label2)
        self.add_directed_edge(label2, label1)

    def get_neighbors(self, from_node: str) -> set[str]:
        """
        Get the the labels for all neighbors for a node

        Parameters
            from_node -- The node 
        """
        node = self.get_node(from_node)  # throws ValueError if node doesn't exist

        neighbors = set()
        for n in node._next_nodes:
            neighbors.add(n.label)
        
        return neighbors

    def get_all_nodes(self):
        """
        Get a list of all node names
        """
        result = set()

        for k in self._all_nodes.keys():
            result.add(k)
        
        return result  