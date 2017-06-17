def genTopicDict():
        # TREAD A DICT OF TOPICS FROM A FILE TO OUTPUT
        topic_gen = dict()
        return topic_gen

def loadUser():
        # LOAD USER DATA FROM FILE
        pass

def createUserFiles(user_name, user_data, discuss_data):
        index_current = -1
        index_prefix = ""
        with open("persons/index.ix", "r") as index_file:
                index_current = int(index_file.read())
                if not index_current > 0:
                        index_current = 1
        for i in range(6 - len(str(index_current))):
                index_prefix = index_prefix + "0"
        with open("persons/" + index_prefix + "_" + user_name + ".human", "w") as user_file:
                for k,v in user_data.items():
                        user_file.write(k + "=" + str(v))
        with open("persons/" + index_prefix + "_" + user_name, ".conv") as discuss_file:
                for k,v in discuss_data.items():
                        discuss_file.write(k + "=" + v)
        return index_prefix



