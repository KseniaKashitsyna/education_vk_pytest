import pytest


# Check reverse function of list
def test_valid_reverse_list():
    test_list_of_number = [1, 2, 3]
    revert_test_list = [3, 2, 1]
    test_list_of_number.reverse()
    assert test_list_of_number == revert_test_list


# check function of clear list
def test_negative_len_list():
    test_list_of_number = [1, 2, 3]
    len_list = len(test_list_of_number)
    test_list_of_number.clear()
    try:
        assert len(test_list_of_number) == len_list
    except AssertionError:
        pass


# check add in list different formats of data
@pytest.mark.parametrize("input_value,expected_size", [(('Andy', 'Samm'), 1), ('', 1), (range(3), 1), ({1:'1', 2:'2'}, 1)])
def test_parametrize_list(input_value, expected_size):
    test_list = []

    test_list.append(input_value)
    assert len(test_list) == expected_size