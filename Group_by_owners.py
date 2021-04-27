files={'input.txt':'shruthi','output.txt':'Manvith','code.txt':'Manvith'}

def group_by_owners(files):
  val = (list(files.values()))
  val = set(val)  
  val = list(val)
  print('Owners of the files : ',val)
  keyst = (list(files.keys()))
  print('Type of files : ',keyst)
  print('\n---Details on files owned by the owners---\n')
  empty = {} #empty dictionary
  for i in range(len(val)):
    for j in range(len(keyst)):
      if val[i]==list(files.values())[j]:
        dummylist = [keyst[j]]
        if val[i] in empty:
          empty[val[i]].append(keyst[j])
        else:
          empty[val[i]] = dummylist 
  return empty
print(group_by_owners(files))
