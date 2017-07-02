from spydetail import spy, Spy, ChatMessage, friends
from steganography.steganography import Steganography
from datetime import datetime
from function import add_status,start_chat,add_friend
from function import send_message,read_message,read_chat_history
STATUS_MESSAGES = ['My name is Bond, James Bond', 'Shaken, not stirred.', 'Keeping the British end up, Sir']
print "Hello! Let\'s get started"
question = "Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N)? "
existing = raw_input(question)
if existing == "Y":
    start_chat(spy)
else:
    spy.name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")
    if len(spy.name) > 0:
        spy.salutation = raw_input("Should I call you Mr. or Ms.?: ")

        spy.age = raw_input("What is your age?")
        spy.age = int(spy.age)

        spy.rating = raw_input("What is your spy rating?")
        spy.rating = float(spy.rating)
        start_chat(spy)
    else:
        print 'Please add a valid spy name'

