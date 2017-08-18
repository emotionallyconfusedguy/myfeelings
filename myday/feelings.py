import sys
import numpy
from numpy import random

if sys.version_info <= (3, 0):
    sys.stdout.write("Sorry, this program requires Python 3.x, not Python 2.x\n")
    sys.exit(1)

feelings = ['exhausted', 'confused', 'ecstatic', 'guilty', 'suspicious',
            'angry', 'hysterical', 'frustrated', 'sad', 'confident',
            'embarassed', 'happy', 'mischievous', 'disgusted', 'frightened',
            'enraged', 'ashamed', 'cautious', 'smug', 'depressed',
            'overwhelmed', 'hopeful', 'lonely', 'lovestruck', 'jealous',
            'bored', 'surprised', 'anxious', 'shocked', 'shy']

sthg = numpy.random.choice(feelings)

print("Hello",sthg,"day")
