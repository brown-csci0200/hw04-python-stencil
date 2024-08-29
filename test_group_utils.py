import pytest
import copy

import group_utils as g

example_person_list = [
    {"name": "Sebastian", "time in group": 2.3, "skills": ["sleeping", "screeching"]},
    {"name": "Claire", "time in group": 0.2, "skills": ["coding", "science", "breathing"]},
    {"name": "Cathy", "time in group": 2.3, "skills": ["eating", "sleeping"]}
]

# test_group = ... # This variable is set up by setup_function()

def setup_function():
    """
    This is a function tht runs **before each test**, similar to @Before
    in Java.  We use this to set up some data (the variable test_group)
    which we can use in our tests
    """
    # set test_group as global so that other methods can find it
    global test_group

    # copy.deepcopy makes a brand-new copy of example_person_list
    # and every piece of data contained in it on the heap
    test_group = g.Group(copy.deepcopy(example_person_list))
    # now we can use and refer to test_group in any test function in this file

# TODO:  Write your tests here!

##############################################################################
# EXAMPLE TEST:  Here's an example of how to write assertions with pytest
# Some important things to note
#  - pytest assertions simply check if boolean expressions evaluate to true
#  - Make sure ALL of your testing functions start with "test_" and are in a 
#    file that starts with "test_".  If you don't do this, pytest won't work!
##############################################################################
def test_example():
    assert 2 == 2

    # use pytest.approx for decimal numbers
    assert 2.5 == pytest.approx(5 / 2)

    # since test_group was declared global and initialized in setup_function, we can call
    # its methods here
    assert test_group.measure_progress("Claire") == pytest.approx(3 / 0.2)

    # testing for exceptions:
    with pytest.raises(LookupError):
        test_group.measure_progress("Caroline")

    # assertions on lists
    assert "a" in ["a", "b", "c"]
    assert "d" not in ["a", "b", "c"]
    assert len(["a", "b", "c"]) == 3

    false_boolean_expression = False
    assert not false_boolean_expression

    # value equality (==) vs. same object on the heap (is)
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    list3 = list1
    assert list1 == list2
    assert list2 == list3
    assert list1 == list3
    assert list1 is list3
    assert not (list1 is list2) # list1 and list2 are different objects on the heap
    list4 = list(list1) # makes a copy of list1 in a new location on the heap
    assert list4 == list1
    assert not(list4 is list1)
    