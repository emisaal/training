from task import List, Node
import pytest

empty_list = List()


def test_node_class():
    """Test Node class object creation."""

    new_obj = Node("apple", 5)
    new_obj2= Node(555, 66, new_obj)
    assert new_obj.data == "apple"
    assert new_obj.index == 5
    assert new_obj.next == None
    assert new_obj2.data == 555
    assert new_obj2.index == 66
    assert new_obj2.next == new_obj

def test_list_class():
    """Test List creation."""

    custom_list = List(1, 2, "apple")

    assert str(empty_list) == '[]'
    assert empty_list._first_node == None
    assert custom_list._first_node.data == 1
    assert str(custom_list) == '[1, 2, apple]'

def test_list_len():
    """Test len()."""

    custom_list = List(1, 2, "apple")
    
    assert len(custom_list) == 3
    assert len(empty_list) == 0

def test_list__getitem__():
    """Test __getitem__."""

    custom_list = List(1, 2, "apple")

    assert custom_list.__getitem__(0) == 1
    assert custom_list.__getitem__(1) == 2
    assert custom_list.__getitem__(2) == 'apple'

    with pytest.raises(IndexError):
        empty_list.__getitem__(0)
        custom_list.__getitem__(5)

def test_list_append():
    """"""

    custom_list = List(1, 2, "apple")

    assert custom_list.append(999) == None
    assert str(custom_list) == '[1, 2, apple, 999]'

