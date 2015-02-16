import sys
import cipher_utils

def vigener_cipher(plaintext, key):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                'n','o','p','q','r','s','t','u','v','w','x','y','z']

    offsets = []
    for key_letter in key:
        offsets.append(alphabet.index(key_letter))

    ciphertext = ''
    for i,char in enumerate(plaintext):
        if char == ' ':
            ciphertext += char
        else:
            offset_index = i % len(offsets)
            offset = offsets[offset_index]
            position_of_char = alphabet.index(char)
            cipher_char = alphabet[(position_of_char+offset)%len(alphabet)]
            ciphertext += (cipher_char)

    return ciphertext

if len(sys.argv) < 4 or len(sys.argv) > 4:
    cipher_utils.print_usage(sys.argv[0])
    sys.exit()

text = open(sys.argv[1], 'r').read()
text = text.replace('\n', ' ')
# remove punctuation and edge whitespace, make lowercase
text = cipher_utils.remove_non_alpha(text).lower().strip()

key = sys.argv[2]
key = key.lower()

output_file = open(sys.argv[3], 'w')

if len(key) < 2 or len(key) > 7:
    print('Key must be of length 2-7')
    sys.exit()

for char in key:
    if not char.isalpha():
        print('Key must be composed of letters from the English alphabet.')
        sys.exit()


ciphertext = vigener_cipher(text, key)
output_file.write(ciphertext)
