from typing import List

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

if __name__ == '__main__':
    cipher: str = input("Please enter the cipher here\n")

    if "=" in cipher:
        print("base64")
    elif ("0" in cipher) and ("1" in cipher):
        print("binary?")

        #checks the majoirty of chars in the cipher to see which cipher to use
        if checkingMajority(cipher):
            print("No, its ceaser")
        else:
            print("yes, its binary")
    else:
        print("ceaser")