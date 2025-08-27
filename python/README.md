# Python Scripts

## Description
Python scripts used to assist with various tasks...

## netgear_generator.py
### Example Usage
#### Generate Netgear passwords (warning: memory usage will grow exponentially when including digits)
```
./netgear_generator.py -w adjectives_wordlist.txt -w nouns_wordlist.txt -o netgear_passwords.txt
```

#### Generate Netgear password prefixes
```
./netgear_generator.py -w adjectives_wordlist.txt -w nouns_wordlist.txt -z 0 -o netgear_password_prefixes.txt
```

#### Generate Netgear password prefixes with Title Case format
```
./netgear_generator.py -w adjectives_wordlist.txt -w nouns_wordlist.txt -z -t -o netgear_password_title_prefixes.txt
```

## wordlist_generator.py
### Help
<table>
<th>Option</th><th>Alternate</th><th>Argument</th><th>Description</th>
<tr><td>-o</td><td>--output_file</td><td>filename</td><td>File to create containing passwords</td><tr>
<tr><td>-k</td><td>--keep_spaces</td><td></td><td>Don't remove spaces from source wordlist</td></tr>
<tr><td>-l</td><td>--case_lower</td><td></td><td>Make all passwords lowercase (e.g. ilovewordlists)</td></tr>
<tr><td>-p</td><td>--prefix</td><td>string</td><td>String to prepend to passwords (e.g. PrefixILoveWordlists)</td></tr>
<tr><td>-s</td><td>--suffix</td><td>string</td><td>String to append to passwords (e.g. ILoveWordlistsSuffix)</td></tr>
<tr><td>-t</td><td>--case_title</td><td></td><td>Make all passwords titlecase (e.g. ILoveWordlists)</td></tr>
<tr><td>-u</td><td>--case_upper</td><td></td><td>Make all passwords uppercase (e.g. ILOVEWORDLISTS)</td></tr>
<tr><td>-v</td><td>--verbose</td><td></td><td>Increase logging from INFO to DEBUG</td></tr>
<tr><td>-w</td><td>--wordlist</td><td>filename</td><td>Existing wordlist with base words to add to</td></tr>
<tr><td>-y</td><td>--year</td><td>string</td><td>String to insert before suffixes (e.g. ILoveWordlistsYearSuffix)</td></tr>
</table>

### Example Usage
#### Generate a wordlist that looks like "GoTeam2025!" for MLB, NBA, NFL, and NHL teams
```
./wordlist_generator.py -w mlb_team_names.txt -w nba_team_names.txt -w nfl_team_names.txt -w nhl_team_names.txt -p Go -y 2025 '!' -t -o go_team.txt
```

#### Generate a wordlist that looks like "ByeState!!!" and "AdiosState!!!"
```
./wordlist_generator.py -w top_state_migrations_to_nevada.txt -p bye -p adios -s '!!!' -t -o moving_to_nevada.txt
```

#### Generate a wordlist that looks like "imissname"
```
./wordlist_generator.py -w human_names.txt -p 'IMiss' -l -o i_miss_name.txt
```

#### Generate a wordlist that looks like "ILOVEPETNAME?"
```
./wordlist_generator.py -w pet_names.txt -p 'ilove' -s '?' -u -o i_love_pets.txt
```