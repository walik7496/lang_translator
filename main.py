from tkinter import *
from translate import Translator

# Create the main window with a unique design
translator_app = Tk()
translator_app.title("Universal Language Translator")
translator_app.geometry("500x300")

# Change font and background colors for the app
translator_app.config(bg="lightblue")

# Declare variables for source and target languages
source_language = StringVar()
target_language = StringVar()

# List of available languages for translation
languages = {'English', 'French', 'German', 'Spanish', 'Hindi', 'Italian', 'Chinese'}
source_language.set('English')  # Set default input language
target_language.set('French')  # Set default output language

# Function to perform translation with error handling
def perform_translation():
    try:
        translator = Translator(from_lang=source_language.get(), to_lang=target_language.get())
        translated_text = translator.translate(input_text.get())
        output_text.set(translated_text)  # Set the translated text in output field
    except Exception as e:
        output_text.set(f"Error: {str(e)}")  # Display error if translation fails

# Dropdown menu to select input language
source_language_menu = OptionMenu(translator_app, source_language, *languages)
Label(translator_app, text="Select Input Language", bg="lightblue").grid(row=0, column=1)
source_language_menu.grid(row=1, column=1)

# Dropdown menu to select output language
target_language_menu = OptionMenu(translator_app, target_language, *languages)
Label(translator_app, text="Select Output Language", bg="lightblue").grid(row=0, column=2)
target_language_menu.grid(row=1, column=2)

# Input field for entering text to be translated
Label(translator_app, text="Enter Text:", bg="lightblue").grid(row=2, column=0)
input_text = StringVar()
input_entry = Entry(translator_app, textvariable=input_text, width=40).grid(row=2, column=1)

# Output field to display the translated text
Label(translator_app, text="Translated Text:", bg="lightblue").grid(row=2, column=2)
output_text = StringVar()
output_entry = Entry(translator_app, textvariable=output_text, width=40).grid(row=2, column=3)

# Button to trigger the translation process
translate_button = Button(translator_app, text="Translate Now", command=perform_translation, relief=GROOVE).grid(row=3, column=1, columnspan=3)

# Run the main loop for the app
translator_app.mainloop()
