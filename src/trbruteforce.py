#!/usr/bin/python3.5

# Transposition Cipher brute force Decryption

import math, sys, getopt, enchant

d = enchant.Dict("en_US")

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "ht:k:o:", ["ctext=", "keysize=", "outfile="])

    except getopt.getoptError:
        sys.exit(1)

    if len(sys.argv[1:]) < 4:
        print('Usage: ./trbruteforce.py -t <cyphetext> -o <outfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('Usage: ./trdecode.py -t <cyphertext> -o <outfile>')
            sys.exit()
        elif opt in ("-t", "--ctext"):
            filename = str(arg)
        elif opt in ("-o", "--outfile"):
            outfilename = str(arg)

    with open(filename, "r") as f:
        ciphertext = f.read()

    # call the crypto function
    plaintext = decryptMessage(ciphertext)
    # Print the plaintext

    with open(outfilename, 'w+') as fw:
        fw.write(plaintext)


# --------------------------------------------------------------------------------------

# The transposition decrypt function will simulate the "columns" and
# "rows" of the grid that the plaintext is written on by using a list
# of strings. First, we need to calculate a few values.
#
# Based of code from class, modified for the requirements of this assignment.
#

def decryptMessage(message):
    # Determine the number of columns
    plaintext = "";

    print("Size of message: " + str(len(message)))
    print("Choose a key renge for brute force")


    while 1:
        key1 = input("choose first key to try: ")

        if key1.isdigit():
            break

    while 1:
        key2 = input("choose last key to try: ")

        if key2.isdigit():
            break

    for key in range(int(key1), int(key2)):

        print("Attempting decryption with key: " + str(key) + "...")

        nCols = math.ceil(len(message) / key)

        # Determine the number of rows
        nRows = key

        # Determine the unused cells
        nUnused = (nCols * nRows) - len(message)

        # Each string in plaintext represents a column in the grid.
        plaintext = [''] * (int(nCols))

        # row and col point to the location of the next character in the ciphertext
        row = col = 0

        for symbol in message:
            plaintext[col] += symbol
            col += 1  # point to next column

            # If it reaches the last column in the row, or at an unused cell, start processing the next row
            if (col == nCols) or (col == nCols - 1 and row >= nRows - nUnused):
                col = 0
                row += 1

        plaintextstring = ''.join(plaintext)

        dictionaryResult = checkForEnglish(plaintextstring)

        if dictionaryResult[2] >= 0.5:
            print("Potential plaintext discovered!")
            print("Result for Key: " + str(key))
            print('Potential Words: ' + str(dictionaryResult[0]) + ' Real Words: ' + str(dictionaryResult[1]) + ' Percentage: ' + str(dictionaryResult[2]))

            while 1:
                userInput = input('Print results to file (Y) or continue attempting (N): ')

                if userInput == 'y' or userInput == 'Y':
                    return plaintextstring
                elif userInput == 'n' or userInput == 'N':
                    break
                else:
                    continue
        else:
            print("Neglegable english words found...")



def checkForEnglish(text):

    data = text.split(' ')
    counter = 0
    for word in data:
        if word != '':
            if d.check(word):
                counter += 1
    return [len(data), counter, (counter/len(data))]


# main() function
if __name__ == "__main__":
    main(sys.argv[1:])
