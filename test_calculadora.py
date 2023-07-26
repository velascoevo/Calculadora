import pytest
from Calculadora import suma, resta, producto, division


class TestCalculadora:
    def test_suma(self):
        assert suma(1, 2) == 3
        assert suma(-1, 2) == 1
        assert suma(0, 0) == 0
        assert suma(100, 200) == 300
        assert suma(-1, -2) == -3

    def test_resta(self):
        assert resta(1, 2) == -1
        assert resta(-1, 2) == -3
        assert resta(0, 0) == 0
        assert resta(200, 100) == 100
        assert resta(-1, -2) == 1

    def test_producto(self):
        assert producto(1, 2) == 2
        assert producto(-1, 2) == -2
        assert producto(0, 0) == 0
        assert producto(100, 200) == 20000
        assert producto(-1, -2) == 2

    def test_division(self):
        assert division(1, 2) == 0.5
        assert division(-1, 2) == -0.5
        assert division(0, 1) == 0
        assert division(200, 100) == 2
        assert division(-2, -1) == 2
        with pytest.raises(ZeroDivisionError):
            division(1, 0)
