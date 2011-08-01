#Modify this file so that it fits your system

#first we set our ZT0; This is when you want the day to start
startHour = 8
startMinute = 30

firstMonitor = 1 #what number is your first monitor?
lastMonitor = 6 #what number is your last monitor

monNumber = range(firstMonitor, lastMonitor+1) #do not change this unless your monitors are not consecutive ( ex [1,3,7,9,23] )
#monNumber = [1,3,5,7,15,19] # if your monitors ARE not consecutive uncomment this line instead
#monNumber = [3] # or use something like this if you have only one monitor

remove_original_lines = False # if true will remove the lines from the original files! Use with extreme caution!
#I don't recommend using this function. Use the script "remove monthly" that you will find on the pysolo website instead

correctErrors = True # Used to add bins if some are lost

#email options
send_email = False
SMTPmailserver = 'your smpt server' #you need to specify your own SMTP server here.
email_rcpts = ['you@example.com'] # list of email recipients. Separate using comma
attach_zipfile = False # the zip file can be attached to the email (might be used for backup purposes)

#output options
use_monFile = True #use TriKinetics monitor format. Default and reccomended
use_chanFile = False #use TriKinetics channel format

inputPath = '/data/sleep/monitors/' # on windows use 'C:/path/to/files'
outputDAMPath = '/data/sleep/data/' # on windows use 'C:/path/to/files'
zippedDataPath = '/data/sleep/zips/' # the directory where the zipped files are stored
