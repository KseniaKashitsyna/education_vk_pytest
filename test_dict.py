import pytest

test_dict = {
    'first': 5,
    'second': -10,
    'third': 15,
}

def test_valid_dict():
    del test_dict['third']

    for key_dict in test_dict.keys():
        assert key_dict != 'third'


def test_negative_dict():
    for val_dict in test_dict.values():
        try:
            assert val_dict > 0
        except AssertionError:
            pass


@pytest.mark.parametrize("input_value,expected_result", [({'A': 5, 'B': [1.2,3], 3: 'three', 'four': range(2), 5: {1,2,3}}, 5),
                                                         ({'1': 'test', '2': '', '3': None},  3)])
def test_parametrize_dict(input_value, expected_result):
    dict_for_param_test = {}
    dict_for_param_test.update(input_value)
    assert len(dict_for_param_test) == expected_result