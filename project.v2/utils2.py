def getHeadIndex(tape: list)-> int:
    """
    given a tape (list), return the index of the first character that's different from "_".
        - if all characters are "_", returns 0 (the first index)
    """
    l = len(tape)
    head=0
    for i in range(l):
        if tape[i]!= "_": 
            head=i
            break
    return head


# def getHeadIndex(tape: list)-> int:
#     """
#     given a tape (list), return the index of the first character that's different from "_".
#         - if all characters are "_", returns 0 (the first index)
#     """
#     l = len(tape)
#     head=0
#     hasOne = False
#     foundZero = False

#     for i in range(l):
#         # position the head on the first character cause all of the 0 or _ don't matter
#         if tape[i]== 1: 
#             hasOne = True
#             head=i
#             break
#         if tape[i] == 0 and not foundZero:
#             foundZero = True
#             head = i #if there are only _ and 0s, it would set the head to the first 0, and later cut all the following charaters if there are any (to prevent a case of 0 0 0 0 ...)
    
#     if(not hasOne):
#         # if there aren't any 1s and the head is on either 0 or _ , cut all the following characters from where the head is positioned
#         tape = tape[:head+1]
       
#     return head

def getLastCharIndex(tape: list)-> int:
    """
    given a tape (list), return the index of the last character that's different from "_".
        - if all characters are "_", returns the last index
    """
    n = len(tape)-1
    k = n
    while k>=0:
        if tape[k]!= "_": return k
        k-=1
    return n

def binaryToDecimal(t) -> int:
    """
    gets a tape from a machine with a number in binary base and returns the decimal number.
    """
    
    start = getHeadIndex(t)
    end = getLastCharIndex(t)  

    is_negative = t[start] == "-"
    if t[start] == "_": return 0
    numberTape = t[start+1:end+1] if is_negative else t[start:end+1]

    binary = "".join(map(str, numberTape)) 
    decimal = int(binary, 2)

    return -decimal if is_negative else decimal



def isZero(tape: list):
    """
     given a tape of a machine, checks if the number appearing in it is zero
        returns: true if it is zero, false otherwise
    """

    for t in tape:
        if t == 1:
            return False
        
    return True