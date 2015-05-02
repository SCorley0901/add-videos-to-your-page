import webbrowser
import os

f = open("project3.html","w")
    
def get_items(p):
    lesson=p[0]
    lesson_title=p[1]
    session=p[2]
    session_title=p[3]
    session_description=p[4]
    return lesson, lesson_title, session, session_title, session_description



#Here's the data to be used to print the HTML - This is in the format Lesson #, Lesson title, Session #, Session title, session description

Text_List = [[1,"The First Lesson: How the Web works and other fun facts",1,"How the Web Works","""To many the Web is a mystery that can only be unlocked by a
 <em>nerd</em>. But how the Web works can be quite facinating to many. Basically, it's a huge network of computers talking to each other.
When your browser (Internet Explorer, Chrome, etc.) requests a web page the request is routed to the server that has the page.
That server then sends the requested document to your computer to display. The problem is that computers don't speak English.
 English, as are most human languages, is ambiguous. The main language for the Web is HTML (HyperText Markup Language). 
HTTP is the "grammer" of the Web. Url's are the addresses for the pages and files you are looking for. The Web was created in the early 1990's.
 It currently has about 30 billion pages."""],
[1, "The First Lesson: How the Web works and other fun facts", 2, "HTML", """HTML stands for HyperText Markup Language. 
 HTML documents form the majority of the content on the Web. HTML is made up of: 1) Text Content - What you see, 2) Markup - How your content looks, 
3) References to other documents e.g. Images and Videos, 4) Links to other pages"""],
[1, "The First Lesson: How the Web works and other fun facts",3,"Tag - The Element is It", """HTML documents are made of HTML elements.
 An element is made up of an opening tag, contents (the information you want to convey)
 , and a closing tag. The opening tag can also contain attributes that assist in coding and style."""],
[1, "The First Lesson: How the Web works and other fun facts",4,"Why Computers are like Spock on steroids", """Spock is very logical and also very literal. Agononizingly so.
 Computers aer just like that. Computers want everything exactly right. Spelling, syntax, indentation - everything has to be just right. Computers don't deal with ambiguity. If your code has issues then the computer will tell you. 
 Usually that means ugly error messages that leave you scratching your head wondering what it means."""],
[1, "The First Lesson: How the Web works and other fun facts",5,"To Inline or Block - That is the Question!???","""Some HTML elements just can't get out of the box.
 For instance p, div, and h> are examples of tags that form an invisible (or visible if you choose) 
box or block around the contents. Other tags are strickly in-line. Like for instance, the span tag"""],
[2,"Lesson 2: Treeing the Elusive HTML Code", 1, "The Tools of the Trade", """The tools programmers use are designed to aid the programmer.
 If you're going to get that HTML treed you're going to need the best tools you can get! 
Here are the tools we have covered so far - 1) Scratchpad - great for quick coding jobs, 2) Sublime Text - an awesome and helpful tool for coding HTML, CSS and Python, 3) 
CodePen - a great tool for HTML and CSS because it lets you see right away when you make changes to the code"""],
[2,"Lesson 2: Treeing the Elusive HTML Code", 2, "Structure from Chaos: 'Treeing' HTML", """
When it comes to HTML, being in the box is a good thing. Some HTML elements can contain many other HTML elements which in turn can contain many other HTML elements, and so on
, and so on.... This nesting of elements (think boxes) shows up as indentations in the code according to how many elements it is nested in.
 This gives rise to the idea of 'treeing' HTML"""],
[2,"Lesson 2: Treeing the Elusive HTML Code",3, "So What's in the box?","""If you are doing a good job of writing code then you indent as you go deeper into the nested boxes. The greater the indentation, the deeper in the
 nested boxes you are. Not indenting causes the code to be hard to read and can all create errors"""],
[3,"Lesson 3: Turning Plain HTML into a CSS Rock Star!",1, "Repetition is usually a problem","""No one likes to write the same code over and over. It's boring and it takes up time and space. More than that it means more errors and more debugging. Even more,
 what happens when your boss says he or she wants a different font used - and it's in fifty places in your code! HTML has an answer for that. Defining classes helps from repeating code over and over again. 
 If you need to make a change then it happens once in the class definition"""],
[3,"Lesson 3: Turning Plain HTML into a CSS Rock Star!",2, "Adding the CSS touch to HTML", """CSS (Cascading Style Sheets) is what makes HTML look good. This is a seperate language that addresses all the style issues that HTML has. The HTML must link to the corresponding CSS file.
 This gives the programmer the ability to change the way a page looks without changing the HTML. It also greatly assists in creating a common theme among related webpages."""],
[4,"Lesson 4: Introduction to Serious Programming",1,"Just what is a program?","""Computers are designed to run a specific sequence of instructions. It will do that time after time after time.... Then when a new set of instruction is needed the computer can start runnning those instructions.
That specific set of instructions to the computer is called the 'program'."""],
[4,"Lesson 4: Introduction to Serious Programming",2,"So what is Python?","""Computers need the instructions in a very specific way. The programming language helps us 'illogical' humans get the instructions right for the computer. Python is a high-level language designed take the code your write and convert it into the instructions the computer needs.
 This 'conversion' is done by the Python interpreter when you press 'run' or 'build'."""],
[4,"Lesson 4: Introduction to Serious Programming",3,"Is Python like English?","""Well, yes and no. Python has a grammer and syntax as English does. Past that though they are not very similar. English is full of ambiguity. As we said before computers don't deal well with that. Python is made up of a set of expressions that must conform to its syntax and grammer.
Failing to do so means errors. That's because Pythin needs to be instructed exactly. Close doesn't count at all....."""],
[5,"Lesson 5: Variables and Strings",1,"What is a variable in Python?","""Variable give programmer a way of keeping up with values. In a way it is 'naming a value'. Obviously though the variable name stays the same even if the value it points to changes.
 This gives a programmer a great deal of flexibility in writing code."""],
[5,"Lesson 5: Variables and Strings",2,"So how does Python assign a value to a variable?","""Let's say we have a variable name we want to use. Let's call it red_jelly_beans. Now we want to assign a value of 30 to it. Here's what the code looks like: 'red_jelly_beans=30'. 
 The value of red_jelly_beans can be changed as the program is run."""],
[5,"Lesson 5: Variables and Strings",3,"Isn't assigning a value to a variable in Python the same as equals in math?","""The short answer is no. in math the equals sign means 'is the same as'. In Python (and any other programming language) the equals sign means 
'takes the value of'."""],
[5,"Lesson 5: Variables and Strings",4,"Adding numbers and strings","""In Python, 2 is a number and '2' is a string. So, the code red_jelly_beans = 2+2 would give the value of 4 to red_jelly_beans. But the code red_jelly_beans='2'+'2' would give the value '22' to red_jelly_beans."""],
[6,"Lesson 6: Input->Function->Output",1,"What is a function?","""Programs handle repetitive tasks easily. Many times a program may need to use the same code over and over.
 This is where a function comes in. You define the function based on the input you need to give it. and the output you expect. The function then does the required code over and over every time it is called in the program."""],
[6,"Lesson 6: Input->Function->Output",2,"What's the difference between making and using a function?","""Function are defined by the first line of the function starting with the keyword 'def' followed by the name and then input parameters in parentheses. The body of the function comes next.
 This is the code that is the job you need the function to perform. The code must be indented under the defining statement. Last it ends with a 'return' keyword and the values being passed back to the program.
  When the main program neds to use the function it is called by using the name of the function followed by the input parameters in parentheses."""],
[6,"Lesson 6: Input->Function->Output",3,"Function Grammer","""Functions have to follow the same grammer rules the the main Python program follows. This means that the 'def'statement has to follow the correct syntax as well as the body and return statement.
 Failure to follow the correct sytax will cause some crazy errors. Failure to 'call the function' correctly from the main program will also mean incorrect or no output from the function. Failure to include the 'return statement' will get you this when it is called: 'none'"""],  
[7,"Lesson 7: Control Flow and Loops: If and While",1,"Decisions and Repetition","Programs need to make decisions just like humans do. They also need a way to do those same old boring tasks the number of times requested of them. That's where the 'if' and 'while' statements come in"],
[7,"Lesson 7: Control Flow and Loops: If and While",2,"The 'if' statement","""The 'if' statement runs a block of code depending on the evauation of a conditional expression. If the expression evaluates to boolean True then the block of code is run. If the expression evauates to boolean False then the the next line following the conditional code is run."""],
[7,"Lesson 7: Control Flow and Loops: If and While",3,"The 'while' statement","""The 'while' statement will loop on a block of code. The while loop is created by the 'while statement' The code is run time after time until the expression included in the 'while' statement is no longer true. Then program execution falls to the next line of code after the 'while' block."""],
[8,"Lesson 8: Debugging",1,"Getting the 'Bugs' out of Python code","Very few programs will run perfect the first time. Usually they have issues that need to be fixed. These are called bugs. Pythin helps the programmer by giving a Traceback error message that helps locate the bugs. Here are a few other techniques to debug a program."],
[8,"Lesson 8: Debugging",2,"Examine Error Messages When Programs Crash","""The last line of Python tracebacks will tell you what went wrong. Reading backwards from there will help you trace back to the origin of the problem."""],
[8,"Lesson 8: Debugging",3,"Work From Example Code","If your modified code doesn't work then comment it (# at the beginning of the line). Then do step-by-step modifications to the example code until it does what you want."],
[8,"Lesson 8: Debugging",4,"Check (Print) Intermediate Results","When your code doesn't crash, but doesn't behave as you expected, add print statements to your program to see where the code stops behaving correctly."],
[8,"Lesson 8: Debugging",5,"Keep and Compare Old Versions","When you have a working version of your code, save it before you add new code."],
[9,"Lesson 9: Structured Data: Lists and For Loops",1,"What is the difference between a string and a list?","A string is a sequence of characters. They can be letters, numbers, or symbols. A list on the other hand can be a sequence of anything."],
[9,"Lesson 9: Structured Data: Lists and For Loops",2,"What is a list?","A list can be a sequence of anything. That includes strings, and numbers. What really makes lists so powerfule is that they can also include other lists. So a list can be any sequence of strings, numbers or lists."],
[9,"Lesson 9: Structured Data: Lists and For Loops",3,"Mutation","lists support mutation. In other words, we can change the value of a list after we have created it.You can change the elements of a list you create. You can also add additional elements to a list"],
[9,"Lesson 9: Structured Data: Lists and For Loops",4,"Aliasing","Aliasing is two different ways of refering to the same object. For instance when we assign the value of a list element to a variable then both the variable name and the List point to the same object."],
[9,"Lesson 9: Structured Data: Lists and For Loops",5,"for Loops","for loops give the programmer a great way to work through a list. The syntax is 'for name in list:'. This will set up a loop that will execute a block of code for each element in the list"],
[10,"Lesson 10: How to Solve Problems",1,"First - Understand the computational problem","The problem is defined by possible inputs (the input set) and the relationships between the input set and the desired outputs. The solution is the procedure that takes the input set and gives you the desired output."],
[10,"Lesson 10: How to Solve Problems",2,"Second - Ask what the inputs are","Don't assume you knowwhat the inputs are. Make sure you ask and define the inputs asa closely as possible. Then go through some possible inputs that might be originally not thought of."],
[10,"Lesson 10: How to Solve Problems",3,"Third - Know the desired output","Again, don't make assumptions. Make sure you know what the desire output is and the form it needs to be in."],
[10,"Lesson 10: How to Solve Problems",4,"Forth - Solve the problem","""This requires understanding the relationships between the inputs and outputs. Usually this requires working through a set of examples to better define the relationships. What you are trying to do is work out a valid algorithm. Try to find a simple mechanical solution.
Don't try to prematurly optimize prematurely"""],
[10,"Lesson 10: How to Solve Problems",5,"Fifth - Develop incremental steps","Don't try to write the code for the whole solution all at once. Figure out small steps that you can test and gradually work towards the solution."],
[11,"Lesson 11: Introduction to Abstraction",1,"The First Step in Object Oriented Thinking and Programming","""Abstract thinking is required for Object Oriented Programming. For instance, a man is just a general or abstract term not refering to any particular man.
John Smith is a name that refers to a particular object - in this case a man. 'Man' is a class and 'John Smith' is an object in that class. Object oriented programming gives a programmer the ability to break a program up and bring in work that others have created. It lets a programming project become a team sport!"""],
[12,"Lesson 12: Digging a Little Deeper With Functions",1,"Using Functions from the Python Standard Library", """This lesson introduced the concept of using functions that exist in the Python standard library. In essence we can use code that others have written. This lets us focus on the probelm we are coding for and not having to re-invent the wheel. 
You can Google 'Python Standard Library' and see a listing of all the functions and classes that are available to use."""],
[12,"Lesson 12: Digging a Little Deeper With Functions",2,"Including External Functions In Your Code","""It's really easy to pull a function in from the Python library. It requires adding a statement at the beginning of your code - 'import' and then the name of the function you are importing.
Then you need to follow the syntax and arguments as define in the Python Standard Library for that function. Two great functions we looked at were 'webbrowser' and 'time'."""],
[13,"Lesson 13: The Power of the Class",1,"What Are Classes?","""A class is like a blueprint. It defines the structure of a building. It does not define any particular building, but how a particular building needs to be constructed. This is what abstraction is all about. 
Every time the blueprint is used to build a building an instance of the blueprint becomes a reality. Each instance uses the same blueprint but may not have all the same details - like for instance color."""],
[13,"Lesson 13: The Power of the Class",2,"How do you use classes?","""In many ways using classes in your code looks similar to using imported functions. The difference lies in how classes use memory and functions too. Every time a class is initialized an instance of that class is created in memory. A class can contain many functions (methods). 
As a programmer you don't need to know how the class does its job. You only need to know what arguments it is looking for and what it returns"""],
[13,"Lesson 13: The Power of the Class",3,"Some examples of Classes","""We looked at and used several classes in a couple of programming problems. First we used the class 'Turtle' in the Python Standard Library to draw interesting images. 
Next, we used an external library to pull in a class that handles various communication requirements. In this case we used 'Twilio' to create a short Python program that would send a text."""],
[13,"Lesson 13: The Power of the Class",4,"Using a website like a class","""This was an awesome example of using a website in an abstarct way. We sent a string to a website and it returned a string telling us if there was profanity in the string we sent. This worked very much like a class. This was a great example of abstraction."""],
[14,"Lesson 14: Making Our Own Classes",1,"The Basics of Creating a Class","""To begin, the class you are creating should be in a Python file by itself. The class file needs to be in the same folder as the main program you are creating. It is possible to code the main calling program to look in a different directory. 
The class you are creating can call other classes or functions. After any import statements you may have will be the opening class statement. The syntax is ' class Name():'. Name is the name of the class starting with a capital letter."""],
[14,"Lesson 14: Making Our Own Classes",2,"Keywords Involved In Creating Classes","""These are important keywords or ideas in classes: 1. Class - An abstraction of an Object. 2. init - 'def__init__(self' is the statement that initiates the instance of the classes and defines the arguments. 
    3. Constructor - the def/init statement is the constructor for the class. 4. self - self is the object being created. 5. Instance Variable - variables that are used strickly within the instance of a class. 6. instance method - a function that is defined within a class and used within an instance."""],
[15,"Lesson 15: Advanced OOP Topics",1,"Class Variables and Instance Variables", """As we said earlier Instance variable are used specifically be a particular instance. These are not available to other instances. Class variables are available though. Every class comes with some class vaiables - like doc, name and module."""],
[15,"Lesson 15: Advanced OOP Topics",2,"Help on Python","""There are so many ways to get help with a particular problem or question. Python's website is a great resource for documentation. Google also has many resources including the style guide for Python code. For instance, the style guide suggests that variables that will remain constant 
have their names in all caps."""],
[15,"Lesson 15: Advanced OOP Topics",3,"Inheritance","""There can be a parent/child structure to a class. If your class is structured that way then variables in the parent class can be inherited by the child class."""],
[15,"Lesson 15: Advanced OOP Topics",4,"One Last Example Of Classes","""Imagine you had a bucket with fish in it. You looked in it and you had three salmon in the bucket. You decided to name the salmon Frank, Joe and Mary (yes you have issues, but what programmer doesn't?). Fish would be a class, Salmon would also be a class, but Mary would be an object or instance."""],
[15,"Lesson 15: Advanced OOP Topics",5,"A Couple of Great OOP Videos", """These are a couple of OOP Basics videos that I really found helpful!!"""]]
# Print the HTML from DOCTYPE to Table of Contents (TOC)

