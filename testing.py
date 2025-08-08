from task import List, _Node
import pytest

LIST = List
empty_list = LIST()


def test_node_class():
    """Test _Node class object creation."""

    new_obj = _Node("apple")
    new_obj2= _Node(555, prev=new_obj)
    new_obj.next = new_obj2
    new_obj3= _Node(555, prev=new_obj2)
    new_obj2.next=new_obj3

    assert new_obj.data == "apple"
    assert new_obj.next == new_obj2
    assert new_obj.prev is None
    assert new_obj2.data == 555
    assert new_obj2.next == new_obj3
    assert new_obj2.prev == new_obj

def test_list_class():
    """Test List creation."""

    custom_list_range = LIST(range(1, 10))
    custom_list = LIST((1, 2, "apple"))
    custom_list1 = List((1, 2, "apple"))

    assert str(custom_list_range) == "[1, 2, 3, 4, 5, 6, 7, 8, 9]"
    assert str(custom_list) == "[1, 2, 'apple']"
    assert custom_list1._first_node.data == 1
    assert custom_list1._last_node.data == 'apple'
    assert custom_list1._first_node.next.next == custom_list1._last_node

def test_list_len():
    """Test len()."""

    custom_list = LIST((1, 2, "apple"))
    
    assert custom_list.__len__() == 3
    assert empty_list.__len__() == 0

def test_list_append_extend():
    """"""

    custom_list = LIST((1, 2, "apple"))
    custom_list2 = LIST(("a", "b", 777))

    assert len(custom_list) == 3
    assert custom_list.append(999) == None
    assert len(custom_list) == 4
    assert str(custom_list) == "[1, 2, 'apple', 999]"
    assert custom_list.extend((71, "pear", None)) == None
    assert len(custom_list) == 7
    assert str(custom_list) == "[1, 2, 'apple', 999, 71, 'pear', None]"

    custom_list.extend(custom_list2)
    assert str(custom_list) == "[1, 2, 'apple', 999, 71, 'pear', None, 'a', 'b', 777]"
    assert len(custom_list) == 10

def test_set_item():
    """"""

    custom_list = LIST((1, 2, "apple"))
    custom_list2 = LIST(("a", "b", 777))
    
    custom_list[0] = 888
    custom_list2[-1] = "xxx"
    
    assert custom_list[0] == 888
    assert custom_list2[-1] == "xxx"

    with pytest.raises(IndexError):
        custom_list[0] == 888
        empty_list[0]
        custom_list[5]

def test_del_item():
    custom_list = LIST((1, 2, "apple"))
    custom_list2 = LIST(("a", "b", 777))

    assert len(custom_list) == 3
    assert len(custom_list2) == 3

    custom_list.__delitem__(0)

    assert str(custom_list) == "[2, 'apple']"
    assert len(custom_list) == 2
    assert len(custom_list) == 2

    custom_list2.__delitem__(-1)

    assert str(custom_list2) == "['a', 'b']"
    assert len(custom_list2) == 2

    custom_list3 = LIST((1, 2, "apple", 999, 71, "pear", None, "a", "b", 777))
    assert len(custom_list3) == 10

    custom_list3.__delitem__(6)
    assert len(custom_list3) == 9
    assert str(custom_list3) == "[1, 2, 'apple', 999, 71, 'pear', 'a', 'b', 777]"

    custom_list3.__delitem__(-3)
    assert len(custom_list3) == 8
    assert str(custom_list3) == "[1, 2, 'apple', 999, 71, 'pear', 'b', 777]"
    assert custom_list3[-4] == 71
    assert custom_list3[2] == "apple"

