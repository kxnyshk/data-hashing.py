# LIB IMPORTS
import sys
from time import sleep

# TYPE.PY
def writerText(data):
    T = 0.07
    for x in data:
        sleep(T)
        sys.stdout.write(x)
        sys.stdout.flush()

def writerHash(data):
    T = 0.02
    for x in data:
        sleep(T)
        sys.stdout.write(x)
        sys.stdout.flush()
