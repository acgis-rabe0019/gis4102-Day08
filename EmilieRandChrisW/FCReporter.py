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
    test_getFeatureTypeFromName()

def getFeatureTypeFromName(fcName):
    feature_name= str(fcName).rsplit('_',1)
    if len(feature_name)==1:
        return "Unknown"
    else:
        suffix=feature_name[-1].upper()
        if suffix== "PLY":
            return "Polygon"
        elif suffix=="PNT":
            return "Point"
        elif suffix == "LIN":
            return "Line"
        else:
            return "Unknown"


def test_getFeatureTypeFromName():
    print getFeatureTypeFromName('Prince_PLY')
    print getFeatureTypeFromName('Prince_of_Persia_PLY')
    print getFeatureTypeFromName('Princeply')
    print getFeatureTypeFromName('Prince_ply')
    print getFeatureTypeFromName('poor unfortunate soul_Lin')
    print getFeatureTypeFromName('forever unknown_PNT')
    print getFeatureTypeFromName("final failed test_pointed")
if __name__ == '__main__':
    main()
