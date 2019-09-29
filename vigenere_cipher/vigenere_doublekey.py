import string

class vigenereCipher():
    def __init__(self, key1, key2):
        self.alphabet = []
        self.fillAlphabet()
        self.key = [key1.upper(), key2.upper()]

    def fillAlphabet(self):
        for i in range(26):
            self.alphabet.append(string.ascii_uppercase[i])

    def increaseKeySize(self, message, key):
        if len(message) >= len(key):
            tempKey = ""
            for i in range(len(message)):
                tempKey += key[i % len(key)]
            return tempKey

    def encrypt(self, message):
        for x in range(2):
            self.key[x] = self.increaseKeySize(message, self.key[x])
            message = message.upper()
            encryptedCipher = ""

            keyPos = 0
            for i in range(len(message)):
                if message[i] == " ": 
                    encryptedCipher += " "
                elif message[i] == ".": 
                    encryptedCipher += "."
                else:
                    letterIndex = (self.alphabet.index(message[i]) + self.alphabet.index(self.key[x][keyPos])) % 26
                    encryptedCipher += self.alphabet[letterIndex]
                    keyPos += 1
            
            print("----- Encryption Round %i (using Key-%i) -----" % (x+1, x+1))
            print("Key: %s" % self.key[x])
            print("Plaintext: %s" % message)
            print("Ciphertext: %s\n" % encryptedCipher)
            message = encryptedCipher

    def decrypt(self, message):
        for x in range(2):
            self.key[x] = self.increaseKeySize(message, self.key[x])
            message = message.upper()
            decryptedText = ""

            keyPos = 0
            for i in range(len(message)):
                if message[i] == " ": 
                    decryptedText += " "
                elif message[i] == ".": 
                    decryptedText += "."
                else:
                    letterIndex = (self.alphabet.index(message[i]) - self.alphabet.index(self.key[x][keyPos])) % 26
                    decryptedText += self.alphabet[letterIndex]
                    keyPos += 1
            
            print("----- Decryption Round %i (using Key-%i) -----" % (x+1, x+1))
            print("Key: %s" % self.key[x])
            print("Plaintext: %s" % message)
            print("Ciphertext: %s\n" % decryptedText)
            message = decryptedText

# Initiate an object, setting key-1 = "Green" and key-2 = "Watermelon"
vigenere = vigenereCipher("Green", "Watermelon")
vigenere.encrypt("The quick brown fox jumps over the lazy dog.")
vigenere.decrypt("VYB YYAXZ TRQNK NSP EJEPU FSMV LCT DABP AWK.")
