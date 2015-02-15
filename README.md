# bookmarkManager
simple command line application created with python 2.7 that manages bookmark entries

How to use the program
-
To run the program, the user has to open the .py-file in the IDLE-2 shell and
press the F5 key to run the code.


Functionalities
-
Upon start of the program the current list of bookmarks will be displayed.
Several inputs from the user are excepted. By entering a number of
the displayed bookmarks, the corresponding website will be opened
in the default webbrowser of the user. The date and time of the last access
of a bookmark will be saved and displayed behind the bookmark entries.
By typing "s" the user can search for an existing bookmark. The program
is capable of finding entries by short, matching patterns of letters. All
entries that match the pattern will be displayed.
It is possible to add bookmark entries by typing "+" and to delete them by
typing "-". To add, the user enters the name and the address of the website
seperately. After that the bookmark will be listed last in the bookmark list.
To delete an entry, the user enters the corresponding number of the bookmark.


How the code works
-
The program is embedded in a while loop that keeps repeating until the user
enters "x" to exit the program. Upon start of the loop a file containg all
current bookmarks will be opened. This is done with the json module.
The design of the bookmark list is created with a combination of print statements
and the format function. The format function defines the distance of the list
elements displayed. To realise an ongoing display of numbers for the bookmarks, even
if new ones are added, a forloop is used, that scans through the bookmarks list and
uses a number between 0 and the current length of the bookmarks list. To reduce the
display of the bookmarks to a number of 20 characters, a function "limiter" is defined.
This function takes two arguments. If the first argument extends the second arguments,
only the first 20 characters will be displayed plus "...".
Inside the while loop are several if conditions nested. The first one terminates
the program when the user input is x. This is realized with a "break" statement.
The second condition (elif) excepts "+" as an input and appends the user input to
the bookmark list, also adding "N/A" as the default value for the last access.
A function is called that will write the changes of the bookmarks list to the json
file.
The third condition (elif) excepts "-" as an input. The entered number will be
converted to an integer and will be removed from the bookmarks list. These changes
will also be saved to the json file by calling the file_write function.
The fourth condition (elif) searches the user input in the bookmarks list at the
"name" position.
