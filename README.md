# Coding-test

All the problems are solved using python

Problem #1 (GROUP BY OWNERS)
         Python Dictionary is used to store the data in the format {key:value}={file-type:owner-name}
         copying all the keys(file-type) in one list
         copying all the values(owner names) in another list
         Iterating through 'for' loop entire for each key(file-type) values are matched, 
            if we have same value(owner-name) for multiple keys(file-type)
              then each value(owner), all the keys are grouped by using 'append' function
              
...................................................................................................................................
Problem #2  (PALINDROME)
          First a input string is taken
          Then is it made case insensitive by converting entire string into lower case through 'casefold()' function
          Then the string is reversed and stored in a variable
          Then casefolded string and reversed string are compared character by character.
          If all the characters are matched
             then it is displayed as 'palindrome string'
          else
             displayed as 'Non-palindrome string'
             
..................................................................................................................................
Problem #3 (PARSING OF FILE)
          This problem is solved using file handling functions
          Along with main.py file, I added 3 more files for the program 'log file','error file' and 'warning file'
          Three files were opened using 'open()' function with read mode for 'log file' and write mode for 'error file' and 'warning file'
          Using 'find' and 'write' functions --> each ERROR message is copied to 'error file'
                                             --> each WARNING message is copied to 'warning file'
                                             
.....................................................................................................................................
Problem #4 (Changing directory function)
           This problem is solved using classes and object concept.
           Class contains directory storing attribute and method called 'cd'(changing directory).
           Object is created and current directory is initialized and printed.
           Then user is given option whether they want to change directory.
           If they select 'yes' --> user can enter different path, this new path is appended to current directory.
           
.....................................................................................................................................
Problem #5 (STUDENT RECORDS)
          This Prolem is also solved using classes and object
          The class 'student' contains following attributes -->name,roll no,age and gender
                                                 methods --> insert(),display(),search(),delete(),update()
          User is given an option to choose their operation.
          This selection goes infinite times unless otherwise user chooses to come out.
          According to the selected option --> relevant method is called and respective methods are executed
         
........................................................................................................................................
ALL THE PROGRAMS LINKS , OUTPUTS ARE SAVED IN THE PDF FILE AND SHARED IN THE REPOSITORY. KINDLY REFER THE PDF FILE FOR MORE DETAILS
        
