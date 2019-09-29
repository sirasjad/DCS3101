import string

class vigenereCipher():
    def __init__(self, _key):
        self.alphabet = []
        self.fillAlphabet()
        self.key = _key.upper()

    def fillAlphabet(self):
        for i in range(26):
            self.alphabet.append(string.ascii_uppercase[i])

    def increaseKeySize(self, message):
        if len(message) > len(self.key):
            tempKey = ""
            for i in range(len(message)):
                tempKey += self.key[i % len(self.key)]
            self.key = tempKey

    def encrypt(self, message):
        self.increaseKeySize(message)
        message = message.upper()
        encryptedCipher = ""

        keyPos = 0
        for i in range(len(message)):
            if message[i] == " ": 
                encryptedCipher += " "
            elif message[i] == ".": 
                encryptedCipher += "."
            else:
                letterIndex = (self.alphabet.index(message[i]) + self.alphabet.index(self.key[keyPos])) % 26
                encryptedCipher += self.alphabet[letterIndex]
                keyPos += 1
        return encryptedCipher

    def decrypt(self, message):
        self.increaseKeySize(message)
        message = message.upper()
        decryptedText = ""

        keyPos = 0
        for i in range(len(message)):
            if message[i] == " ":
                decryptedText += " "
            elif message[i] == ".": 
                decryptedText += "."
            else:
                letterIndex = (self.alphabet.index(message[i]) - self.alphabet.index(self.key[keyPos])) % 26
                decryptedText += self.alphabet[letterIndex]
                keyPos += 1
        return decryptedText

vigenere = vigenereCipher("Lemon")
ciphertext = vigenere.encrypt("The quick brown fox jumps over the lazy dog.")
plaintext = vigenere.decrypt("ELQ EHTGW PEZAZ TBI NGACD SHSE ELQ ZNKC PCT.")

print("Encrypted text: %s" % ciphertext)
print("Decrypted text: %s" % plaintext)
