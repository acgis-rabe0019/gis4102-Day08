#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      chris
#
# Created:     14-11-2017
# Copyright:   (c) chris 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    test_getCoordsFromGpx()
def getCoordsFromGpx(gpx):
    contains_indicator= str(gpx).find("trkpt")
    if contains_indicator>=0:
        gpx_rep_character_1=gpx.replace('"','')
        gpx_rep_character_2=gpx_rep_character_1.replace('>','')
        Latlon= gpx_rep_character_2.split(' ')
        lat= Latlon[1][4:]
        lon= Latlon[2][4:]
        return "("+lat+ ","+lon+")"

    else:
        return"None"
def test_getCoordsFromGpx():
    print getCoordsFromGpx('<trkpt lat="45.3888995" lon="-75.7472631">')
    print getCoordsFromGpx('trkpt lat=45.987562 lon=75.985648')
    print getCoordsFromGpx('4561235263')
if __name__ == '__main__':
    main()
