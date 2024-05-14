import sys
import os
import pytest

# Por algum motivo, o pytest não está conseguindo importar o módulo number_asc_order, professor.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from number.number import NumberAscOrder
from custom_stack.custom_stack_class import CustomStack

def test_sort_with_numbers():
    stack = CustomStack(6)
    numbers = [5, 3, 6, 2, 1, 4]
    for number in numbers:
        stack.push(number)
    
    sorted_numbers = NumberAscOrder.sort(stack)
    assert sorted_numbers == sorted(numbers)
    assert stack.isEmpty()

def test_sort_empty_stack():
    stack = CustomStack(6)
    sorted_numbers = NumberAscOrder.sort(stack)
    assert sorted_numbers == []
    assert stack.isEmpty()

def test_sort_invalid_input():
    with pytest.raises(TypeError):
        NumberAscOrder.sort("not a stack")
