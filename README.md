# GUI-Vocabulary-Flashcards
this code provides an interactive GUI and dynamic way for users to learn French vocabulary using flashcards.

1} 
This code is a flashcard application implemented using the tkinter library in Python. It allows users to learn and practice French vocabulary. The code displays a graphical user interface (GUI) window with a canvas where the flashcards are shown. The front side of the flashcard displays a French word, and the back side shows the corresponding English translation.

2}
The code reads data from a CSV file that contains French words and their English translations. If the file is not found, it falls back to a default CSV file. The data is then stored as a dictionary for efficient retrieval. The program randomly selects a flashcard from the dictionary and displays the French word on the front side. After a delay of 3 seconds, the card automatically flips to show the English translation on the back side.

3}
The GUI window also includes two buttons: a cross button to indicate that the user doesn't know the translation and wants to skip to the next card, and a right button to indicate that the user knows the translation. Clicking the right button removes the current flashcard from the dictionary and updates the CSV file accordingly. The next card is then displayed.
