#Made it in a class just because
class Tokener:

    @staticmethod
    def decrypt(pk, ciphertext):
        #Decrypt the token and hand it over to the bot
        key, n = pk
        plain = [chr((char ** key) % n) for char in ciphertext]
        decToken = str()
        for ch in plain:
            decToken += ch

        return decToken

    @staticmethod
    def accessFile(self, fileName):

        #Open the file, make the coded token operable
        file = open(fileName, 'r')
        private = []
        private += [int(input("Provide private key: "))]
        private += [int(input())]

        codedToken = []
        for inter in file:
            codedToken.append(int(inter))

        file.close()
        return self.decrypt(private, codedToken)