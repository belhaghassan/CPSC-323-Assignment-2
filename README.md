Berkeley C.,
Bilal El-haghassan, 
Nicholas Vuong, 
Thomas Lee
CPSC 323-04

CPSC 323 Assignment 2 Documentation

Problem Statement
	We must create a lexical analyzer for assignment 1. There is the option to build the entire lexer with a finite state machine or build our lexer using multiple finite state machines for identifiers, integers, and reals. A major component of our assignment will be to write a procedure/function “lexer()” that returns a token when it is needed. Our lexer function should return a record, one field for the token and another field that the actual value(lexeme) of the token will be recognized. The lexer should read the files containing the source code given by our professor to generate tokens and print the results to an output file.
	
How to use your program
To begin, in order for the file to run the user must have python installed on their machine. After confirming python is installed, the user must download and extract the zip file provided. Once the file has been downloaded onto the computer, the user must open the cmd line(assuming they are using a windows machine). With the terminal open, the user must navigate to the file location using the “cd” command and the pathway of the file, for example, “cd C:\Users\CSUFTitan\Lexical_Analyzer”. Now that the user is in the file location, they must type in the command line “python main.py” and press enter. This will run the program of the lexical analyzer which will tokenize and validate a source text file that the user passes. The user must also type in the name of the file they want the results to be outputted into, for example, a possible output file name would be “output.txt”. Once analyzed, the results will be recorded into an output file. In the output file, it will begin by stating which file was accessed and a list of the tokens and their lexemes will be shown.

Design of your program
Our lexer is written in the Python language and was developed in the Repl.it environment. 
The use of Python’s Lists was an integral part of our code as it was used to store the list of strings we used for reference. The list would be used for cross-referencing for whether the taken token was a keyword, identifier, separator, operator, real, or an unknown.
The use of Functions was a simple matter of how we wanted to organize our program, as we wanted our program to be readable and easy to debug. This also falls in line with how we made the Finite State Machine functions a separate file so that our program would be organized in how everything related to the Finite State Machine was in its own file and any other function we created was in another, separate from the main file.
The use of the Python library function isdigit() made it a relatively easy matter to tell whether the current token was a digit or not. If it was not a digit, it would move on to the next test; and if it was a digit, it would then test if the following token had a decimal to see if the token was a real number and not a standalone integer.
The separateElements function is a function that we created in order for us to split up the row of input into individual items and then identify whether it was a double operator, separator, or single operator. It would then concatenate each item together with space in between each item. Once left with a long concatenated string, we would then use the split library function to remove the spaces and return the string.
The use of the sys library was also an integral part of the project as we used the functions within it to create and write our program’s output into a text file.
The use of the os library was to check if the file that the user wants tokenized exists. Thus, serving as a form of input validation.
For our Finite State Machine, we used a matrix to identify the state of each input. Every input in the token would change the current state of the FSM depending on what type of token it is.

Any Limitations
Limitations we experienced included unavoidable schedule conflicts, lack of understanding of Finite State Machines, loss of touch with Python, and technical difficulties with Repl.it and Git. Inevitable schedule conflicts arose when members of our group had their jobs to go to. Due to being unable to skip or reschedule the days they had to work on or having to prioritize their jobs more, our other members had to either wait for those who were gone to work on the project or had to work on the project without them. The same can be said for our group members’ familial circumstances which were also unavoidable. The lack of understanding of Finite State Machines was simply due to it being a fairly difficult subject for some of our members to grasp. Those who did understand what Finite State Machines are and what they do have to take some time to explain to our other group members in a way that they could understand. Thus, leaving us with less time to work on the project than we would have had. The loss of touch with Python is another simple limitation in how quite some time has passed since some of our group members coded in the language. Those who were familiar with Python had to take some time to refresh themselves so that they can work on the project efficiently. We also had to wait for the other members to learn the language themselves and with the aid of the members who were already familiar with the language, they learned Python fairly quickly. This also helped the members who knew Python to refresh their knowledge of the language. Learning Python was not very difficult for the members who were not familiar with it, nor was it a long process as it is very similar to C Plus Plus which all of us are familiar with. Technical difficulties with Repl.it included lag while we were coding and random disconnections from their servers. There was also an unfortunate accident involving Git where one of our members forgot to push our project after committing the changes.

Any shortcomings
None.


References:
Bhaskarcbhaskarc 7, Alexey KachayevAlexey Kachayev 5, Iliyan BobevIliyan Bobev 2, MrKelleymrKelley 2, Joran BeasleyJoran Beasley 91.8k1111 gold badges125125 silver badges152152 bronze badges, Adrian RatnapalaAdrian Ratnapala 4, . . . Dansalmodansalmo 10.1k44 gold badges4949 silver badges4848 bronze badges. (1962, April 01). Iterating over a 2 dimensional Python list. Retrieved March 07, 2021, from https://stackoverflow.com/questions/16548668/iterating-over-a-2-dimensional-python-list
Python matrices and numpy arrays. (n.d.). Retrieved March 07, 2021, from https://www.programiz.com/python-programming/matrix
Repl.it. (n.d.). The collaborative browser based IDE. Retrieved March 07, 2021, from https://repl.it/
Sebesta, Robert W.(2016) Concepts of Programming Languages(Eleventh Ed.). Harlow, England: Pearson Education Limited. Retrieved January 10, 2021.
