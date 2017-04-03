#!/usr/bin/python3.5

# Transposition Cipher Encryption
#myMessage = 'A wilderness of mirrors'
#myKey = 12
#python3 trencode.py -t text.txt -k 7 -o ciphertext.txt

import sys, getopt

def main (argv):

    try:
        opts, args = getopt.getopt (argv, "ht:k:o:",["ptext=", "keysize=", "outfile="])

    except getopt.getoptError:
        sys.exit (1)

    if len (sys.argv[1:]) < 6:
        print ('Usage: ./trencode.py -t <plaintext> -k <keysize> -o <outfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('Usage: ./trencode.py -t <plaintext> -k <keysize> -o <outfile>')
            sys.exit ()
        elif opt in ("-t", "--ptext"):
            filename = str(arg)
        elif opt in ("-k", "--keysize"):
            keylen = int (arg)
        elif opt in ("-o", "--outfile"):
            outfilename = str(arg)

    with open(filename, "r") as f:
        plaintext = f.read()

    # call the crypto function
    ciphertext = encryptMessage (keylen, plaintext)

    with open(outfilename, 'w+') as fw:
        fw.write(ciphertext)

    # Print the ciphertext
    #
    #print(ciphertext)


def encryptMessage (key, message):

    # Each string in ciphertext represents a column in the grid.
    ciphertext = [''] * key

    # Iterate through each column in ciphertext.
    for col in range (key):
        pointer = col

        # process the complete length of the plaintext
        while pointer < len (message):
            # Place the character at pointer in message at the end of the
            # current column in the ciphertext list.
            ciphertext[col] += message[pointer]

            # move pointer over
            pointer += key

    # Convert the ciphertext list into a single string value and return it.
    return ''.join (ciphertext)


# If transpositionEncrypt.py is run (instead of imported as a module) call
# the main() function.
if __name__ == "__main__":
    main (sys.argv[1:])
