import pytest

test_list_of_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_valid_list():
    for val in test_list_of_number:
        assert type(val) is int


def test_negative_list():
    for val in test_list_of_number:
        try:
            assert val % 2 is 0
        except AssertionError:
            pass


@pytest.mark.parametrize("input_value,expected_result", [(['Andy', 'Samm'], 4), ([''], 0)])
def test_parametrize_list(input_value, expected_result):
    for val in input_value:
        assert len(val) == expected_result