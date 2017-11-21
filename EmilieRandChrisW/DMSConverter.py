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
    #test_getEW()
    #test_getNS()
    test_dd2dms()
#get east or west function
def getEW(dmsRecord):
    Find_if_E= dmsRecord.upper().find('E')
    Find_if_W= dmsRecord.upper().find('W')
    if Find_if_E==10:
        if dmsRecord.count('e')==1:
            return "e"
        elif dmsRecord.count("E")==1:
            return "E"
    if Find_if_W==10:
        if dmsRecord.count('w')==1:
            return "w"
        elif dmsRecord.count('W')==1:
            return 'W'
#get north or south function
def getNS(dmsRecord):
    Find_if_N= dmsRecord.upper().find('N')
    Find_if_S= dmsRecord.upper().find('S')
    if Find_if_N==21:
        if dmsRecord.count('N')==1:
            return "N"
        elif dmsRecord.count('n')==1:
            return "n"
    elif Find_if_S==21:
        if dmsRecord.count('S')==1:
            return 'S'
        elif dmsRecord.count('s')==1:
            return 's'
# dms to dd converter function
def dms2dd(dmsRecord):
    dms=dmsRecord.upper().replace('S','N').replace('E','N'). replace('W','N').split('N',2)
    get_dms_EW=getEW(dmsRecord)
    get_dms_NS=getNS(dmsRecord)
    lat=0
    lon=0
    if get_dms_EW.upper().replace('W','E')==('E'):
        degrees= int(dms[0][0:3])
        minutes= int(dms[0][4:6])/60.0
        seconds= int(dms[0][7:9])/3600.0
        dd_lat=degrees+minutes+seconds
        if dd_lat<=180:
            if dmsRecord.upper().count('W')==1:
                lat=float(0-dd_lat)
            else:
                lat=float(dd_lat)
        else:
            return "None"
    if get_dms_NS.upper().replace('N','S')==('S'):
        degrees= int(dms[1][1:3])
        minutes=int(dms[1][4:6])/60.0
        seconds=int(dms[1][7:9])/3600.0
        dd_lon=degrees+minutes+seconds
        if dd_lon <=90:
            if dmsRecord.upper().count('S')==1:
                lon=float(0-dd_lon)
            else:
                lon=float(dd_lon)
        else:
            return "None"
    return "{0:.4f}{1:s}{2:.4f}".format(lat,",",lon)
#test functions
def test_getEW():
    print getEW('075 45 35 W 56 89 45 N\n')
    print getEW('056 65 44 e 65 88 89 N\n')

def test_getNS():
    print getNS('075 45 35 W 56 89 45 N\n')
    print getNS('075 45 35 W 56 89 45 s\n')

def test_dd2dms():
    print dms2dd('075 45 35 E 56 89 45 N\n')
    print dms2dd('075 45 35 W 56 89 45 S\n')
if __name__ == '__main__':
    main()
