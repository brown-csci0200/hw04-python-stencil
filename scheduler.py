from node_graph import NodeEdgeGraph


def check_validity(graph, proposed_alloc: list[set[str]]):
    """
    Check if a given allocation of labs adheres to the scheduling
    constraints for this graph.  Assumes that all lab names in
    proposed_alloc are valid labels in the graph.

    Returns true if the proposed allocation is valid

    Parameters:
        graph -- The graph to try to schedule
        proposed_alloc -- The proposed allocation of labs between profs
    """
    
    # TODO: Implement!
    # (NotImplementedError is a common way to denote unfinished code in Python.)
    raise NotImplementedError("TODO") # Remove this when you are ready to test!


def find_schedule(graph):
    """
    Compute a valid split of the graph nodes without violating the
    scheduling constraints, if such a split exists.
    Throws a NoScheduleError if no such split exists.
    """

    # TODO: Implement!
    raise NotImplementedError("TODO") # Remove this when you are ready to test!


class NoScheduleError(Exception):
    """
    Exception class for when a schedule is not found
    """
    pass # (No implementation here, since we just extend the builtin Exception class)