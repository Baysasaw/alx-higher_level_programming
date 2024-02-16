#!/usr/bin/python3
"""Filename: 0-add_integer"""

def add_integer(a, b=98):
    """

    a and b must be integers or floats, otherwise raise a TypeError
    exception with the message a must be an integer or b must be an integer
    
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
    