def test_insert():
    """"""

    custom_list = LIST((1, 2, "apple"))

    custom_list.insert(0, "insert1")
    assert custom_list[0] == "insert1"
    assert str(custom_list) == "['insert1', 1, 2, 'apple']"

    custom_list.insert(5, "insert5")
    assert str(custom_list) == "['insert1', 1, 2, 'apple', 'insert5']"

    custom_list.insert(-1, "insert_last")
    assert str(custom_list) == "['insert1', 1, 2, 'apple', 'insert_last', 'insert5']"
    assert custom_list[-1] == "insert5"

def test_insert():
    """"""

    custom_list = List((1, 2))

    custom_list.insert(0, "insert1")
    custom_list.insert(4, "insert5")
    custom_list.insert(-1, "insert_last")
    assert str(custom_list) == "['insert1', 1, 2, 'insert_last', 'insert5']"
    assert custom_list._first_node.prev is None
    assert custom_list._first_node.next.data == 1
    assert custom_list._last_node.next is None
    assert custom_list._last_node.prev.data == 'insert_last'
    assert custom_list._first_node.next.data == 1
    assert custom_list._first_node.next.next.data == 2
    assert custom_list._first_node.next.next.next.data == 'insert_last'
    assert custom_list._first_node.next.next.next.next.data == 'insert5'

def test_remove():
    custom_list2 = LIST((1, 2, "apple", 2))

    custom_list2.remove("apple")
    assert str(custom_list2) == "[1, 2, 2]"
    assert len(custom_list2) == 3
    custom_list2.remove(1)
    assert str(custom_list2) == "[2, 2]"
    assert len(custom_list2) == 2

def test_pop():
    custom_list = LIST((1, 2, "apple"))
    custom_list2 = LIST((1, 2, "apple", 2))
    
    assert custom_list.pop() == "apple"
    assert str(custom_list) == "[1, 2]"
    assert len(custom_list) == 2

    assert custom_list.pop(1) == 2
    assert str(custom_list) == "[1]"
    assert len(custom_list) == 1

    assert custom_list2.pop(0) == 1
    assert str(custom_list2) == "[2, 'apple', 2]"
    assert len(custom_list2) == 3

def test_clear():
    custom_list = LIST((1, 2, "apple"))
    custom_list.clear()

    assert len(custom_list) == 0
    assert str(custom_list) == "[]"

    custom_list2 = LIST((1, 2, "apple"))
    del custom_list2[:]
    assert len(custom_list2) == 0
    assert str(custom_list2) == "[]"

def test_count_contains():
    custom_list2 = LIST((1, 2, 2, "apple", 2, 2, None))

    assert custom_list2.count(2) == 4
    assert 2 in custom_list2
    assert custom_list2.count("apple") == 1
    assert custom_list2.count(None) == 1
    assert custom_list2.count(0) == 0
    assert 0 not in custom_list2

def test_iter():
    """"""

    custom_list2 = LIST(("a", "b", 777))

    assert [data for data in custom_list2] == ["a", "b", 777]
    assert [data for data in empty_list] == []

def test_index():
    custom_list2 = LIST((1, 2, 2, "apple", 2, 2, None))

    assert custom_list2.index("apple") == 3
    assert custom_list2.index(2) == 1
    with pytest.raises(ValueError):
        custom_list2.index(888)
        custom_list2.index("apple", 4)
        assert custom_list2.index(2, -1)
    
    assert custom_list2.index(2, 3) == 4
    assert custom_list2.index(2, 2) == 2
    assert custom_list2.index(2, 0, -1) == 1
    assert custom_list2.index(None, -3) == 6
    assert custom_list2.index(None, 4) == 6
    assert custom_list2.index("apple", 3) == 3

def test_reverse():
    custom_list2 = LIST((1, "apple", 2))
    
    assert str(custom_list2) == "[1, 'apple', 2]"
    custom_list2.reverse()
    assert str(custom_list2) == "[2, 'apple', 1]"

def test_copy():
    custom_list = LIST((1, 2, "apple"))
    copy_list = custom_list.copy()

    assert str(copy_list) == str(custom_list)
    assert id(copy_list) != id(custom_list)

