#Step 1 Create a regex for phone numbers
#Finds phone numbers and email addresses on clipboard

import pyperclip,re

phoneRegex =re.compile(r'''(
 (\d{3}|\(\d{3}\))?  #Area Code
  (\s|-|\.)? #Seperator
 (\d{3}) #First three digits
  (\s|-|\.)  #Seperator
 (\d{4}) #Last four digits
 (\s*(ext|x|ext.)\s*(\d{2,5}))?  #extension   
 
)''',re.VERBOSE

#TODO: Create Email Regix

emailRegex = re.compile(r'''(
  [a-zA-Z0-9._%+-]+ #Username
   @ #Symbol
  [a-zA-Z0-9.-]+ #Domain name
  (\.[a-zA-Z]{2,4}) #Dot somehing
  )''', re.VERBOSE)


#TODOL Find matches in clipboard text

text = str(pyperclip.paste())

matches =[]
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] !="":
      phoneNum += 'x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
  matches.append(groups[0])




#TODO :Copy resuts to the clipboard

if len(matches) >0:
  pyperclip.copy('\n'.join(matches))
  print('Cipied to clipboard:')
  print('\n'.join(matches))
else:
  print('No phone numbers or email addresses found')

  

