#adding a prefix to a word

def add_prefix_un(word):
    return 'un' + word

#adding prefixes to word groups
word = ['en','close', 'joy', 'lighten']
def make_word_groups(list):
    prefix = list[0]
    list.pop(0)
    for word in list:
        print(prefix + word)
        

#removing a suffix from a word

def remove_suffix_ness(word):
    char = []
    word = word.replace('ness','')
    for letter in word:
        char.append(letter)

    if char[-1] == 'i':
        char[-1] = 'y'
        new_word = "".join(char)
    else:
        new_word = word

    return new_word
  

#extract and transform a word

def adjective_to_verb(sentance,index):
    words = sentance.split()
    return words[index] + 'en'



