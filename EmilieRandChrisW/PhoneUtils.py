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
    #test_isValidPhoneNumber()
    test_phoneNumberHasLetters()
def isValidPhoneNumber(phoneNumber):
    phone_string=str(phoneNumber)
    if len(phone_string)==12:
        if phone_string[0:3].isdigit():
            if phone_string[3]=='-':
                if phone_string[4:7].isdigit():
                    if phone_string[7]=='-':
                        if phone_string[8:].isdigit():
                            return True
                        else: return False
                    else: return False
                else:return False
            else: return False
        else:return False
    else: return False

def phoneNumberHasLetters(phoneNumber):
    phone_string=str(phoneNumber)
    if len(phone_string)==12:
           if phone_string[0:3].isdigit():
               if phone_string[3]=='-':
                   if phone_string[4:7].isalnum():
                       if phone_string[7]=='-':
                           if phone_string[8:].isalnum():
                               return True
                           else: return False
                       else: return False
                   else:return False
               else: return False
           else:return False
    else: return False
def test_isValidPhoneNumber():
    print isValidPhoneNumber('560-632-8904')
    print isValidPhoneNumber('45h768890555')
def test_phoneNumberHasLetters():
    print phoneNumberHasLetters('416-458-test')
    print phoneNumberHasLetters('562-5t8-y7p9')
if __name__ == '__main__':
    main()
