import alphaToBraille

def open_text(filename):
    while True:
        try:
            file = open(filename)
            return file.read()
        except:
            filename = input("Cannot find the file, please try again: ")
        
text_file = input("Please Enter the Text File Name: ")
text = open_text(text_file)

trans = alphaToBraille.Translate(text)
print("\nThe Braille code is:\n",trans.translate())