def test_getitem():
    """Test __getitem__."""

    custom_list = LIST((1, 2, "apple"))

    assert custom_list[0] == 1
    assert custom_list[1] == 2
    assert custom_list[2] == "apple"
    assert custom_list[-1] == "apple"
    assert custom_list[-2] == 2

    with pytest.raises(IndexError):
        empty_list[0]
        custom_list[5]

    custom_list2 = LIST((1, 2, "apple"))

    # start idx
    assert str(custom_list2[0::]) == "[1, 2, 'apple']"
    assert str(custom_list2[1::]) == "[2, 'apple']"
    assert str(custom_list2[2::]) == "['apple']"
    assert str(custom_list2[3::]) == "[]"

    # stop idx
    assert str(custom_list2[:0:]) == "[]"
    assert str(custom_list2[:1:]) == "[1]"
    assert str(custom_list2[:2:]) == "[1, 2]"
    assert str(custom_list2[:3:]) == "[1, 2, 'apple']"

    # step
    assert str(custom_list2[0:2:2]) == "[1]"
    assert str(custom_list2[1::2]) == "[2]"
    assert str(custom_list2[2::2]) == "['apple']"
    assert str(custom_list2[::2]) == "[1, 'apple']"

def test_eq_add_mul():
    custom_list1 = LIST((1, 2, "apple"))
    custom_list2 = LIST((1, 2, "apple"))

    assert custom_list1 == custom_list2

    custom_list3 = custom_list1 + custom_list2
    assert str(custom_list3) == "[1, 2, 'apple', 1, 2, 'apple']"

    custom_list4 = custom_list1 + custom_list2 + custom_list3
    assert str(custom_list4) == "[1, 2, 'apple', 1, 2, 'apple', 1, 2, 'apple', 1, 2, 'apple']"

    custom_list4 = custom_list1 * 3
    assert str(custom_list4) == "[1, 2, 'apple', 1, 2, 'apple', 1, 2, 'apple']"

def test_append_slice():
    custom_list2 = LIST((1, 2, "apple"))
    custom_list2[len(custom_list2):] = [555]

    custom_list3 = LIST((1, 2, "apple"))
    custom_list3[len(custom_list2):] = [888, 777]

    assert str(custom_list2) == "[1, 2, 'apple', 555]"
    assert str(custom_list3) == "[1, 2, 'apple', 888, 777]"

def test_slicing():
    custom_list = LIST((0, 1, 2, 3, 4, 5))

    assert str(custom_list[1:4]) == "[1, 2, 3]"
    assert str(custom_list[:3]) == "[0, 1, 2]"
    assert str(custom_list[3:]) == "[3, 4, 5]"
    assert str(custom_list[:]) == str(custom_list)

def test_negative_indices():
    custom_list = LIST((10, 20, 30, 40, 50))

    assert str(custom_list[-1]) == "50"
    assert str(custom_list[-3:-1]) == "[30, 40]"
    assert str(custom_list[:-2]) == "[10, 20, 30]"

def test_step_slicing():
    custom_list = LIST((0, 1, 2, 3, 4, 5, 6))

    assert str(custom_list[::2]) == "[0, 2, 4, 6]"
    assert str(custom_list[1::2]) == "[1, 3, 5]"
    # assert str(custom_list[::-1]) == "[6, 5, 4, 3, 2, 1, 0]"

def test_edge_cases():
    custom_list = LIST((1, 2, 3))

    assert str(custom_list[10:]) == "[]"
    assert str(custom_list[:10]) == "[1, 2, 3]"
    assert str(custom_list[-10:]) == "[1, 2, 3]"
    assert str(custom_list[1:1]) == "[]"

def test_empty_list():
    custom_list = LIST()

    assert str(custom_list[:]) == "[]"
    assert str(custom_list[1:3]) == "[]"
    assert str(custom_list[::-1])== "[]"

