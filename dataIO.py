"""Module providing data write and read procedures."""
"""Author: Felix Hilscher"""
"""Version: 0.16062017"""

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
            return current_index
    new_index = current_index + 1
    with open("persons/index.ix", "w") as index_file:
        try:
            index_file.write(str(new_index))
        except Exception as index_exception:
            debug.debugLog("dataIO.py", "indexIncr", repr(index_exception))
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
            return current_index
    return current_index

#   generates a new index number based on index.ix and increments
def genIndexId():
    index_new_num = indexRead()
    index_new_prefix = ""
    if index_new_num > 0:
        for i in range(6 - len(str(index_new_num))):
            index_new_prefix = index_new_prefix + "0"
        index_new_prefix = index_new_prefix + str(index_new_num + 1)
    else:
        index_new_prefix = "000001"
    debug.debugLog("dataIO.py", "genIndexId", "Generated index prefix; incremented index by one.")
    indexIncr()
    return index_new_prefix

#   generates a string with an index number based on integer argument
def indexString(target_index):
    target_index_num = str(target_index)
    target_index_prefix = ""
    for i in range(6 - len(target_index_num)):
        target_index_prefix = target_index_prefix + "0"
    target_index_prefix = target_index_prefix + target_index_num
    return target_index_prefix

# TODO
#   GET USERS BY NAME AND/OR INDEX NUMBER

#   create new user file
def createUser(new_user):
    user_index_part_new = genIndexId()
    try:
        with open("persons/" + user_index_part_new + new_user + ".human", "w") as new_u_file:
            new_u_file.write("")
        debug.debugLog("dataIO.py", "createUser", "New user file" + new_user + "created")
    except Exception as usercreate_exception:
        debug.debugLog("dataIO.py", "createUser", "Problem with creating user " + new_user + ".human .")
        debug.debugLog("dataIO.py", "createUser", repr(usercreate_exception))
        return False
    return True

#   splits a single file line into one k, v pair and returns a dict with k and v
def valueSplitter(text_line):
    split_dict = {}
    kvpair_data = text_line.split("=")
    split_dict[kvpair_data[0]] = kvpair_data[1]
    return split_dict


#   returns a dictonary of k, v pairs of all entries in a file
def readUserFile(user_file):
    data_dict = {}
    with open("persons/" + user_file + ".human", "r") as data_file:
        data_line = data_file.readline()
        while data_line != "":
            data_dict.update(valueSplitter(data_line))
            data_line = data_file.readline()
    return data_dict

        
#   function writing formatted data to a file
def writeToFile(file, **kwargs):
    """Accepts a target file name as string and any number of key-value arguments.\nFilename hast to end on '.txt'\nValue of k-v pairs has to be a string; e.g.: test="123"."""
    try:
        with open(("persons/" + file + ".human"), "a") as data:
            for t,v in kwargs.items():
                data.write(t + "=" + v + "\n")
        debug.debugLog("dataIO.py", "writeToFile", ("Successfully wrote data to file persons/" + file + "."))
    except Exception as write_exception:
        debug.debugLog("dataIO.py", "writeToFile", "Problem with writing to file" + file + ".human .")
        debug.debugLog("dataIO.py", "writeToFile", repr(write_exception))
    else:
        return False
    return True
