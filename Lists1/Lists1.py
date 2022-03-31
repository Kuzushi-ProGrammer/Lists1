# No imports allowed
# Open the local .txt file romeo.txt                                        (DONE)
# Read line by line and split into a list of words with .split()            (DONE)
# Build a list of words                                                     (DONE)
# Sort the list alphabetically                                              (DONE)
# Count the words in list                                                   (DONE)
# Output as one list                                                        (DONE)

romeom = []
romeomscript = ''
n = 0
wordlist = []
rompath = 'I:/Testing/romeo.txt'              # School computers
# rompath = 'D:/Lists1/Lists1/romeo.txt'      # USB / Home computer

romeomscript = open(rompath, 'r')           # Opens file path for reading

romeomlines = romeomscript.readlines()      # Reads file for a string

# for romeomlines in romeomlines:           # There may be a way to do this although my knowledge is limited atm

line1 = romeomlines[0]                      # Splits lines into segments (So I can get rid of newline with .strip() )
line2 = romeomlines[1]
line3 = romeomlines[2]
line4 = romeomlines[3]

line1 = line1.strip()                       # Removes the invisible (now visible) newline character
line2 = line2.strip()
line3 = line3.strip()
line4 = line4.strip()

romeom.append(line1)                        # Puts the strings as 4 items in a list
romeom.append(line2)
romeom.append(line3)
romeom.append(line4)

romeom = " ".join(romeom)                   # Stitches the items in the list back together as one string

romeomlower = romeom.lower()                # Turns everything lowercase for alphabetical sorting

romeomwords = romeomlower.split(" ")        # Splits the string into a list again to be sorted

romeomwords.sort()                          # Sorts the list

romeomcount = len(romeom)                   # Counts the amount of items in the list (33)

wordlist.append(romeomwords[0])

for x in romeomwords:             # Should go through all the words
    try:
        word1 = romeomwords[n]
        word2 = romeomwords[n + 1]
        print(word1)                    # Left in for demonstrative purposes
        print(word2)
        if word1 == word2:              # Checks if word1 and word2 are the same
            print('same!')              # If they match there's a duplicate since the words are in alphabetical order
            print('')
            n = n + 1                   # Increments place in list
            pass
        elif word1 != word2:
            wordlist.append(word2)      # If word is unique, add to seperate list
            print('not same!')
            print('')
            n = n + 1                   # Still increments place in list to avoid getting stuck
    except IndexError:                  # Happens when list tries to compare number 32 to number 33 which isnt in the list
        continue

uniquewords = ('Unique Words: {}').format(len(wordlist))        # Extra fluff

print(uniquewords)
print('Word List: ')
print(wordlist)

input('-Press Enter to Exit-')      # Stops program from exiting immediately 
