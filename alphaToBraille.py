import mapAlphaToBraille

class Translate: 
    __CAPITAL = chr(10272)  # ⠠
    __NUMBER = chr(10300)  # ⠼
    __LETTER = chr(10288)
    __UNRECOGNIZED = '?'
    __ABBREVIATION = list(mapAlphaToBraille.abbreviation.keys())

    # There is no braille symbol for a generic quote (").
    # There is only open quotation (“) and closed quotation (”).
    # Therefore we must keep track of what the last quotation was
    # so that we may convert the generic quotation to a specific one.
    open_quotes = True

    def __init__(self, text):
        self.text = text
        
    def __extract_words(self, string):
        # Split up a sentence based on whitespace (" ") and new line ("\n") chars.
        words = string.split(" ")
        result = []
        for word in words:
            new_line = "\n" in word
            temp = word.split("\n")
            for item in temp:
                result.append(item)
                if new_line:
                    result.append("\n")
        return result[:-1]


    def __trim(self, word):
        # Remove punctuation around a word. Example: cat." becomes cat
        while len(word) is not 0 and not word[0].isalnum():
            word = word[1:]
        while len(word) is not 0 and not word[-1].isalnum():
            word = word[:-1]
        return word


    def __char_to_braille(self, char):
        # Convert an alphabetic char to braille.
        if char == "\n":
            return "\n"
        elif char == "\"":
            if self.open_quotes:
                self.open_quotes = not self.open_quotes
                #return mapAlphaToBraille.punctuation.get("“")
                return mapAlphaToBraille.punctuation.get("“")
            else:
                self.open_quotes = not self.open_quotes
                #return mapAlphaToBraille.punctuation.get("”")
                return mapAlphaToBraille.punctuation.get("”")
        elif char.lower() in mapAlphaToBraille.abbreviation:
            return mapAlphaToBraille.abbreviation.get(char.lower())
        elif char.lower() in mapAlphaToBraille.letters:
            braille_char = mapAlphaToBraille.letters.get(char.lower())
            if char.isupper():
                return self.__CAPITAL + braille_char
            return braille_char
        elif char in mapAlphaToBraille.punctuation:
            return mapAlphaToBraille.punctuation.get(char)
        elif char in mapAlphaToBraille.numbers:
            return mapAlphaToBraille.numbers.get(char)


    def __word_to_braille(self, word):
        # Convert an alphabetic word to braille.
        if word.lower() in mapAlphaToBraille.contractions:
            braille_word = mapAlphaToBraille.contractions.get(word.lower())
            if word.isupper():
                return self.__CAPITAL*2 + braille_word
            elif word[0].isupper() and word[1:].islower():
                return self.__CAPITAL + braille_word
            else:
                return braille_word
        abbreviation = {abr:word.find(abr) for abr in self.__ABBREVIATION if abr in word}
        if 'ing' in abbreviation.keys():
            del abbreviation['in']

        abbreviation = sorted(abbreviation.items(), key=lambda kv:kv[1], reverse=True)
        
        word_l = list(word)
        for abr, pos in abbreviation:
            word_l[pos:pos+len(abr)] = [''.join(word_l[pos:pos+len(abr)])]

        result = ""
        for char in range(len(word_l)):
            if char != 0 and word_l[char-1].isdigit() and (not word_l[char].isdigit()):
                result += self.__LETTER
            elif (char == 0 and word_l[char].isdigit()) or (char != 0 and word_l[char].isdigit() and (not word_l[char-1].isdigit())):
                result += self.__NUMBER
            elif char != 0 and word_l[char-1].islower() and word_l[char].isupper():
                result += self.__CAPITAL
            result += self.__char_to_braille(word_l[char])
        if word.isupper():
            result = self.__CAPITAL * 2 + result
        return result


    def __build_braille_word(self, trimmed_word, shavings, index, braille):
        # Translate a trimmed word to braille then re-attach the shavings.
        if shavings == "":
            braille += self.__word_to_braille(trimmed_word)
        else:
            for i in range(0, len(shavings)):
                if i == index and trimmed_word is not "":
                    braille += self.__word_to_braille(trimmed_word)
                braille += self.__word_to_braille(shavings[i])
            if index == len(shavings):  # If the shavings are all at the beginning.
                braille += self.__word_to_braille(trimmed_word)
        return braille


    def translate(self):
        # Convert alphabetic text to braille.
        braille = ""
        words = self.__extract_words(self.text)
        for word in words:
            trimmed_word = self.__trim(word)  # Remove punctuation (ex: change dog?" to dog)
            untrimmed_word = word
            index = untrimmed_word.find(trimmed_word)
            shavings = untrimmed_word.replace(trimmed_word, "")
            braille = self.__build_braille_word(trimmed_word, shavings, index, braille) #+ " "
            if braille[-1] != "\n":
                braille += " "
        return braille[:-1]  # Remove the final space that was added.
