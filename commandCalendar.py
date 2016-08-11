'''
Terminal Calendar
'''
from time import sleep, strftime
NAME = "Joe"
calendar = {}
def welcome():
	print "Welcome to %s\'s calendar." % (NAME)
	sleep(1)
	print strftime("%A %B %d, %Y")
	print strftime("%I:%M:%S")
	sleep(1)
	print "What would you like to do?"

def start_calendar():
  welcome()
  start = True
  while start == True:
		user_choice = raw_input("A to Add\nU to Update\nV to View\nD to Delete\nX to Exit\nWhat would you like to do? ").upper()
		if user_choice == "V": # View Calendar Function
			if len(calendar.keys()) <= 0:
				print "There are no events."
			else:
				print calendar
		elif user_choice == "U": # Update Calendar Function
			date = raw_input("What date: ") # User enters date
			update = raw_input("What event: ") # User enters details
			calendar[date] =  update # creates event with detail
			print calendar # shows calendar
			print "Update successful"
		elif user_choice == "A": # Add to Calendar Function
			date = raw_input("Enter date (MM/DD/YYYY):") # User enters date
			if(len(date) > 10 or int(date[6:]) < int(strftime("%Y"))): # Check if date is valid and year is in the future
				print "Invalid date was entered"
				try_again = raw_input("Try again? Y for yes, N for no: ").upper()
				if try_again == "Y":
					continue
				else:
					start = False
			else:
				event = raw_input("What event: ")
				calendar[date] = event
		elif user_choice == "D": # Delete event Function
			if len(calendar.keys()) < 1:
				print "Calendar is already empty"
 			else:
				event = raw_input("What event: ")
				for date in calendar.keys():
					if event == calendar[date]:
						del calendar[date]
						print "Event has been deleted"
						print calendar
					else:
						print "Incorrect event was specified"
		elif user_choice == "X": # User exit program
			start = False
		else: # Invalid command, force exit
			print "Invalid command entered."
			start = False
start_calendar()