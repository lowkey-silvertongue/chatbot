"""Be gentle with her."""
"""Author: Felix Hilscher"""
"""Version: 0.15062017"""

#import initiate
from datetime import datetime
#import dataIO

#test_one = dataIO.indexIncr()

#print(test_one)


time_log_test = datetime.now().strftime("%d_%m_%Y_%H_%M")

print(time_log_test)

time_log_actual = datetime.now().strftime("%H-%M-%S")

print(time_log_actual)



