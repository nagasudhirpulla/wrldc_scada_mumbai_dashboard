def makeTwoDigits(num: float) -> str:
    if(num < 10):
        return "0"+str(num)
    return "{0}".format(num)
