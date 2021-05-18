from main import reverse_list


def test_reverse_even():
    actual = reverse_list([1, 2, 3, 4])
    expected = [4, 3, 2, 1]
    assert actual == expected
