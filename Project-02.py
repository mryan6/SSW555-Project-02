""" Michael Ryan
    Project-02
    SSW-555
    The goal of this assignment is to write a parser that can parse through GEDCOM files line by line and separate each line into its level, tag and arguments
    The script should also tell whether the tag is valid or not (valid tags are in project description)

    The problem: GEDCOM files have line format of <level> <tag> <argument>
    We want to get familiar with extracting this information from the line so that we can easily separate it

    Exceptions:
    for INDI and FAM tags, the format is <level> <id> <tag>
    certain tags are only valid at certain levels

    Steps:
    1. Open File
    2. Read File Line by Line
    3. Print Line
    4. Separate line into information
    5. Check to make sure information is correct
        *Check to see if tag is a supported tag or not
        *Make sure all tags are on a valid level
    6. Print Separated Line

    Assignment wording:
    Reads each line of a GEDCOM file

    Prints "--> <input line>"

    Prints "<-- <level>|<tag>|<valid?> : Y or N|<arguments>"
    <level> is the level of the input line, e.g. 0, 1, 2
    <tag> is the tag associated with the line, e.g. 'INDI', 'FAM', 'DATE', ...
    <valid?> has the value 'Y' if the tag is one of the supported tags or 'N' otherwise.  The set of all valid tags for our project is specified in the Project Overview document.
    <arguments> is the rest of the line beyond the level and tag.
"""

fileName = 'proj02test.ged'

try:
    chosenFile = open(fileName)
    #We do not want the script to run if the file is empty, so we will check for this case first
    #If the file is not empty, we will use seek(0) to return to the beginning of the file
    #Then go through the file and read each character, each time a character is used, we will increase its value in the dict
    checkFirstLine = chosenFile.read(1)
    if not checkFirstLine :
        print("This file is empty, try running this script on a file that is not empty!")
        exit()
    else :
        chosenFile.seek(0)
        for line in chosenFile :
            #line = line.rstrip()
            print('--> ' + line)
            #now we must

#FileNotFoundError will only occur if the file is not found within the working directory
except FileNotFoundError :
    print("File Not Found in this directory, ensure that you have entered the file name and extension (.ged etc.) correctly, and ensure that the file is in the correct working directory.")
#TypeError will occur if there is some difficulty in converting/printing values, meaning not all values are of the expected type
except TypeError :
    print("A type error has occurred. The file may be corrupt.")
#ValueError will occur when there is a value that does not make sense/causes a system error within the script
except ValueError :
    print("File contains a bad value. Make sure your file has not been corrupted.")