f.write('''<!DOCTYPE html>
<html lang="en-US" dir="ltr">
<head>
    <meta charset="utf-8">
    <title>Steve's Notes on HTML, CSS, and Python</title>
    <link rel="stylesheet" href="Project1-style.css">
</head>
<body>
    <div class="TOC-Title">
        <h1>Table of Contents</h1>
            <ol>''');

# Print the HTML for the Table of contents
#
# There are two nested for loops. The first loops through the lessons and the second loops through the main thoughts in each lesson.
#It is assumed that the lesson # and session # are in ascending numerical order.

lesson_counter=0 # initialize the variable that will control printing the lesson header

for e in Text_List:
    (lesson, lesson_title, session, session_title, session_description) = get_items(e)

    #Print the Table of Contents Lesson header
    if lesson != lesson_counter:
        f.write('\n                <li class="TOC-lesson"><a href="#lesson-'+str(lesson)+'">'+str(lesson_title)+'</a>');
        lesson_counter=lesson
        f.write('\n                    <ul>');
        # Print the session listings for the Table of Contents
        lesson_counter2 = lesson_counter
        for e2 in Text_List:
            (lesson, lesson_title, session, session_title, session_description) = get_items(e2)
            if lesson==lesson_counter2:
                f.write('\n                         <li><a href="#lesson-'+str(lesson)+'-'+str(session)+'">'+session_title+'</a></li>');
        f.write('\n                    </ul>');
        f.write('\n                </li>');

