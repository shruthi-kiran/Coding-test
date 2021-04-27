class Path:
    def _init_(self, path):
        self.current_path = path

    def cd(self, new_path):
        i=0;
        path1=new_path.split('/')
        Length=len(path1)
        path2=self.current_path.split('/')
        if path1[0]=='':
            del path2[:]
            path2.append('/'+path1[1])
            i=i+2
        while(i<Length):
            j=len(path2)-1
            if path1[i]=='..':
                path2.pop(j)
            else:
                path2.append(path1[i])
            i=i+1
        self.current_path="/".join(path2)

        pass

path=Path()
path.current_path='/home/shruthi/programs'
print('The current directory of the file - ',path.current_path)

choice =input('Do you want to change directory (Y/N) ? ')
if choice == 'Y':
  path.new_path=input('enter the new path : ')
  print('The changed directory of the file - ',path.new_path)
elif choice == 'N':
  print('You are continuing to work in the directory path :  ',path.current_path)
else:
  print('Enter valid choice (Y/N)')