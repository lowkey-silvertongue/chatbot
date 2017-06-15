"""Module providing data write and read procedures."""
"""Author: Felix Hilscher"""
"""Version: 0.15062017"""

import debug

#   increments index file
def indexIncr():
    """Returns current index number from index file\nas an integer and increments index by one (1)."""
    current_index = -1
    new_index = -1
    with open("persons/index.ix", "r") as index_file:
        try:
            current_index = int(index_file.readline())
        except Exception as index_exception:
            debug.debugLog("dataIO.py", "indexIncr", repr(index_exception))
        else:
            return current_index
    new_index = current_index + 1
    with open("persons/index.ix", "w") as index_file:
        try:
            index_file.write(str(new_index))
        except Exception as index_exception:
            debug.debugLog("dataIO.py", "indexIncr", repr(index_exception))
        else:
            return current_index
    debug.debugLog("dataIO.py", "indexIncr", "Incremented index by one.")
    return current_index

#   reads index file
def indexRead():
    """Returns current index number from index file as an integer."""
    current_index = -1
    with open("persons/index.ix", "r") as index_file:
        try:
            current_index = int(index_file.readline())
        except Exception as index_exception:
            debug.debugLog("dataIO.py"), "indexRead", repr(index_exception)
        else:
            return current_index
    return current_index

# TODO
#   READ FILE DATA; OUTPUT AS DICTONARY (key-value)
#   GET USERS BY NAME AND/OR INDEX NUMBER
#   CREATE USER BASED ON NAME AND INDEX NUMBER

        
#   function writing formatted data to a file
def writeToFile(file, **kwargs):
    """Accepts a target file name as string and any number of key-value arguments.\nFilename hast to end on '.txt'\nValue of k-v pairs has to be a string; e.g.: test="123"."""
    if file.find(".human") < 1:
        debug.debugLog("dataIO.py", "writeToFile", "File was no .human or name was to short.")
        return False
    with open(("persons/" + file), "w") as data:
        for t,v in kwargs.items():
            data.write(t + "=" + v + "\n")
    debug.debugLog("dataIO.py", "writeToFile", ("Successfully wrote data to file persons/" + file + "."))
    return True
