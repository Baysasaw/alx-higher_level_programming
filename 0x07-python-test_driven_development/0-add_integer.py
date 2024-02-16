#!/usr/bin/python3
"""A module to add two numbers

This module performs the addition operation between two numbers,
these numbers can be integers or floats.

"""

def add_integer(a, b=98):
     """Adds two numbers

    Performs the addition between two numbers.

    Args:
        a (:obj:`int, float`): The first number.
        b (:obj:`int, float`, optional): The second number.

    Returns:
        int: The result of the addition.

    """
     
     
     if type(a) != int and type(a) != float:
        raise TypeError('a must be an integer')
     
     if type(b) != int and type(b) != float:
        raise TypeError('b must be an integer')
     else:
        """
        
        a and b must be first casted to integers if they are float
        
        """

        a = int(a)
        b = int(b)
        """
        
        Returns:
          int: the addition of a and b
        
        """
        return a + b
    