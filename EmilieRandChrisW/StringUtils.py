#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chris
#
# Created:     14-11-2017
# Copyright:   (c) chris 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    test_getinitials()

def getinitials(fullName):
    name=fullName.title().split(' ')
    if len(name)==2:
        return name[0][0] +'.' + name[1][0] + '.'
    if len(name)==3:
        return name[0][0] +'.' + name[1][0] + '.'+name[2][0]+'.'
    if len(name)>3:
        return name[0][0]+'.'+name[1][0]+'.'+name[2][0]+'.'+name[-1][0]+'.'


def test_getinitials():
    print getinitials('Christopher John Wenkoff')
    print getinitials('John samuel wobbly')
    print getinitials('Dylan McDermott')
    print getinitials('nora young')
    print getinitials('Nora james simmons smith timmothy')

if __name__ == '__main__':
    main()
