import sys
import os
import debug
import u_toolkit as u_tools

class User:

    def __init__(self, name, index=None):
        self.u_name = str(name)
        if index is None:
            self.u_data = {"Vorname":name}
            self.u_topics = u_tools.genTopicDict()
            self.u_discuss = dict()
            index_number = u_tools.createUserFiles(name, self.u_data)
            self.u_file = index_number + "_" + name
            # SAVE TARGET FILE TO 'user_file' AND
            # 'user_conv' AS STRING WITH FORMAT 'index_name' AND 'index_name_CONV'
        elif not isinstance(index, int):
            raise ValueError("Tried to build 'User' object with a non integer index. Index can only be 'None' or integer.")
        else:
            
            # LOAD ALL USERDATA FROM A FILE

    def rebuildTopics():
        # REBUILD TOPICS DICT FROM FILE
        pass

    def saveUser():
        # SAVE USER DATA TO 'user_file'
        pass

    def pickTopic(topic=None):
        picked_topics = dict()
        if topic is None:
            # COMPRISE DICT OF A RANDOM TOPIC
            picked_topics = dict()
        elif not isinstance(topic, str):
            raise ValueError("Tried to call pickTopic() with a non string argument. Argument can only be 'None' or string.")
        else:
            # COMPRISE DICT OF CHOSEN TOPIC
            picked_topics = dict()
        # RETURN A DICT COMPRISED OF ENTRIES FROM 'u_topics' WITH THE SAME TOPIC TYPE
        # WITH THE STRUCTURE 'type=topic'
        return picked_topics


    

