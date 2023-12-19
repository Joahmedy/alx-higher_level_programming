#!/usr/bin/python3


def safe_print_division(a, b):
    """
    divides two integers and prints the result
    catches divide by zero exception
    """
    try:
        res = a / b
    except:
        res = None
    finally:
        print("Inside result: {:s}".format(res))
    return res