# Close the Table of Contents
f.write('\n            </ol>');
f.write('\n    </div>');

# Open the description section - This is a summation of each session within a lesson

f.write('\n    <h1>Lesson/Session Summations</h1>');
f.write('\n    <div class="lesson">');


# Nested for loops for printing Lesson/session summations

lesson_counter = 0

for e in Text_List:
    (lesson, lesson_title, session, session_title, session_description) = get_items(e)

    # Print the lesson header
    if lesson != lesson_counter:
        f.write('\n         <h2 id="lesson-'+str(lesson)+'">'+str(lesson_title)+'</h2>');
        lesson_counter=lesson

        # Print the session header and description
        lesson_counter2 = lesson_counter
        for e2 in Text_List:
            (lesson, lesson_title, session, session_title, session_description) = get_items(e2)
            if lesson==lesson_counter2:
                f.write('\n             <div class="concept" id="lesson-'+str(lesson)+'-'+str(session)+'">');
                f.write('\n                 <div class="concept-title">'+str(session_title)+'</div>');
                f.write('\n                 <div class="concept-description">');
                f.write('\n                     <p>');
                f.write('\n                         '+str(session_description));
                if lesson==15 and session ==5:
                    f.write('<a href="https://www.youtube.com/watch?v=SZqLEDH0x7A&list=WL&index=54">  This video</a> gives a good overview of abstraction.');
                    f.write('<a href="https://www.youtube.com/watch?v=SS-9y0H3Si8&index=53&list=WL">  This video</a> gives a good overview of OOP.');
                f.write('\n                     </p>');
                f.write('\n                 </div>');
                f.write('\n             </div>');

# Close the HTML Body
f.write('\n    </div>');
f.write('\n    <img src="http://jigsaw.w3.org/css-validator/images/vcss" alt="CSS Validated by W3">');
f.write('\n</body>');
f.write('\n</html>');
f.close()

# Open the output file in a new browser tab
url = os.path.abspath(f.name)
webbrowser.open('file://' + url, new=2) # open in a new tab, if possible





