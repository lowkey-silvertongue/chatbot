"""Module containing debug log function used in all modules."""
"""Author: Felix Hilscher"""
"""Version: 0.15062017"""

from datetime import datetime

def debugLog(module_name, function_debug, desc_debug):
    """Writes debug information to debug.log.\nAccepts strings: module name, function name and a description."""
    with open("logs/debug.log", "a") as debuglog:
        debuglog.write(datetime.now().strftime("%H-%M-%S") + " - " + module_name + " " + function_debug + " called:   " + desc_debug + "\n")
    return
