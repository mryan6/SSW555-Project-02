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

fileName = 'test.ged'


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
        line = line.rstrip()
        print('--> ' + line)
        """
        now we must go through and get the information we want, and split it up according to above conditions
        First thought: use split() to get each point of data and then check based on index?
        potential problems: Arguments are not neccesarily one word, would probably need to keep track of the index manually
            *Some lines just have less information but are perfectly correct. (eg. 0 HEAD)
                **Lets handle these first!
        if we keep track of it manually we can use a loop to make sure we always reach the end of the line.
        first item should always be <level>.
            *level = information[0]
        second item should be <id> OR <tag>
            *IF level = 0, check for id
                **how to check for id? id could be anything
                **could check for tags, we know what tags to be expecting, if none of them are in the second position, second position must be id
                **could also check to see if the third position is a tag INDI or FAM <-- lets do this one
            *IF level is not 0, this will be the tag
        """
        information = line.split()
        level = information[0]
        length = len(information)
        #print(length)
        #print (level)

        #SPLIT IT UP BY LEVELS FIRST
        if (level == '0') :
            if ((information[1] == 'NOTE') or (information[1] == 'HEAD') or (information[1] == 'TRLR')) :
                tag = information[1]
                args = ''
                for i in information[2:] :
                    args += i + ' '

                print('<-- '+level + '|'+tag+'|Y|'+args)

            elif ((information[2] == 'FAM') or (information[2] == 'INDI')) :
                args = information[1]
                tag = information[2]
                print('<-- '+level + '|'+tag+'|Y|'+args)

            else :
                tag = information[1]
                args = ''
                for i in information[2:] :
                    args += i + ' '

                print('<-- '+level + '|'+tag+'|N|'+args)

        elif (level == '1') :
            if (information[1] == 'BIRT' or information[1] == 'DEAT' or information[1] == 'MARR' or information[1] == 'DIV') :
                tag = information [1]
                args = ''
                print('<-- '+level + '|'+tag+'|Y|'+args)

            elif (information[1] == 'HUSB' or information[1] == 'WIFE' or information[1] == 'CHIL'
             or information[1] == 'NAME' or information[1] == 'SEX' or information[1] == 'FAMC' or information[1] == 'FAMS') :
                tag = information[1]
                args = ''
                for i in information[2:] :
                    args += i + ' '

                print('<-- '+level + '|'+tag+'|Y|'+args)

            else :
                tag = information[1]
                args = ''
                for i in information[2:] :
                    args += i + ' '

                print('<-- '+level + '|'+tag+'|N|'+args)

        elif (level == '2') :
            if (information[1] == 'DATE') :
                tag = information[1]
                args = ''
                for i in information[2:] :
                    args += i + ' '

                print('<-- '+level + '|'+tag+'|Y|'+args)

            else :
                tag = information[1]
                args = ''
                for i in information[2:] :
                    args += i + ' '

                print('<-- '+level + '|'+tag+'|N|'+args)

        else :
            tag = information[1]
            args = ''
            for i in information[2:] :
                args += i + ' '

            print('<-- '+level + '|'+tag+'|N|'+args)
