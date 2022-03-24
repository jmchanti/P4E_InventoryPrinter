import io
from random import randint
from unittest.mock import Mock
import oddAbsolute

def test_calculateAbsolute_printsABS_lessThan21(capfd, monkeypatch):
    in_num = randint(-100, 21)
    input = [in_num]
    monkeypatch.setattr('builtins.input', lambda _:input.pop())
    oddAbsolute.calculateAbsolute()

    out, err = capfd.readouterr()
    expected = "Result: "+str(abs(in_num-21))+"\n"
    assert out == expected


def test_calculateAbsolute_printsDoubleAbs_greaterThan21(capfd, monkeypatch):
    in_num = randint(21, 200)
    input = [in_num]
    monkeypatch.setattr('builtins.input', lambda _:input.pop())
    oddAbsolute.calculateAbsolute()

    out, err = capfd.readouterr()
    expected = "Result: "+str(abs(2*(in_num-21)))+"\n"
    print(in_num)
    assert out == expected