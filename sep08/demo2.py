def getDigit(x):
    """

    :type x: int or float
    """
    returnDigit=0
    while x>0:
        x//=10
        returnDigit += 1
    return returnDigit
if __name__ =='__main__':
    print(getDigit(123123))