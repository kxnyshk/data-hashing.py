# FUNCTION IMPORTS
from Functions.writer import writerText

# READ PASSWORD
def readPassword():
    PATH = './Static/pass.txt'
    MODE = 'r'

    f = open(PATH, MODE)
    return f.read()

# FETCH PASSWORD
def fetchPassword():
    writerText(readPassword())
    password = input()
    return password
