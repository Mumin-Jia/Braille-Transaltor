# Braille-Transaltor
The main purpose of this project is translating normal English text to grade two braille, which can be used on translating website or braille printers to supply reading materials for vision impaired people.

There are three python files to finish translating tasks. The basic part of the translating system is the mapping file, “mapAlphaToBraille”, to create dictionary for letters, contractions, punctuation, abbreviation and numbers in Braille. The second file “main.py” contains “open_text” function and test cases. The “open_text” function takes file name as parameter, and try to open the text file with the file name and return the contents as a single string. It also catches open file error, and if the error occurs, it will ask user to re-enter the file name until the file can be opened. After “open_text” function successfully returns the text, main.py uses “translate” method in “Translate” class, which is the second part of the translating system, to finish translating.

As the above mentioned, the main part is the “alphaToBraille.py”. The whole translating process is finished by the Translate class. There are four static variables in the class, which are indicates for capital, letter, number, and abbreviations. The constructor of the class only takes English text as parameter. The public method, “translate” method in the class uses the following algorithm to finish translating English text to grade 2 braille:

•	Separate the text string by blank space and new-line character by using method “__extract_words”.
•	Loop through each word in the word list. For each word, using “__trim” method to separate words and punctuations. For example, “cat?” will become to [“cat”, “?”]?
•	Remember the position of punctuations, and call “__build_braille_word” method to convert the words and then re-attach shavings.
•	“__word_to_braille” method separate the words further. It separates words into the abbreviations and characters, and call “__char_to_braille” method to do the final translating.
•	“__char_to_braille” method takes “word list” and translate words character by character according to “mapAlphaToBraille” map.
•	All braille characters then are assembled and are returned back to “translate” method to form the final braille character string. 
