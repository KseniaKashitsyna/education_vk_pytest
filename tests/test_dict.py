import pytest


# check del method in dict
def test_valid_dict():
    test_dict = {
        'first': 5,
        'second': -10,
        'third': 15,
    }

    del test_dict['third']

    for key_dict in test_dict.keys():
        assert key_dict != 'third'


# check method pop() in dict
def test_negative_dict():
    test_dict = {
        'first': 5,
        'second': -10,
        'third': 15,
    }

    dict_len = len(test_dict)

    test_dict.pop('third')

    try:
        assert len(test_dict) == dict_len
    except AssertionError:
        pass


# check add different formats to dict
@pytest.mark.parametrize("input_value,expected_result", [({'A': 5, 'B': [1.2,3], 3: 'three', 'four': range(2), 5: {1,2,3}}, 5),
                                                         ({'1': 'test', '2': '', '3': None},  3)])
def test_parametrize_dict(input_value, expected_result):
    dict_for_param_test = {}
    dict_for_param_test.update(input_value)
    assert len(dict_for_param_test) == expected_result