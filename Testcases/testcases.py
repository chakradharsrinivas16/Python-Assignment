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
def object_1():
    obj_1=Solution('X','O',4,4)
    return obj_1

def test_given_input(object_1):
    
    # Test case 2
    object_1.board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    expected_output = [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
    if(object_1.validator()):
        object_1.solve_bfs()
        assert object_1.board == expected_output
        object_1.board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
        object_1.solve_dfs()
        assert object_1.board == expected_output
    else:
        print(f"Invalid entries, Please enter again.")
def test_random_input(object_1):
    
    # Test case 3
    object_1.board = [["X","O","X","O"],["O","X","O","X"],["X","O","X","O"],["O","X","O","X"]]
    expected_output = [["X","O","X","O"],["O","X","X","X"],["X","X","X","O"],["O","X","O","X"]]
    if(object_1.validator()):
        object_1.solve_bfs()
        assert object_1.board == expected_output
        object_1.board = [["X","O","X","O"],["O","X","O","X"],["X","O","X","O"],["O","X","O","X"]]
        object_1.solve_dfs()
        assert object_1.board == expected_output
    else:
        print(f"Invalid entries, Please enter again.")
def test_no_border_Os(object_1):
    
    # Test case 4
    object_1.board = [["X","X","X","X"],["X","O","X","X"],["X","X","X","X"],["X","X","X","X"]]
    expected_output = [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","X","X","X"]]
    if(object_1.validator()):
        object_1.solve_bfs()
        assert object_1.board == expected_output
        object_1.board = [["X","X","X","X"],["X","O","X","X"],["X","X","X","X"],["X","X","X","X"]]
        object_1.solve_dfs()
        assert object_1.board == expected_output
    else:
        print(f"Invalid entries, Please enter again.")

@pytest.fixture
def object_2():
    obj_2=Solution('X','O',1,1)
    return obj_2

def test_single_elementO(object_2):    
    # Test case 5: single element board
    object_2.board = [["O"]]
    expected_output = [["O"]]
    if(object_2.validator()):
        object_2.solve_bfs()
        assert object_2.board == expected_output
        object_2.board = [["O"]]
        object_2.solve_dfs()
        assert object_2.board == expected_output
    else:
        print(f"Invalid entries, Please enter again.")

def test_single_elementX(object_2):    
    # Test case 6: single element board
    object_2.board = [["X"]]
    expected_output = [["X"]]
    if(object_2.validator(board)):
        object_2.solve_bfs()
        assert object_2.board == expected_output
        object_2.board = [["X"]]
        object_2.solve_dfs()
        assert object_2.board == expected_output
    else:
        print(f"Invalid entries, Please enter again.")

@pytest.fixture
def object_3():
    obj_3=Solution('X','O',3,3)
    return obj_3

def test_single_elementO(object_3):    
    # Test case 7: All elements are 'X's
    object_3.board = [["X","X","X"],["X","X","X"],["X","X","X"]]
    expected_output = [["X","X","X"],["X","X","X"],["X","X","X"]]
    if(object_3.validator()):
        object_3.solve_bfs()
        assert object_3.board == expected_output
        object_3.board = [["X","X","X"],["X","X","X"],["X","X","X"]]
        object_3.solve_dfs()
        assert object_3.board == expected_output
    else:
        print(f"Invalid entries, Please enter again.")

def test_single_elementX(object_3):    
    # Test case 8: All elements as 'O's
    object_3.board = [["O","O","O"],["O","O","O"],["O","O","O"]]
    expected_output = [["O","O","O"],["O","O","O"],["O","O","O"]]
    if(object_3.validator()):
        object_3.solve_bfs()
        assert object_3.board == expected_output
        object_3.board = [["O","O","O"],["O","O","O"],["O","O","O"]]
        object_3.solve_dfs()
        assert object_3.board == expected_output
    else:
        print(f"Invalid entries, Please enter again.")

def test_invalid_entries(object_3):    
    # Test case 9: board with invalid entries
    object_3.board = [["C","X","O"],["X","X","X"],["X","X","X"]]
    with pytest.raises(Exception):
        object_3.validateInput()

def test_invalid_shape(object_3):    
    # Test case 10: board with invalid entries
    board = [["X","X","O"],["X","X"],["X"]]
    with pytest.raises(Exception):
        object_3.validateInput()
