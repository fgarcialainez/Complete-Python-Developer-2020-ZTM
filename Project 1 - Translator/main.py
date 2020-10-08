"""
This module implements the translator exercise of the Section 13 of the course.
"""

from translate import Translator


def translate():
    # Create the translator object
    translator = Translator(to_lang="ja")

    try:
        with open('./test.txt', mode='r') as file:
            # Read the contents of the file to translate
            text = file.read()

            # Translate the text to Japanese
            translation = translator.translate(text)

            # Write the results to a new file
            with open('./test-ja.txt', mode='w') as file2:
                file2.write(translation)
    except FileNotFoundError as e:
        print("Please check your file path!")


# Entry point of the program
if __name__ == '__main__':
    # Call the translate function
    translate()
