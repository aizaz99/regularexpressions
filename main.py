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

#TODO :Copy resuts to the clipboard



