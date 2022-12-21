import io
import json
from random import randint
from unittest.mock import Mock
import displayInventory

def test_displayInventory_basic_result(capfd, monkeypatch):
    inputString ="{\"rope\": 1, \"torch\": 6, \"gold coin\": 42, \"ring\": 1, \"apple\": 12}"
    displayInventory.displayInventory(json.loads(inputString))

    out, err = capfd.readouterr()
   
    assert "Inventory:" in out
    assert "1 rope" in out
    assert "6 torch" in out
    assert "42 gold coin" in out
    assert "1 ring" in out
    assert "12 apple" in out
    
def test_displayInventory_differentImput_result(capfd, monkeypatch):
    inputString ="{\"rope\": 7, \"torch\": 12, \"gold coin\": 42, \"ring\": 1, \"apple\": 12, \"axe\": 785}"
    displayInventory.displayInventory(json.loads(inputString))

    out, err = capfd.readouterr()
   
    assert "Inventory:" in out
    assert "7 rope" in out
    assert "12 torch" in out
    assert "42 gold coin" in out
    assert "1 ring" in out
    assert "12 apple" in out
    assert "785 axe" in out
