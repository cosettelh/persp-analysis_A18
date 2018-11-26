# Cosette L. Hampton, Fall 2018 
# Homework 7 - Q1-3, Test file

import Q3

import pytest

def test_operate(): 
    assert Q3.operate(5, 4, '/') == 1.25, "Trying a decimal output" 
    assert Q3.operate(22, 42, '-') == -20, "Trying a negative output"
    assert Q3.operate(0, 3, '*') == 0, "Trying multiplying by zero" 
    assert Q3.operate(1.25, 1.25, '+') == 2.5, "Adding decimals" 
    with pytest.raises(ZeroDivisionError) as excinfo: 
        Q3.operate(4, 0, '/') 
    assert excinfo.value.args[0] == "division by zero is undefined", "No zero division"
    with pytest.raises(TypeError) as str_excinfo: 
        Q3.operate(7, 9, 3)
    assert str_excinfo.value.args[0] == "oper must be a string", "Last value must be a string"
    with pytest.raises(ValueError) as op_excinfo: 
        Q3.operate(7, 9, "^")
    assert op_excinfo.value.args[0] == "oper must be one of '+', '/', '-', or '*'"

    
    
    