#!/usr/bin/env python3
"""
Author Kieran W 20200118

Build a README file using fragments from the following subdirectories

core
lang
extras
"""
# Imports
import argparse
import re
import os

# Constants
DIR_C = "core/"
DIR_L = "lang/"
DIR_E = "extras/"

FILE_EXT = ".md"
FILE_OUT = "output" + FILE_EXT
FRAG_DIV = "\n\n"


def fileToString(filepath):
	"""Return the contents of a file as a string using a (relative) filepath

	Args:
		filepath (string): The file path

	Returns:
		string: The contents of the file
	"""
	string = ""
	with open(filepath, "r") as file:
		data = file.read()
		for line in data:
			string += line
	return string + FRAG_DIV


def stringToFile(filepath, string):
	"""Write a string to a file defined with a (relative) path

	Args:
		filepath (string): The file path
		string (string): The string to write to the file
	"""
	file = open(filepath, "w")
	file.write(string)
	file.close()


"""
Command line arguments
"""
parser = argparse.ArgumentParser(
	description="""Build a README file using fragments from the following
	subdirectories
	""")
parser.add_argument(
	"-o",
	"--output",
	action="store",
  	 help="""Enter the filename to output to with or without ".md". Leave blank for default
""")
parser.add_argument(
	"-v",
	"--verbose",
	action="store_true",
  	 help="""Print debug to the terminal
""")


# Define some variables
args = parser.parse_args()
debug = args.verbose
buildString = ""

if (debug):
	print(args)

"""
Do building
"""
buildString += fileToString(DIR_C + "info.md")
if (debug):
	print("added info")
buildString += fileToString(DIR_C + "proj-name.md")
if (debug):
	print("added name")


"""
Set the Language
"""
options = []

for subdir, dirs, files in os.walk("lang"):
	for fileName in files:
		options += [subdir + os.sep + fileName]

print("-1/[enter]: [none]")
for index, option in enumerate(options):
	print(str(index) + ":", option)

choiceString = input(
	"Select the number that corresponds to an option above (between, and including, 0 and " +
	str(
		len(options) -
		1) +
 		 ")\n>")
if len(choiceString) > 0:
	choice = int(choiceString)
	if choice >= 0 and choice < len(options):
		buildString += fileToString(options[choice])
		if (debug):
			print("added language: " + options[choice])


buildString += fileToString(DIR_C + "proj-changelog.md")
if (debug):
	print("added changelog")
buildString += fileToString(DIR_C + "proj-down.md")
if (debug):
	print("added download")
buildString += fileToString(DIR_C + "proj-lice.md")
if (debug):
	print("added license")

"""
Extras (can select multiple - order s-mobile, s-desktop, theme, browser-s)
"""
options = os.listdir("extras")
print("-1/[enter]: [none]")
for index, option in enumerate(options):
	print(str(index) + ":", option)

choiceString = input(
	"Select the number that corresponds to an option above (between, and including, 0 and " +
	str(
		len(options) -
		1) +
 		 " and separate with \",\")\n>")
if len(choiceString) > 0:
	choices = choiceString.split(",")
	for choice in choices:
		choiceInt = int(choice)
		if choiceInt >= 0 and choiceInt < len(options):
			buildString += fileToString(DIR_E + options[choiceInt])
			if (debug):
				print("added extra: " + options[choiceInt])


"""
Get slugs to mangle
"""
print("Fill in the slugs:")
for tag in set(re.findall("{{(.*?)}}", buildString)):
	tagReplace = input(tag + ":")
	buildString = buildString.replace("{{" + tag + "}}", tagReplace)


"""
Output the file
"""
if args.output is not None:
	outFileName = args.output
else:
	outFileName = FILE_OUT
stringToFile(outFileName, buildString)
if (debug):
	print("written file")
