# Python Scripts

## Description
Python scripts used to assist with various tasks...

## Getting Started
* Generate Netgear passwords (warning: memory usage will grow exponentially when including digits)
```
./netgear_generator.py -w adjectives_wordlist.txt -w nouns_wordlist.txt -o netgear_passwords.txt
```
* Generate Netgear password prefixes
```
./netgear_generator.py -w adjectives_wordlist.txt -w nouns_wordlist.txt -z 0 -o netgear_password_prefixes.txt
```
* Generate Netgear password prefixes using Title Case format
```
./netgear_generator.py -w adjectives_wordlist.txt -w nouns_wordlist.txt -z -t -o netgear_password_title_prefixes.txt
```