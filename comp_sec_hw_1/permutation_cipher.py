import sys

def remove_non_alpha(text):
    return ''.join([c for c in text if c.isalpha() or c == ' '])

def print_usage(program_name):
    print('USAGE: python3', program_name, 'TEXT_FILE KEY OUTPUT_FILE')

def permutation_cipher(plaintext, key):
    # form a list of integer key digits and subtract 1 from them all to make the 0 indexable
    processed_key = [int(c) - 1 for c in key]

    # get rid of all spaces but save their location
    space_indices = []
    for i,c in enumerate(plaintext):
        if c == ' ': space_indices.append(i)

    plaintext = plaintext.replace(' ', '')

    # split plaintext into an array of chunks that are the length of the permutation key
    chunk_size = len(key)
    chunks = [plaintext[i:i+chunk_size] for i in range(0, len(plaintext), chunk_size)]

    # add extra letters to the last chunk if necessary
    end_letters = 'setpci'
    if len(chunks[-1]) < len(key):
        num_missing_letters = len(key) - len(chunks[-1])
        chunks[-1] += end_letters[0:num_missing_letters]

    # create the ciphertext
    ciphertext = ''
    for chunk in chunks:
        cipherchunk = ''
        for permutation_val in processed_key:
            cipherchunk += chunk[permutation_val]
        ciphertext += cipherchunk

    # add spaces back in their original locations
    cipherchar_list = list(ciphertext)
    for i in space_indices:
      cipherchar_list.insert(i, ' ')

    ciphertext = ''.join(cipherchar_list)

    return ciphertext

if len(sys.argv) < 4 or len(sys.argv) > 4:
    print_usage(sys.argv[0])
    sys.exit()

text = open(sys.argv[1], 'r').read()
text = text.replace('\n', ' ')
# remove punctuation and edge whitespace, make lowercase
text = remove_non_alpha(text).lower().strip()

key = sys.argv[2]
output_file = open(sys.argv[3], 'w')

if len(key) < 2 or len(key) > 7:
    print('Key must be of length 2-7')
    sys.exit()

if not key.isnumeric():
    print('Key must be composed of digits 1,2,...,key_length in any order')
    sys.exit()

for char in key:
    if int(char) > len(key):
        print('Key must be composed of digits 1,2,...,key_length in any order')
        sys.exit()

if len(set([char for char in key])) < len(key):
    print('Key must be composed of digits 1,2,...,key_length in any order')
    sys.exit()

# remember: end_letters is setpci
'''
assert permutation_cipher('abcdef', '123') == 'abcdef'
assert permutation_cipher('abcdefg', '123') == 'abcdefgse'
assert permutation_cipher('abcdefgh', '123') == 'abcdefghs'
assert permutation_cipher('abcdef', '321')  == 'cbafed'
assert permutation_cipher('a b c d e f', '321') == 'c b a f e d'
assert permutation_cipher('abc defgh', '4321') == 'dcb ahgfe'
assert permutation_cipher('abc def', '4321') == 'dcb aesfe'
assert permutation_cipher('abc de', '4321') == 'dcb atese'
'''

text = text.replace(' ', '')
ciphertext = permutation_cipher(text, key)
output_file.write(ciphertext)
