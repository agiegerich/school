def remove_non_alpha(text):
    return ''.join([c for c in text if c.isalpha() or c == ' '])

def print_usage(program_name):
    print('USAGE: python3', program_name, 'TEXT_FILE KEY OUTPUT_FILE')


