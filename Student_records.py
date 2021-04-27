class Student:
    # Constructor
    def __init__(self, name, rollno, age, gender):
        self.name = name
        self.rollno = rollno
        self.age = age
        self.gender = gender
         
    # Function to create and append new student   
    def insert(self, Name, Rollno, age, gender ):
        # use  ' int(input()) ' method to take input from user
        ob = Student(Name, Rollno, age, gender )
        ls.append(ob)
  
    # Function to display student details     
    def display(self, ob):
            print("Name   : ", ob.name)
            print("RollNo : ", ob.rollno)
            print("Age : ", ob.age)
            print("Gender : ", ob.gender)
            print("\n")    
         
    # Search Function    
    def search(self, rn):
        for i in range(ls.__len__()):
            if(ls[i].rollno == rn):
                return i       
  
    # Delete Function                                  
    def delete(self, rn):
        i = obj.search(rn)  
        del ls[i]
  
    # Update Function   
    def update(self, rn, name):
        i = obj.search(rn)
        ls[i].name = name
	   
         
# Create a list to add Students
ls =[]
# an object of Student class
obj = Student('', 0, 0, '')
  
print("\n Select the option for student management system \n")
print("1. Insert student\n")
print("2. Display student\n")
print("3. Search student\n")
print("4. Delete student\n")
print("5. Update student\n")
print("6. Exit\n")

x=1

while x==1: 

 ch = int(input("Enter choice:"))
 if(ch == 1):
  name = input('Enter the name of the student to be inserted: ')
  roll = input('Enter the Roll number: ')
  age = input('Enter the Age: ')
  gender = input('Enter the gender M/F: ')
  obj.insert(name, roll, age, gender)
         
 elif(ch == 2):
  print("\n")
  print("\nList of Students\n")
  for i in range(ls.__len__()):    
    obj.display(ls[i])
             
 elif(ch == 3):
  roll = input('Enter the roll number of the student to be searched: ')
  s = obj.search(roll)
  if(s != None):
    print("\n Student Found, ")
    obj.display(ls[s])
  else:
    print("\n Student NOT Found, ")
         
 elif(ch == 4):
  roll = input('Enter the roll number of the student to be removed: ')
  obj.delete(roll)
  print(ls.__len__())
  print("List after deletion")
  for i in range(ls.__len__()):    
    obj.display(ls[i])
             
 elif(ch == 5):
  roll = input('Enter the roll number of the student to be updated: ')
  name = input('Enter the New name of the student: ')
  obj.update(roll, name)
  print(ls.__len__())
  print("List after updation")
  for i in range(ls.__len__()):    
    obj.display(ls[i])
             
 elif(ch == 6):
  x=2
	
 else:
  print("End")