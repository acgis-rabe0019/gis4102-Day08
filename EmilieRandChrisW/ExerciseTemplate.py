#-------------------------------------------------------------------------------
# Name:        Module name
# Purpose:     Brief desciption of what module does
# Usage:       Module name and required/optional command-line parameters (if any)
# Author:      Your name(s)
#
# Created:     21/10/2016
#-------------------------------------------------------------------------------

fmt = "Expected: {}\tActual  : {}"

def main():
    test_func1()

def func1(params):
    """Function documentation:
       - What does function do?
       - What is/are expected parameter value(s)?
       - What does function return, if anything
       - Example usage"""
    pass

def func2(params):
    pass

def test_func1():
    # Test case 1
    expected = "expected value"
    actual = func1(1)
    if expected == actual:
        print "func1(1) passed"
    else:
        print fmt.format(expected, actual)

    # Test case 2 ...


if __name__ == '__main__':
    main()