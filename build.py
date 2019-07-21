'''
Author Kieran W 2019-05-08

Build a README file using fragments from the following subdirectories

req
core
lang
support
screenshots
extras


'''

# Help Text

HELP_N = """Option to determine if core fragments are added to the output. Recommended to 
omit this.
"""
HELP_O = """Enter the filename to output to with or without '.md'. Leave blank for default
"""
HELP_L = """Enter the programming language to use in the form ide/language or language.
Use the latter for generalized readme.
Leave blank for none 
"""
HELP_S = """Enter the type of support to use. Leave blank for none 
"""
HELP_I = """Enter the type of screenshots to use
"""
HELP_E = """Enter any extras. Use -e for each extra
"""
HELP_V = """Print debug to the terminal
"""
HELP_P = """Specify parameters in the form -p param=value eg.
-p proj-name=''my fantastic project''
"""
HELP_C = """Use config.txt (under req)
"""
HELP_A = """
"""


# Imports
import argparse

# Constants
DIR_R = 'req/'
DIR_C = 'core/'
DIR_L = 'lang/'
DIR_S = 'support/'
DIR_I = 'screenshots/'
DIR_E = 'extras/'

FILE_EXT = '.md'

FILE_OUT = 'output' + FILE_EXT

FRAG_DIV = '\n\n'

'''
Return the contents of a file as a string using a (relative) filepath
'''
def fileToString(filepath):
    string = ''
    with open(filepath, 'r') as file:
        data = file.read()
        for line in data:
            string += line
    return string + FRAG_DIV


'''
Write a string to a file defined with a (relative) path
'''
def stringToFile(filepath, string):
    file = open(filepath, "w")
    file.write(string)
    file.close()
    return

'''
Add the file extension if required
'''
def fileExt(filename):
    fileNameLen = len(FILE_EXT)
    if filename[-fileNameLen:] != FILE_EXT:
        filename += FILE_EXT
    return filename


'''
Command line arguments
'''
# Program description
parser = argparse.ArgumentParser(description='Build a README file using fragments from the following subdirectories')
# Use of -n or --nocore sets nocore to True (excludes core components)
parser.add_argument("-n", "--nocore", help=HELP_N, action="store_true")
parser.add_argument("-o", "--output", help=HELP_O, action="store")
parser.add_argument("-l", "--lang", help=HELP_L, action="store")
parser.add_argument("-s", "--support", help=HELP_S, action="store")
parser.add_argument("-i", "--images", "--screenshots", help=HELP_I, action="store")
parser.add_argument("-e", "--extras", help=HELP_E, action="append")
parser.add_argument("-v", "--verbose", help=HELP_V, action="store_true")
parser.add_argument("-p", "--param", help=HELP_P, action="append")
parser.add_argument("-c", "--config", help=HELP_C, action="store_true")

parser.add_argument("-a", "--advanced-help", action="store_true")

# Define some variables
args = parser.parse_args()
debug = args.verbose
buildString = ''

if (debug):
    print(args)

if args.nocore:
    print("core fragments turned off")
if args.support:
    print("support text enabled")

# Advanced/ Python Help
if args.advanced_help:
    print(fileToString(DIR_R + "build-help.txt"))
    exit()


'''
Do building 
'''

# Add .md to extras if required
extras = []
if args.extras is not None:
    for index in range(len(args.extras)):
        extras.append(fileExt(args.extras[index]))
    if (debug):
        print(extras)

'''
Optional 'info' uncomment to include
'''
buildString += fileToString(DIR_R + fileExt("info"))
if (debug):
    print("added info")

'''
Badges
'''
if len(extras) > 0:
    if 'proj-badges.md' in extras:
        buildString += fileToString(DIR_E + fileExt("proj-badges"))
        if (debug):
            print("added badges")

'''
Core elements / Insert project icon?
'''
if not args.nocore:
    buildString += fileToString(DIR_C + fileExt("proj-name"))
    if (debug):
        print("added name")


if len(extras) > 0:
    if 'proj-icon.md' in extras:
        buildString += fileToString(DIR_E + fileExt("proj-icon"))
        if (debug):
            print("added project icon")

if not args.nocore:
    buildString += fileToString(DIR_C + fileExt("proj-desc"))
    buildString += fileToString(DIR_C + fileExt("proj-down"))
    if (debug):
        print("added description and download instruction")

if args.lang is not None:
    buildString += fileToString(DIR_L + fileExt(args.lang))
    if (debug):
        print("added language")

if not args.nocore:
    buildString += fileToString(DIR_C + fileExt("proj-lice"))
    if (debug):
        print("added license")


'''
Browser Support
'''
if len(extras) > 0:
    if 'proj-browser-support.md' in extras:
        buildString += fileToString(DIR_E + fileExt("proj-browser-support"))
        if (debug):
            print("added browser support")


'''
Screenshots / Themes
'''
if args.images is not None:
    buildString += fileToString(DIR_I + fileExt(args.images))
    if (debug):
        print("added screenshots")

if len(extras) > 0:
    if 'proj-theme.md' in extras:
        buildString += fileToString(DIR_E + fileExt("proj-theme"))
        if (debug):
            print("added theme")

'''
Support
'''
if args.support is not None:
    buildString += fileToString(DIR_S + fileExt(args.support))
    if (debug):
        print("added support")


'''
Replace elements of the output file with params (-p)
'''
if args.param is not None:
    for element in range(len(args.param)):
        param = args.param[element].split('=')
        if(debug):
            print("param: " , param)
        buildString = buildString.replace(":"+param[0]+":",param[1])

'''
Replace elements of the output file with config.txt (-c)
'''
if args.config:
    elements = fileToString(DIR_R + "config.txt").split('\n')
    for element in elements:
        param = element.split('=')
        if(debug):
            print("param: " , param)
        if len(param) == 2:
            buildString = buildString.replace(":"+param[0]+":",param[1])


'''
Output the file 
'''
if args.output is not None:
    outFileName = fileExt(args.output)
else:
    outFileName = FILE_OUT
stringToFile(outFileName, buildString)
if (debug):
    print("written file")

