import pytest

from node_graph import NodeEdgeGraph
import scheduler as s

# Some constants we can use for nodes (to save on typing)
n_a = "Node A"
n_b = "Node B"
n_c = "Node C"
n_d = "Node D"

# Some constants for labs (to save on typing)
lab1 = "Lab 1"
lab2 = "Lab 2"
lab3 = "Lab 3"
lab4 = "Lab 4"

# ############## Helper methods for writing tests #############
def add_simple_nodes(graph):
    graph.add_node(n_a)
    graph.add_node(n_b)
    graph.add_node(n_c)
    graph.add_node(n_d)

def add_simple_edges(graph):
    graph.add_undirected_edge(n_a, n_b)
    graph.add_undirected_edge(n_b, n_c)

def make_simple(graph_name: str) -> NodeEdgeGraph:
    graph = NodeEdgeGraph(graph_name)
    add_simple_nodes(graph)
    add_simple_edges(graph)
    return graph

##################################################################

def test_check_validity_true():
    g = make_simple("a graph")

    proposed_schedule = [
        {lab1, lab3, lab4}, # <--- Using curly brackets here creates a set
        {lab2},             #      a set (HashSet) instead of a list
    ]
    
    assert s.check_validity(g, proposed_schedule) is True

def test_check_validity_false():
    g = make_simple("a graph")

    proposed_schedule = [
        {lab3, lab4},
        {lab1, lab2},
    ]
    
    assert s.check_validity(g, proposed_schedule) is False

def test_find_schedule_valid():
    g = make_simple("a graph")
    schedule = s.find_schedule(g)
    assert s.check_validity(schedule) is True

def test_schedule_invalid():
    g = make_simple("a graph")
    g.add_undirected_edge(lab3, lab1)

    with pytest.raises(s.NoScheduleError):
        s.find_schedule(g)