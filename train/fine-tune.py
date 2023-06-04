
from txtai.pipeline import HFTrainer
trainer = HFTrainer()
data = [
    {
    
    "question": "What is Python?",
    
    "context": "Python is a high-level, interpreted, interactive, and object-oriented scripting language. It uses English keywords frequently. Whereas, other languages use punctuation, Python has fewer syntactic constructions.",
    
    "answers": "Python is a high-level, interpreted, interactive, and object-oriented scripting language."
    
    },
    {
    
    "question": "Python is an interpreted language. Explain.?",
    
    "context": "An interpreted language is any programming language that executes its statements line by line. Programs written in Python run directly from the source code, with no intermediary compilation step.",
    
    "answers": "An interpreted language"
    
    },  

    {
    
    "question": "What is the difference between lists and tuples?.",
    
    "context": "Lists are mutable, i.e., they can be edited	Tuples are immutable (they are lists that cannot be edited) Lists are usually slower than tuples	Tuples are faster than lists Lists consume a lot of memory	Tuples consume less memory when compared to lists Lists are less reliable in terms of errors as unexpected changes are more likely to occur	Tuples are more reliable as it is hard for any unexpected change to occur Lists consist of many built-in functions.	Tuples do not consist of any built-in functions.S",
    
    "answers": "Lists are mutable, i.e., they can be edited	Tuples are immutable"
    
    },

    {
    
    "question": "What is pep 8?",
    
    "context": "PEP in Python stands for Python Enhancement Proposal. It is a set of rules that specify how to write and design Python code for maximum readability.",
    
    "answers": "PEP in Python stands for Python Enhancement Proposal"
    
    },
    {
    
    "question": "What are the Key features of Python?",
    
    "context": "Python is an interpreted language, so it doesn’t need to be compiled before execution, unlike languages such as C.Python is dynamically typed, so there is no need to declare a variable with the data type. Python Interpreter will identify the data type on the basis of the value of the variable.object-oriented programming,cross-platform language,general-purpose language",
    
    "answers": "object-oriented programming,cross-platform language,general-purpose language"
    
    },
    
    {
    
    "question": "How is Memory managed in Python?",
    
    "context": "Memory in Python is managed by Python private heap space. All Python objects and data structures are located in a private heap. This private heap is taken care of by Python Interpreter itself, and a programmer doesn’t have access to this private heap. Python memory manager takes care of the allocation of Python private heap space. Memory for Python private heap space is made available by Python’s in-built garbage collecto Memory for Python private heap space is made available by Python’s in-built garbage collector",
    
    "answers": "Memory for Python private heap space is made available by Python’s in-built garbage collector"
    
    },
 
    {
    
    "question": "What is PYTHONPATH?",
    
    "context": "PYTHONPATH has a role similar to PATH. This variable tells Python Interpreter where to locate the module files imported into a program. It should include the Python source library directory and the directories containing Python source code. PYTHONPATH is sometimes preset by Python Installer.",
    
    "answers": "PYTHONPATH has a role similar to PATH"
    
    },
    {
    
    "question": "What are Python Modules?",
    
    "context": "Files containing Python codes are referred to as Python Modules. This code can either be classes, functions, or variables and saves the programmer time by providing the predefined functionalities when needed. It is a file with “.py” extension containing an executable code.",
    
    "answers": "Files containing Python codes are referred to as Python Modules."
    
    },
    {
    
    "question": "What are python namespaces?",
    
    "context": "A Python namespace ensures that object names in a program are unique and can be used without any conflict. Python implements these namespaces as dictionaries with ‘name as key’ mapped to its respective ‘object as value’.",
    
    "answers": "A Python namespace ensures that object names in a program are unique and can be used without any conflict."
    
    },
      {
    
    "question": "Explain Inheritance in Python with an example?",
    
    "context": "As Python follows an object-oriented programming paradigm, classes in Python have the ability to inherit the properties of another class. This process is known as inheritance. Inheritance provides the code reusability feature. The class that is being inherited is called a superclass or the parent class, and the class that inherits the superclass is called a derived or child class. The following types of inheritance are supported in Python. Single inheritance Multiple inheritance Multilevel inheritance Hierarchical inheritance",
    
    "answers": "Single inheritance Multiple inheritance Multilevel inheritance Hierarchical inheritance"
    
    },
  
    {
    
    "question": "What is scope resolution?",
    
    "context": "A local scope refers to the local objects included in the current function. A global scope refers to the objects that are available throughout execution of the code.A scope is a block of code where an object in Python remains relevant.Each and every object of python functions within its respective scope.As Namespaces uniquely identify all the objects inside a program but these namespaces also have a scope defined for them where you could use their objects without any prefix. It defines the accessibility and the lifetime of a variable.",
    
    "answers": "A local scope refers to the local objects included in the current function. A global scope refers to the objects that are available throughout execution of the code."
    
    },
    {
    
    "question": "What is a dictionary in Python?",
    
    "context": "A scope is a block of code where an object in Python remains relevant.Each and every object of python functions within its respective scope.As Namespaces uniquely identify all the objects inside a program but these namespaces also have a scope defined for them where you could use their objects without any prefix. It defines the accessibility and the lifetime of a variable.",
    
    "answers": "A scope is a block of code where an object in Python remains relevant."
    
    },
    {
    
    "question": "What are functions in Python?",
    
    "context": "A function is a block of code which is executed only when a call is made to the function. def keyword is used to define a particular function as shown below",
    
    "answers": "A function is a block of code which is executed only when a call is made to the function"
    
    },
    {
    
    "question": "What is __init__ in Python?",
    
    "context": "Equivalent to constructors in OOP terminology, __init__ is a reserved method in Python classes. The __init__ method is called automatically whenever a new object is initiated. This method allocates memory to the new object as soon as it is created. This method can also be used to initialize variables.",
    
    "answers": "Equivalent to constructors in OOP terminology, __init__ is a reserved method in Python classes."
    
    },
   
    {
    
    "question": "What are the common built-in data types in Python?",
    
    "context": "Python supports the below-mentioned built-in data types: Immutable data types: Number String Tuple",
    
    "answers": "Number String Tuple"
    
    },
    {
    
    "question": "What are local variables and global variables in Python?",
    
    "context": "Local variable: Any variable declared inside a function is known as Local variable and it’s accessibility remains inside that function only. Global Variable: Any variable declared outside the function is known as Global variable and it can be easily accessible by any function present throughout the program.Local variable: Any variable declared inside a function is known as Local,Global Variable: Any variable declared outside the function is known as Global variable and it can be easily accessible by any function present throughout the program.Local variable: Any variable declared inside a function is known as Local,Global Variable: Any variable declared outside the function is known as Global variable and it can be easily accessible by any function present throughout the program. Local variable: Any variable declared inside a function is known as Local,Global Variable: Any variable declared outside the function is known as Global variable and it can be easily accessible by any function present throughout the program.",
    
    "answers": "Local variable: Any variable declared inside a function is known as Local,Global Variable: Any variable declared outside the function is known as Global variable and it can be easily accessible by any function present throughout the program."
    
    },
    {
    
    "question": "What is type conversion in Python?",
    
    "context": "Python provides you with a much-needed functionality of converting one form of data type into the needed one and this is known as type conversion.Implicit Type Conversion: In this form of type conversion python interpreter helps in automatically converting the data type into another data type without any User involvement.",
    
    "answers": "Implicit Type Conversion: In this form of type conversion python interpreter helps in automatically converting the data type into another data type without any User involvement."
    
    },
      {
    
    "question": "How to install Python on Windows and set a path variable?",
    
    "context": "After that, install it on your PC by looking for the location where PYTHON has been installed on your PC by executing the following command on command prompt isit advanced system settings and after that add a new variable and name it as PYTHON_NAME and paste the path that has been copied.cmd python.",
    
    "answers": "cmd python."
    
    },  
    {
    
    "question": "What is the difference between Python Arrays and lists?",
    
    "context": "List array Consists of elements belonging to different data types	Consists of only those elements having the same data type No need to import a module for list declaration	Need to explicitly import a module for array declaration Can be nested to have different type of elements	Must have all nested elements of the same size Recommended to use for shorter sequence of data items	Recommended to use for longer sequence of data items More flexible to allow easy modification (addition or deletion) of data	Less flexible since addition or deletion has to be done element-wise Consumes large memory for the addition of elements	Comparatively more compact in memory size while inserting elements Can be printed entirely without using looping	A loop has to be defined to print or access the components",
    
    "answers": "List array"
    
    },
    {
    
    "question": "Is python case sensitive?",
    
    "context": "Yes, Python is a case sensitive language. This means that Function and function both are different in pythons like SQL and Pascal.",
    
    "answers": "Python is a case sensitive language."
    
    },
    {
    
    "question": "What does [::-1] do?",
    
    "context": "[::-1] ,this is an example of slice notation and helps to reverse the sequence with the help of indexing.Output: 5,4,3,2,1",
    
    "answers": "Output: 5,4,3,2,1"
    
    },
        {
    
    "question": "What are Python packages?",
    
    "context": "In Python, decorators are necessary functions that help add functionality to an existing function without changing the structure of the function at all. These are represented by @decorator_name in Python and are called in a bottom-up format.",
    
    "answers": "In Python, decorators are necessary functions that help add functionality to an existing function"
    
    },
        {
    
    "question": "Is indentation required in Python?",
    
    "context": "Indentation in Python is compulsory and is part of its syntax.All programming languages have some way of defining the scope and extent of the block of codes. In Python, it is indentation. Indentation provides better readability to the code, which is probably why Python has made it compulsory.",
    
    "answers": "All programming languages have some way of defining the scope and extent of the block of codes. In Python"
    
    }, 
    {
    
    "question": "How does break, continue, and pass work?",
    
    "context": "These statements help to change the phase of execution from the normal flow that is why they are termed loop control statements. Python break: This statement helps terminate the loop or the statement and pass the control to the next statement.Python break Python continue Python pass",
    
    "answers": "Python break Python continue Python pass"
    
    },
    {
    
    "question": "How can you randomize the items of a list in place in Python?",
    
    "context": "This can be easily achieved by using the Shuffle() function from the random library as shown below: from random import shuffle",
    
    "answers": "This can be easily achieved by using the Shuffle() function from the random library as shown below"
    
    },

       {
    
    "question": "How to comment with multiple lines in Python?",
    
    "context": "To add a multiple lines comment in python, all the line should be prefixed by #.",
    
    "answers": "To add a multiple lines comment in python, all the line should be prefixed by #."
    
    },
    {
    
    "question": "What type of language is python? Programming or scripting?",
    
    "context": "Generally, Python is an all purpose Programming Language ,in addition to that Python is also Capable to perform scripting.",
    
    "answers": "Python is an all purpose Programming Language"
    
    },
    {
    
    "question": "What are negative indexes and why are they used?",
    
    "context": "To access an element from ordered sequences, we simply use the index of the element, which is the position number of that particular element. The index usually starts from 0, i.e., the first element has index 0, the second has 1, and so on.When we use the index to access elements from the end of a list, it’s called reverse indexing. In reverse indexing, the indexing of elements starts from the last element with the index number ‘−1’. The second last element has index ‘−2’, and so on. These indexes used in reverse indexing are called negative indexes When we use the index to access elements from the end of a list, it’s called reverse indexing. In reverse indexing, the indexing of elements starts from the last element with the index number ‘−1’. The second last element has index ‘−2’, and so on. These indexes used in reverse indexing are called negative indexes",
    
    "answers": "When we use the index to access elements from the end of a list, it’s called reverse indexing. In reverse indexing, the indexing of elements starts from the last element with the index number ‘−1’. The second last element has index ‘−2’, and so on. These indexes used in reverse indexing are called negative indexes"
    
    },
    {
    
    "question": "Explain split(), sub(), subn() methods of “re” module in Python?",
    
    "context": "These methods belong to the Python RegEx or ‘re’ module and are used to modify strings. split(): This method is used to split a given string into a list. sub(): This method is used to find a substring where a regex pattern matches, and then it replaces the matched substring with a different string. subn(): This method is similar to the sub() method, but it returns the new string, along with the number of replacements.",
    
    "answers": "These methods belong to the Python RegEx or ‘re’ module and are used to modify strings. split(): This method is used to split a given string into a list. sub(): This method is used to find a substring where a regex pattern matches, and then it replaces the matched substring with a different string. subn(): This method is similar to the sub() method, but it returns the new string, along with the number of replacements."
    
    },

    {
    
    "question": "What do you mean by Python literals?",
    
    "context": "Literals refer to the data which will be provided to a given in a variable or constant. Literals supported by python are listed below: String Literals These literals are formed by enclosing text in the single or double quotes. String Literals Numeric Literals",
    
    "answers": "String Literals Numeric Literals"
    
    },
    {
    
    "question": "What is a map function in Python?",
    
    "context": "The map() function in Python has two parameters, function and iterable. The map() function takes a function as an argument and then applies that function to all the elements of an iterable, passed to it as another argument. It returns an object list of results.",
    
    "answers": "The map() function in Python has two parameters, function and iterable."
    
    },
  
       {
    
    "question": "What are the generators in python?",
    
    "context": "Generator refers to the function that returns an iterable set of items.",
    
    "answers": "Generator refers to the function that returns an iterable set of items."
    
    },
        {
    
    "question": "What are python iterators?",
    
    "context": "These are the certain objects that are easily traversed and iterated when needed.",
    
    "answers": "These are the certain objects that are easily traversed and iterated when needed."
    
    },
    
    {
    
    "question": "Do we need to declare variables with data types in Python?",
    
    "context": "These are the certain objects that are easily traversed and iterated when needed. No. Python is a dynamically typed language, I.E.",
    
    "answers": "No. Python is a dynamically typed language, I.E."
    
    },
    {
    
    "question": "What are Dict and List comprehensions?",
    
    "context": "Python comprehensions are like decorators, that help to build altered and filtered lists, dictionaries, or sets from a given list, dictionary, or set. Comprehension saves a lot of time and code that might be considerably more complex and time-consuming.Performing mathematical operations on the entire list Performing conditional filtering operations on the entire list Combining multiple lists into one Flattening a multi-dimensional list",
    
    "answers": "Performing mathematical operations on the entire list Performing conditional filtering operations on the entire list Combining multiple lists into one Flattening a multi-dimensional list"
    
    }, 
    {
    
    "question": "How do you write comments in python?",
    
    "context": "Python Comments are the statement used by the programmer to increase the readability of the code. With the help of #, you can define the single comment and the other way to do commenting is to use the docstrings(strings enclosed within triple quotes). Comments in Python  print('Comments in Python')",
    
    "answers": "Comments in Python  print('Comments in Python')"
    
    },
      {
    
    "question": "Is multiple inheritance supported in Python?",
    
    "context": "Yes, unlike Java, Python provides users with a wide range of support in terms of inheritance and its usage. Multiple inheritance refers to a scenario where a class is instantiated from more than one individual parent class. This provides a lot of functionality and advantages to users.",
    
    "answers": "unlike Java, Python provides users with a wide range of support in terms of inheritance and its usage"
    
    },
   
    {
    
    "question": "What is the difference between range  xrange?",
    
    "context": "Functions in Python, range and xrange are used to iterate in a for loop for a fixed number of times. Functionality-wise, both these functions are the same. The difference comes when talking about Python version support for these functions and their return values.",
    
    "answers": "Functions in Python, range and xrange"
    
    },
   
    {
    
    "question": "What is pickling and unpicklin",
    
    "context": "The Pickle module accepts the Python object and converts it into a string representation and stores it into a file by using the dump function. This process is called pickling. On the other hand, the process of retrieving the original Python objects from the string representation is called unpickling.",
    
    "answers": "The Pickle module accepts the Python object and converts it into a string representation and stores"
    
    }, 
    
    {
    
    "question": "What do you understand by Tkinter?",
    
    "context": "Tkinter is a built-in Python module that is used to create GUI applications. It is Python’s standard toolkit for GUI development. Tkinter comes with Python, so there is no separate installation needed. You can start using it by importing it in your script.",
    
    "answers": "Tkinter is a built-in Python module that is used to create GUI applications."
    
    },
    {
    
    "question": "Is Python fully object oriented?",
    
    "context": "Python does follow an object-oriented programming paradigm and has all the basic OOPs concepts such as inheritance, polymorphism, and more, with the exception of access specifiers. Python doesn’t support strong encapsulation (adding a private keyword before data members). Although, it has a convention that can be used for data hiding, i.e., prefixing a data member with two underscores.",
    
    "answers": "Python does follow an object-oriented programming paradigm and has all the basic OOPs concepts such as inheritance, polymorphism, and more, with the exception of access specifiers."
    
    }, 
  
     
]  

model, tokenizer = trainer("deepset/bert-base-cased-squad2", data, task="question-answering", num_train_epochs=len(data))


# https://intellipaat.com/blog/interview-question/python-interview-questions/
