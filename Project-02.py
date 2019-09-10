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
#So if we wanna use a dict, the tag must be the key. we cannot use args for keys because we dont know what args will be
#we cant use level for key because each level can have multiple tags
dict = {
        'NOTE':'0',
        'HEAD':'0',
        'TRLR':'0',
        'FAM':'0',
        'INDI':'0',
        'BIRT':'1',
        'DEAT':'1',
        'MARR':'1',
        'DIV':'1',
        'HUSB':'1',
        'WIFE':'1',
        'CHIL':'1',
        'NAME':'1',
        'SEX':'1',
        'FAMC':'1',
        'FAMS':'1',
        'DATE':'2'
    }

fileName = input("Please enter the filename, including file extension (eg. proj02test.ged): ")


chosenFile = open(fileName)
output = open('output.txt', 'w+')
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
        """
            for each key in the dict, check to see if the key is in the line.
                *still need the information array to help resolve collisions (since information is an array and not a string, the extra condition ensures that the entire tag is in the line)
                    **Without this, FAM and FAMC/FAMS behave weirdly because FAM is a string in FAMC/FAMS but FAM is not in an array containing FAMC/FAMS
            Once a match is found, check for validity by seeing if the value at the key matches the value from the line
                *have to do an extra check for the special cases (FAM and INDI)
                    **if these special cases don't have the tag as the last thing on the line, they are not valid
            We can use the information array to help us separate arguments from tags since we know all lines that don't have FAM or INDI will have the same format
        """

        line = line.rstrip()
        output.write('--> ' + line+'\n')
        information = line.split()
        level = information[0]
        keys = dict.keys()

        for key in keys :
            if key in line and dict[key] == level and key in information :
                if (key == 'INDI' or key == 'FAM') :
                    if line.endswith(key) :
                        valid = 'Y'
                        tag = key
                        args = information[1]
                        break

                    else :
                        valid = 'N'
                        tag = key
                        args = line.split(tag,1)[1].lstrip()
                        break

                valid = 'Y'
                tag = key
                args = line.split(tag,1)[1].lstrip()
                break

            else :
                valid = 'N'
                tag = information[1]
                args = ''
                for i in information[2:] :
                    args += i + ' '

        output.write('<-- '+level + '|'+tag+'|'+ valid +'|' + args + '\n')
