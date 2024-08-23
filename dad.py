import pyfiglet
import requests
from random import choice
from termcolor import colored

header = 'Dad Joke Generator'
header_fmtd = pyfiglet.figlet_format(header)
colored_header = colored(header_fmtd, color='magenta')
print(colored_header)

topic = input('Let me tell you a joke! Give me a topic:')
response_json = requests.get(
		"https://icanhazdadjoke.com/search", 
		headers={"Accept": "application/json"},
		params={"term": topic}
	).json()
joke = response_json["results"]
count = len(joke)
if count == 0:
	print(f"Sorry, I don't have any jokes about {topic}! Please try again.")
elif count == 1:
	print(f"I've got {count} joke about {topic}! Here it is:")
	print(joke[0]['joke'])
else:
	print((f"I've got {count} jokes about {topic}! Here is one:"))
	print(choice(joke)['joke'])