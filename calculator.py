def add(self, a, b):
    return a + b


def test_add(self):
    # arrange
    a = 4321
    b = 1234
    cal = Calculator()

    # act
    result = cal.add(a, b)

    # assert
    expected = 5555
    assert result == expected
