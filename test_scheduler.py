import pytest

from node_graph import NodeEdgeGraph
import scheduler as s

# Some constants for labs (to save on typing)
# Feel free to add more!
lab1 = "Lab 1"
lab2 = "Lab 2"
lab3 = "Lab 3"
lab4 = "Lab 4"


def make_simple(graph_name: str) -> NodeEdgeGraph:
    """
    Make a simple graph for testing
    """
    g = NodeEdgeGraph(graph_name)
    g.add_node(lab1)
    g.add_node(lab2)
    g.add_node(lab3)
    g.add_node(lab4)
    return g
    

##############################################
#  Examples for using sets and NodeEdgeGraph
##############################################
def test_get_neighbors():
    g = make_simple("a graph")
    g.add_undirected_edge(lab1, lab2)
    g.add_undirected_edge(lab2, lab3)
    g.add_undirected_edge(lab1, lab3)

    lab1_neighbors = g.get_neighbors(lab1)
    expected_neighbors = {lab2, lab3} # <--- Use curly brackets to make a set instead of a list
    assert lab1_neighbors == expected_neighbors
    
    assert g.get_neighbors(lab4) == set() # Empty set

    g.add_undirected_edge(lab4, lab1)
    assert g.get_neighbors(lab4) == {lab1}

def test_get_all_nodes():
    g = make_simple("a graph")
    assert g.get_all_nodes() == {lab1, lab2, lab3, lab4}

    g2 = NodeEdgeGraph("")
    assert g2.get_all_nodes() == set()

##############################################
#           Example Scheduler tests 
##############################################
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

# TODO:  Add your tests here!