# declare letters
letters = 'abcdefghijklmnopqrstuvwxyz'
num_letters = len(letters)

# first trial of encrypt and decrypt functions
# def encrypt(plaintext, key):
#     ciphertext = ''
#     for letter in plaintext:
#         letter = letter.lower()
#         if not letter == ' ':
#             index = letters.find(letter)
#             if index == -1:
#                 ciphertext += letter
#             else:
#                 new_index = index + key
#                 if new_index >= num_letters:
#                     new_index -= num_letters
#                 ciphertext += letters[new_index]
#     return ciphertext

# def decrypt(ciphertext, key):
#     plaintext = ''
#     for letter in ciphertext:
#         letter = letter.lower()
#         if not letter == ' ':
#             index = letters.find(letter)
#             if index == -1:
#                 plaintext += letter
#             else:
#                 new_index = index - key
#                 if new_index < 0:
#                     new_index += num_letters
#                 plaintext += letters[new_index]
#     return plaintext

def encrypt_decrypt(text, mode, key):
    result = ''
    if mode == 'd':
        key = -key
    for letter in text:
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                result += letter
            else:
                new_index = index + key
                if new_index >= num_letters:
                    new_index -= num_letters
                elif new_index < 0:
                    new_index += num_letters
                result += letters[new_index]
    return result

print()
print('*** Caesar Cipher Program ***')
print()

print('Do you want to encrypt or decrypt?')
user_input = input('e/d: ').lower()
print()

if user_input == 'e':
    print('Encryption mode selected')
    print()
    key = int(input('Choose a key (1-26): '))
    text = input('Enter the text to encrypt: ')
    ciphertext = encrypt_decrypt(text, user_input, key)
    print(f'Ciphertext: {ciphertext}')

elif user_input == 'd':
    print('Decyption mode selected')
    print()
    key = int(input('Enter the key (1-26): '))
    text = input('Enter the text to decrypt: ')
    plaintext = encrypt_decrypt(text, user_input, key)
    print(f'Plaintext: {plaintext}')