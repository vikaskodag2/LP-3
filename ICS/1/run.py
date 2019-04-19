import numpy as np
from keygen import keygen
from encrypt import encrypt, decrypt

def main() :
    choice = input("enter 'e' to encrypt or 'd' to decrypt : ")
    if choice == 'e' :
        inputfile = input("enter input file : ")
        outputfile = input("enter output file : ")
        print("starting encryption!!")
        with open(inputfile, 'rb') as f :
            input_text = np.fromfile(f, dtype=np.uint8)

        k1, k2 = keygen()
        output = encrypt(input_text, k1, k2)
        with open(outputfile, 'wb') as f :
            output.tofile(f)
        print("Encryption completed!")

    elif choice == 'd' :
        inputfile = input("enter input file : ")
        outputfile = input("enter output file : ")
        print("starting decryption!!")
        with open(inputfile, 'rb') as f :
            input_text = np.fromfile(f, dtype=np.uint8)

        k1, k2 = keygen()
        output = decrypt(input_text, k1, k2)
        with open(outputfile, 'wb') as f :
            output.tofile(f)
        print("Decryption completed!!")
    else :
        print("enter correct choice!")


if __name__ == '__main__' :
    main()