def check(a,b,c):
    if a==b or a==c:
        return True
    elif b==c or a==b:
        return True
    else:
        return False


check(0,9,9)
