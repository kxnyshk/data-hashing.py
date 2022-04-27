# LIB IMPORTS
import sys

# FUNCTION IMPORTS
from Functions.hash import hashData
from Functions.writer import writerText
from Functions.writer import writerHash

# READ SHA3-256
def readSHA3_256():
    PATH = './Static/sha3-256.txt'
    MODE = 'r'

    f = open(PATH, MODE)
    return f.read()

# FETCH HASH
def fetchHash():
    data = hashData()
    writerText(readSHA3_256())
    writerHash(data)

# TERMINATE
def terminate():
    PATH = './Static/terminate.txt'
    MODE = 'r'

    f = open(PATH, MODE)
    var = input(f.read())

    if(var == '-1'):
        sys.exit()
    else:
        if(var == '0'):
            fetchHash()
        terminate()

# RUN
def run():
    PATH_USER = './Static/user.txt'
    PATH_WELCOME = './Static/welcome.txt'
    MODE = 'r'

    f_user = open(PATH_USER, MODE)
    f_welcome = open(PATH_WELCOME, MODE)
    
    writerText(f_user.read())
    user = input()
    
    writerText(f'{f_welcome.read()}{user}!\n')
    fetchHash()
