from typing import List
import base64

#checking the majoirty for the help of binary and ceaser
def checkingMajority(cipher: str) -> bool:
    ceaser: List[str] = [] #empty ceaser cipher list
    binary: List[str] = [] #empty binary list

    for char in cipher:
        if char == "0" or char == "1":
            binary.append(char)
        else:
            ceaser.append(char)

    if len(ceaser) > len(binary): #if the ceaser has the majority, returns true
        return True
    else: #if binary has the majoity, returns false
        return False

#binary decorder
def decode_binary(binary: str) -> str:
    #splits the spaces and new lines
    bits = binary.split()

    decoded_chars = []
    for b in bits:
        #converts each 8-bit chunk to a int, then to a char
        decoded_chars.append(chr(int(b, 2)))

    return "".join(decoded_chars)

#base64 decoder
def decode_base64(base: str) -> str:
    try:
        decoded_bytes = base64.b64decode(base)
        return decoded_bytes.decode('utf-8')
    except Exception:
        return "[ERROR] Could not decode message in Base 64"

if __name__ == '__main__':
    cipher: str = input("Please enter the cipher here\n")

    if "=" in cipher:
        print("base64")
        print(decode_base64(cipher))
    elif ("0" in cipher) and ("1" in cipher):
        print("binary?")

        #checks the majoirty of chars in the cipher to see which cipher to use
        if checkingMajority(cipher):
            print("No, its ceaser")
        else:
            print("yes, its binary")
            print(decode_binary(cipher))
    else:
        print("ceaser")