import pytest

from node_graph import NodeEdgeGraph
import scheduler as s

# Some constants we can use for labs (to save on typing)
lab1 = "Lab 1"
lab2 = "Lab 2"
lab3 = "Lab 3"
lab4 = "Lab 4"

# ############## Helper methods for writing tests #############
def add_simple_nodes(graph):
    graph.add_node(lab1)
    graph.add_node(lab2)
    graph.add_node(lab3)
    graph.add_node(lab4)

def add_simple_edges(graph):
    graph.add_undirected_edge(lab1, lab2)
    graph.add_undirected_edge(lab2, lab3)

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
    assert s.check_validity(g, schedule) is True

def test_schedule_invalid():
    g = make_simple("a graph")
    g.add_undirected_edge(lab3, lab1)

    with pytest.raises(s.NoScheduleError):
        s.find_schedule(g)