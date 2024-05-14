import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from custom_stack.custom_stack_class import CustomStack

class NumberAscOrder:
    @staticmethod
    def sort(custom_stack):
        if not isinstance(custom_stack, CustomStack):
            raise TypeError("O argumento deve ser do tipo de CustomStack")
        
        if custom_stack.isEmpty():
            return []
        
        sorted_elements = []
        while not custom_stack.isEmpty():
            sorted_elements.append(custom_stack.pop())
        
        sorted_elements.sort()
        return sorted_elements
