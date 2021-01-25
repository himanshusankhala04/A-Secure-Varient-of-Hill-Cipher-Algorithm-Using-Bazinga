# A-Secure-Varient-of-Hill-Cipher-Algorithm-Using-Bazinga

In Hill cipher there is a constant substitution performed on chunks of data , it is developed on linear algebra. The major drawbacks of Hill cipher are that it is vulnerable to a known-plaintext attack and  the unreliability of whether the key matrix is invertible for decryption. The proposed algorithm includes a key generation using python secrets library which will always generate a random and valid key, there are two phases of padding and by applying a two level bit manipulation algorithm (Bazinga), it overcomes the flaws of the traditional Hill cipher, based on real testing and experiments the avalanche score increases to 54.7%.\n


The modified algorithm has three main parts to it: encryption, decryption and a key generation. Key is generated randomly using python secrets library, padding which means adding dummy values inside the plaintext to increase the length of the text and a new type of bit manipulation technique called Bazinga. 
Program for this study is written in python programming language and is thoroughly tested with real test cases.
Program divided into parts:\n
1  Key Generation Process
2 Plain-Text Encryption
  A)Pre-Padding 
  B) Traditional Hill Cipher
  C)  Post Padding
  D) Binary Converter :
  E)  Bazinga Level 1 :
  F)  Bazinga Level - 2:
3  Decryption



