#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chris
#
# Created:     13-11-2017
# Copyright:   (c) chris 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
   test_hasXcode()
   test_getXcodePosition()
   test_getPatternPosition()


def hasXcode(inText):
    search_string="Tx6op3"
    find_string= str(inText).find(search_string)
    if find_string >=0:
        return True
    else:
        return False


def getXcodePosition(inText):
    search_string="Tx6op3"
    find_string_position= str(inText).find(search_string)
    if find_string_position >=0:
        return find_string_position+1
    else:
        return -1

def getPatternPosition(pattern, inText):
    find_pattern_position= str(inText).find(pattern)
    if find_pattern_position >=0:
        return find_pattern_position +1
    else:
        return -1

def test_hasXcode():
    print hasXcode('Tx6op3')
    print hasXcode('32')
    print hasXcode("This is a completeTx6op3test")
def test_getXcodePosition():
    print getXcodePosition('Tx6op3')
    print getXcodePosition(65)
    print getXcodePosition('This is a compeTx6op3ency test')
def test_getPatternPosition():
    print getPatternPosition("x96","x96")
    print getPatternPosition('x96',"in a range of 4")
    print getPatternPosition("test1","test1 w2")
    print getPatternPosition("redrum","Why is the redrum always gone?")
if __name__ == '__main__':
    main()
