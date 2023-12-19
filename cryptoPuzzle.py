# Challenge: Crypto Puzzle
# Task: Try to decipher the encrypted message or create a more secure algorithm.


class CryptoPuzzle:
    def __init__(self, key):
        self.key = key
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"

    def encrypt(self, message):
        encrypted_message = ""
        for char in message:
            if char.isalpha():
                char_index = (self.alphabet.index(char.lower()) + self.key) % 26
                encrypted_char = self.alphabet[char_index]
                encrypted_message += (
                    encrypted_char if char.islower() else encrypted_char.upper()
                )
            else:
                encrypted_message += char
        return encrypted_message

    def decrypt(self, encrypted_message):
        decrypted_message = ""
        for char in encrypted_message:
            if char.isalpha():
                char_index = (self.alphabet.index(char.lower()) - self.key) % 26
                decrypted_char = self.alphabet[char_index]
                decrypted_message += (
                    decrypted_char if char.islower() else decrypted_char.upper()
                )
            else:
                decrypted_message += char
        return decrypted_message


# Example
crypto = CryptoPuzzle(key=3)
message = "Hello, Python Challenge!"
encrypted_message = crypto.encrypt(message)
decrypted_message = crypto.decrypt(encrypted_message)

print("Original Message:", message)
print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)
