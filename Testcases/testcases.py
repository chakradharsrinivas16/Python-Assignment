import pytest
import Pythonassignment_tc
from Pythonassignment_tc import Solution


def test_empty_list():
    # Test case 1
    board=[]
    Object=Solution('X','O',0,0)
    with pytest.raises(Exception):
        Object.validator(board)

@pytest.fixture
def object1():
    obj1=Solution('X','O',4,4)
    return obj1

def test_given_input(object1):
    
    # Test case 2
    object1.board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    expected_output = [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
    if(object1.validator()):
        object1.solve_bfs()
        assert object1.board == expected_output
        object1.board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
        object1.solve_dfs()
        assert object1.board == expected_output
    else:
        print(f"Invalid entries, Please enter again.")
def test_random_input(object1):
    
    # Test case 3
    object1.board = [["X","O","X","O"],["O","X","O","X"],["X","O","X","O"],["O","X","O","X"]]
    expected_output = [["X","O","X","O"],["O","X","X","X"],["X","X","X","O"],["O","X","O","X"]]
    if(object1.validator()):
        object1.solve_bfs()
        assert object1.board == expected_output
        object1.board = [["X","O","X","O"],["O","X","O","X"],["X","O","X","O"],["O","X","O","X"]]
        object1.solve_dfs()
        assert object1.board == expected_output
    else:
        print(f"Invalid entries, Please enter again.")
def test_no_border_Os(object1):
    
    # Test case 4
    object1.board = [["X","X","X","X"],["X","O","X","X"],["X","X","X","X"],["X","X","X","X"]]
    expected_output = [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","X","X","X"]]
    if(object1.validator()):
        object1.solve_bfs()
        assert object1.board == expected_output
        object1.board = [["X","X","X","X"],["X","O","X","X"],["X","X","X","X"],["X","X","X","X"]]
        object1.solve_dfs()
        assert object1.board == expected_output
    else:
        print(f"Invalid entries, Please enter again.")

@pytest.fixture
def object2():
    obj2=Solution('X','O',1,1)
    return obj2

def test_single_elementO(object2):    
    # Test case 5: single element board
    object2.board = [["O"]]
    expected_output = [["O"]]
    if(object2.validator()):
        object2.solve_bfs()
        assert object2.board == expected_output
        object2.board = [["O"]]
        object2.solve_dfs()
        assert object2.board == expected_output
    else:
        print(f"Invalid entries, Please enter again.")

def test_single_elementX(object2):    
    # Test case 6: single element board
    object2.board = [["X"]]
    expected_output = [["X"]]
    if(object2.validator(board)):
        object2.solve_bfs()
        assert object2.board == expected_output
        object2.board = [["X"]]
        object2.solve_dfs()
        assert object2.board == expected_output
    else:
        print(f"Invalid entries, Please enter again.")

@pytest.fixture
def object3():
    obj3=Solution('X','O',3,3)
    return obj3

def test_single_elementO(object3):    
    # Test case 7: All elements are 'X's
    object3.board = [["X","X","X"],["X","X","X"],["X","X","X"]]
    expected_output = [["X","X","X"],["X","X","X"],["X","X","X"]]
    if(object3.validator()):
        object3.solve_bfs()
        assert object3.board == expected_output
        object3.board = [["X","X","X"],["X","X","X"],["X","X","X"]]
        object3.solve_dfs()
        assert object3.board == expected_output
    else:
        print(f"Invalid entries, Please enter again.")

def test_single_elementX(object3):    
    # Test case 8: All elements as 'O's
    object3.board = [["O","O","O"],["O","O","O"],["O","O","O"]]
    expected_output = [["O","O","O"],["O","O","O"],["O","O","O"]]
    if(object3.validator()):
        object3.solve_bfs()
        assert object3.board == expected_output
        object3.board = [["O","O","O"],["O","O","O"],["O","O","O"]]
        object3.solve_dfs()
        assert object3.board == expected_output
    else:
        print(f"Invalid entries, Please enter again.")

def test_invalid_entries(object3):    
    # Test case 9: board with invalid entries
    object3.board = [["C","X","O"],["X","X","X"],["X","X","X"]]
    with pytest.raises(Exception):
        object3.validateInput()

def test_invalid_shape(object3):    
    # Test case 10: board with invalid entries
    board = [["X","X","O"],["X","X"],["X"]]
    with pytest.raises(Exception):
        object3.validateInput()



print("All Passed")
