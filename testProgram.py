import io
from random import randint
from unittest.mock import Mock
import counter

def test_calculate_printsLineCountSmallFile(capfd, monkeypatch):
    input = ['mbox-short.txt']
    monkeypatch.setattr('builtins.input', lambda _:input.pop())
    counter.countDayOfTheWeek()

    out, err = capfd.readouterr()
    assert "\'Sat\': 1," in out
    assert "\'Fri\': 20," in out
    assert "\'Thu\': 6" in out


def test_calculate_printsLineCountLargeFile(capfd, monkeypatch):
    input = ['mbox-long.txt']
    monkeypatch.setattr('builtins.input', lambda _:input.pop())
    counter.countDayOfTheWeek()

    out, err = capfd.readouterr()
    
    assert "\'Sat\': 61," in out
    assert "\'Fri\': 315" in out
    assert "\'Wed\': 292" in out
    assert "\'Thu\': 392" in out
    assert "\'Tue\': 372" in out
    assert "\'Mon\': 299" in out
    assert "\'Sun\': 66" in out