#!/usr/bin/env python3
# Author: str3tch @ Vegas 2.0 | dc702
# Description: Generates a list of passwords or password prefixes mirroring
#              a Netgear algorithm
# Example Usages:
#     ./netgear_generator.py -w adj.txt -w noun.txt -z 0 -t -o title_prefixes
#     ./netgear_generator.py --wordlist adj.txt --wordlist noun.txt -o passwords
# Note: Actually appending the digits results in massive amounts of RAM usage.
import argparse
import logging

# Command line arguments
parser = argparse.ArgumentParser(description='Netgear password generator')
parser.add_argument('-o', '--output_file', help='wordlist file')
parser.add_argument('-t', '--title_case', action='store_true',
                    help='use Title Case for passwords')
parser.add_argument('-w', '--wordlist', default=[], action='append',
                    help='wordlist file')
parser.add_argument('-x', '--min_len', type=int, default=4,
                    help='minimum word length')
parser.add_argument('-y', '--max_len', type=int, default=6,
                    help='maximum word length')
parser.add_argument('-z', '--digits', type=int, default=3,
                    help='number of trailing digits')
ARGS = parser.parse_args()


def create_output_file(filename, data):
    with open(filename, 'w') as file:
        for item in data:
            file.write(f'{item}\n')


def get_words_from_file(filename):
    words = []

    with open(filename, 'r') as file:
        for word in file:
            words.append(word.strip())

    return words


def main():
    logging.basicConfig(level=logging.INFO)
    passwords = []
    if ARGS.wordlist:
        # Append each wordlist to the previous wordlist entries
        for filename in ARGS.wordlist:
            new_passwords = []
            logging.info(f'Processing {filename}...')
            for word in get_words_from_file(filename):
                # Skip words that are too short
                if len(word) < ARGS.min_len:
                    continue

                # Skip words that are too long
                if len(word) > ARGS.max_len:
                    continue

                # Use Title Case if specified
                if ARGS.title_case:
                    word = word.title()

                if passwords:
                    # Append word to each password if passwords exist from
                    # previous wordlist
                    for password in passwords:
                        new_passwords.append(password + word)
                else:
                    new_passwords.append(word)

            if new_passwords:
                logging.info(f'passwords: {len(passwords)} -> '
                             f'{len(new_passwords)}')
                passwords = new_passwords
            else:
                logging.info(f'passwords: {len(passwords)}')

    # Add trailing digits if specified
    if passwords and ARGS.digits > 0:
        new_passwords = []
        for password in passwords:
            for i in range(ARGS.digits ** 10):
                new_passwords.append(password + str(i).zfill(ARGS.digits))

        logging.info(f'passwords: {len(passwords)} -> {len(new_passwords)}')
        passwords = new_passwords

    # Write passwords to file
    if ARGS.output_file:
        logging.info('Creating output file...')
        create_output_file(ARGS.output_file, passwords)


if __name__ == '__main__':
    main()
