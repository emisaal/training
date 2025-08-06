from task import List, _Node
import pytest

empty_list = List()


def test_node_class():
    """Test _Node class object creation."""

    new_obj = _Node("apple")
    new_obj2= _Node(555, new_obj)

    assert new_obj.data == "apple"
    assert new_obj.next == None
    assert new_obj2.data == 555
    assert new_obj2.next == new_obj

def test_list_class():
    """Test List creation."""

    custom_list = List((1, 2, "apple"))

    assert str(empty_list) == '[]'
    assert empty_list._first_node == None
    assert custom_list._first_node.data == 1
    assert str(custom_list) == '[1, 2, apple]'

def test_list_len():
    """Test len()."""

    custom_list = List((1, 2, "apple"))
    
    assert custom_list.__len__() == 3
    assert empty_list.__len__() == 0

def test_list__getitem__():
    """Test __getitem__."""

    custom_list = List((1, 2, "apple"))

    assert custom_list.__getitem__(0) == 1
    assert custom_list.__getitem__(1) == 2
    assert custom_list.__getitem__(2) == 'apple'
    assert custom_list[0] == 1
    assert custom_list[1] == 2
    assert custom_list[2] == 'apple'
    assert custom_list[-1] == 'apple'
    assert custom_list[-2] == 2

    with pytest.raises(IndexError):
        empty_list.__getitem__(0)
        custom_list.__getitem__(5)
        empty_list[0]
        custom_list[5]

    custom_list2 = List((1, 2, "apple"))

    # start idx
    assert custom_list2[0::] == '[1, 2, apple]'
    assert custom_list2[1::] == '[2, apple]'
    assert custom_list2[2::] == '[apple]'
    assert custom_list2[3::] == '[]'

    # stop idx

    
    # step

def test_list_append_extend():
    """"""

    custom_list = List((1, 2, "apple"))
    custom_list2 = List(("a", "b", 777))

    assert custom_list.__len__() == 3
    assert custom_list.append(999) == None
    assert custom_list.__len__() == 4
    assert str(custom_list) == '[1, 2, apple, 999]'
    assert custom_list.extend((71, "pear", None)) == None
    assert custom_list.__len__() == 7
    assert str(custom_list) == '[1, 2, apple, 999, 71, pear, None]'

    custom_list.extend(custom_list2)
    assert str(custom_list) == '[1, 2, apple, 999, 71, pear, None, a, b, 777]'
    assert custom_list.__len__() == 10

def test_set_item():
    """"""

    custom_list = List((1, 2, "apple"))
    custom_list2 = List(("a", "b", 777))
    
    custom_list[0] = 888
    custom_list2[-1] = "xxx"
    
    assert custom_list[0] == 888
    assert custom_list2[-1] == "xxx"

    with pytest.raises(IndexError):
        custom_list[0] == 888
        custom_list.__getitem__(5)
        empty_list[0]
        custom_list[5]

def test_iter():
    """"""

    custom_list2 = List(("a", "b", 777))

    assert [[data] for data in custom_list2] == [['a'], ['b'], [777]]
    assert [[data] for data in empty_list] == []

def test_del_item():
    custom_list = List((1, 2, "apple"))
    custom_list2 = List(("a", "b", 777))

    assert custom_list.__len__() == 3
    assert custom_list2.__len__() == 3

    custom_list.__delitem__(0)

    assert str(custom_list) == '[2, apple]'
    assert custom_list.__len__() == 2
    assert len(custom_list) == 2

    custom_list2.__delitem__(-1)

    assert str(custom_list2) == '[a, b]'
    assert custom_list2.__len__() == 2

    custom_list3 = List((1, 2, 'apple', 999, 71, 'pear', None, 'a', 'b', 777))
    assert custom_list3.__len__() == 10

    custom_list3.__delitem__(6)
    assert custom_list3.__len__() == 9
    assert str(custom_list3) == '[1, 2, apple, 999, 71, pear, a, b, 777]'

    custom_list3.__delitem__(-3)
    assert custom_list3.__len__() == 8
    assert str(custom_list3) == '[1, 2, apple, 999, 71, pear, b, 777]'
    assert custom_list3[-4] == 71
    assert custom_list3[2] == 'apple'


def test_insert():
    """"""

    custom_list = List((1, 2, "apple"))

    custom_list.insert(0, 'insert1')
    assert custom_list[0] == 'insert1'
    assert str(custom_list) == '[insert1, 1, 2, apple]'

    with pytest.raises(IndexError):
        custom_list.insert(5, 'insert5')

    custom_list.insert(-1, 'insert_last')
    assert custom_list[-1] == 'insert_last'
    assert str(custom_list) == '[insert1, 1, 2, apple, insert_last]'

    custom_list.insert(2, 'insert2')
    assert str(custom_list) == '[insert1, 1, insert2, 2, apple, insert_last]'
    
def test_remove():
    """"""

    custom_list = List((1, 2, "apple"))
    custom_list2 = List((1, 2, "apple", 2))

    custom_list.remove(2)
    assert str(custom_list) == '[1, apple]'

    assert custom_list2.remove('apple') == None
    assert str(custom_list2) == '[1, 2, 2]'

def test_pop():
    """"""

    custom_list = List((1, 2, "apple"))
    custom_list2 = List((1, 2, "apple", 2))
    
    assert custom_list.pop() == 'apple'
    assert str(custom_list) == '[1, 2]'
    assert custom_list.__len__() == 2

    assert custom_list.pop(1) == 2
    assert str(custom_list) == '[1]'
    assert custom_list.__len__() == 1

    assert custom_list2.pop(0) == 1
    assert str(custom_list2) == '[2, apple, 2]'
    assert custom_list2.__len__() == 3

def test_clear():
    """"""
    custom_list = List((1, 2, "apple"))
    custom_list.clear()
    assert len(custom_list) == 0
    assert str(custom_list) == '[]'

def test_count_contains():
    """"""

    custom_list = List((1, 2, "apple"))
    
    assert custom_list.count(2) == 1
    assert custom_list.__contains__(2) == True
    assert custom_list.count('apple') == 1
    assert custom_list.count(999) == 0
    assert custom_list.__contains__(999) == False

    custom_list2 = List((1, 2, 2, "apple", 2, 2, None))

    assert custom_list2.count(2) == 4
    assert custom_list2.__contains__(2) == True
    assert custom_list2.count(None) == 1
    assert custom_list2.count(0) == 0
    assert custom_list2.__contains__(0) == False
