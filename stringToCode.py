setA = ("a","b","c","d","e","f","g",
        "h","i","j","k","l","m","n",
        "o","p","q","r","s","t","u",
        "v","w","x","y","z", " ", ".", "(",")","'") #Alphabet

setB = ("c","d","e","f","g",
        "h","i","j","k","l","m","n",
        "o","p","q","r","s","t","u",
        "v","w","x","y","z", "a","b", " ", ".", "(",")","'") #Alphabet+2

testString = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr glzw fylb gq glcddgagclr ylb rfyr'q ufw rfgqrcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

dict = {}

def fromCodeToEng(input):
    if (type(input) is not str):
        print("Enter a string")
        return

    output = ""
    i = 0
    for x in setA:
        dict[x] = setB[i]
        i+=1

    newString = ""

    for x in input:
        output = output + dict[x]

    print(input)
    print(output)

    return output

def fromEngToCode(input):
    if (type(input) is not str):
        print("Enter a string")
        return

    output = ""
    i = 0
    for x in setB:
        dict[x] = setA[i]
        i += 1
    for x in input:
        output = output + dict[x]

    print(input)
    print(output)

    return output

# Has obvious flaw in that anything that inlcudes the letter
# a or b in the code will re-translated incorrectly
# Just use string.maketrans()