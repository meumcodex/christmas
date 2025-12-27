import pyfiglet
from termcolor import colored
from colorama import init
import random
init()
colors = ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]
art=pyfiglet.figlet_format("¡Happy New Year 2026!")
colored_art=colored(art,random.choice(colors))
print(colored_art)
print(colored("🎆¡Have a joyful holiday!    🎉🍾🥂",random.choice(colors),))