#This program will encrypt and decrypt a file of text

# (C) Ben Baker 2021

minASCII = 32
maxASCII = 126
count = maxASCII - minASCII + 1             #provides range of printable characters

#accepts filename
inputFilename = input("Enter filename here: ")

#open and read file
try:
    f = open(inputFilename, 'r')
    text = f.read()

    #accepts distance
    distance = int(input("Enter distance: "))

    encryptedText = ""

    #iterate over characters ch in file's text
    for ch in text:
        ordValue = ord(ch)
        if ordValue < 32 or ordValue > 126:
            encryptedText += ch
            continue                        #skip if non-printable character

        cipherValue = ordValue + distance

        cipherValue = cipherValue % count   #ensures value is
        if cipherValue < minASCII:          #within printable
            cipherValue += count            #character range

        encryptedText += chr(cipherValue)
    print("\nEncrypted Text:\n%s" % encryptedText)


    plainText = ""

    # iterate over characters ch in file's text
    for ch in encryptedText:
        ordValue = ord(ch)
        if ordValue < 32 or ordValue > 126:
            plainText += ch
            continue                        #skip if non-printable character

        cipherValue = ordValue - distance

        cipherValue = cipherValue % count   #ensures value is
        if cipherValue < minASCII:          #within printable
            cipherValue += count            #character range

        plainText += chr(cipherValue)
    print("\nPlain Text:\n%s" % plainText)

#in case file not found
except FileNotFoundError:
    print("There is no file with that name in this directory.")
