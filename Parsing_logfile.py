logfile = open('log_file.log','r')
errorfile = open('Error_file.log','w')
warningfile = open('warning_file.log','w')

line = logfile.readlines()
type(line)
for i in range(0,len(line)):
   if(line[i].find('ERROR')!=-1):
      errorfile.write(line[i])
   elif (line[i].find('WARNING')!=-1):
      warningfile.write(line[i])
   else:
      pass
errorfile.close()
warningfile.close()

result = line