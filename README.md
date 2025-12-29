# Ciphers2
this will only work with ceaser, binary and base64

# Whats NEW
Nothing. its still the same idea, but for another ARG

# how would this work in the other arg
Simple, we will use wasm. but first i need to make the code first

for the code, i know wasm love to print out all print statements, so for print statements that are not ment to be shown. I will just comment out, but still include in this file

# distinguishing each cipher

1. for base 64
   1. each base 64 file contains a =, so its checked first.
   2. if the file has a =, then returns a decipher base 64 cipher
2. if binary
    1. bit tricky
        1. first checks for the majority of the cipher.
       2. if the cipher is majority 1 and 0, then return binary decipher message
       3. else returns a deciphered ceaser cipher.
3. if ceaser
   1. just returns a deciphered ceaser cipher.