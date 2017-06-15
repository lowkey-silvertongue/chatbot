"""Module containing routines for file setup and program initiation."""
"""Author: Felix Hilscher"""
"""Version: 0.15062017"""

from pathlib import Path
from datetime import datetime
import debug


#
# CRITICAL VARIABLE DECLARATIONS
#

log_current_datetime = ""

#
# CRITICAL FUNCTION DEFINITIONS
#


#   writes log data regarding setup
def _setupLog(logdate, function, desc):
    """Writes to current setup log. See 'debug.py' for information on arguments."""
    with open((logdate + ".log"), "a") as setup_log:
        setup_log.write(datetime.now().strftime("%H-%M-%S") + " - initiate.py - " + function + " called:   " + desc + "\n")
    return

#   check if directory exists
def _dirExists(target):
    """Looks at a specific path; Returns 'True' if it exists."""
    ret = True
    try:
        directory = Path(target)
    except Exception as exception_dir:
        _setupLog(log_current_datetime, "_dirExists", repr(exception_dir))
    if not directory.is_dir():
        ret = False
    return ret

#   check if file exists
def _fileExists(target):
    """Looks at a specific file; Returns 'True' if it exists."""
    ret = True
    try:
        file = Path(target)
    except Exception as exception_file:
        _setupLog(log_current_datetime, "_fileExists", repr(exception_file))
    if not file.is_file():
        ret = False
    return ret

#
#
# SETUP MAIN FUNCTION
#
#

# TODO
#   ADD CONSISTENCY CHECKS FOR
#       -CONFIG.CFG
#       -USER/INDEX PAIRING
#   ADD REBUILD USER/INDEX PAIRING FUNCTION

def botSetup():
    """Function validating presence of core files, filestructures and directories.\nReturns 'True' if successful, False if not."""
    bot_file_setup = False
    print("CHATBOT TECHNICAL SETUP INITIATED")
    log_current_datetime = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    _setupLog(log_current_datetime, "botSetup", "Logfile created, setup initiated.")
    if not _fileExists(log_current_datetime + ".log"):
        return bot_file_setup
    if not _dirExists("logs"):
        Path("logs").mkdir()
        if not _dirExists("logs"):
            return bot_file_setup
        _setupLog(log_current_datetime, "botSetup", "Log directory not found, 'logs/' created.")
    else:
        _setupLog(log_current_datetime, "botSetup", "Log directory found.")
    if not _fileExists("config.cfg"):
        with open("config.cfg", "w") as config_file:
            config_file.write("CHATBOT CONFIG FILE - DO NOT CHANGE MANUALLY")
        if not _fileExists("config.cfg"):
            return bot_file_setup
        _setupLog(log_current_datetime, "botSetup", "No configuration file found, config.cfg created.")
    else:
        _setupLog(log_current_datetime, "botSetup", "Configuration file found.")
    if not _dirExists("persons"):
        Path("persons").mkdir()
        if not _dirExists("persons"):
            return bot_file_setup
        _setupLog(log_current_datetime, "botSetup", "Data directory not found, 'person/' created.")
    else:
        _setupLog(log_current_datetime, "botSetup", "Data directory found.")
    if not _fileExists("persons/index.ix"):
        with open("persons/index.ix", "w") as index_setup:
            index_setup.write("0")
        if not _fileExists("persons/index.ix"):
            return bot_file_setup
        _setupLog(log_current_datetime, "botSetup", "No index file found, 'persons/index.ix' created.")
    else:
        _setupLog(log_current_datetime, "botSetup", "Index file found.")
    bot_file_setup = True
    with open("logs/debug.log", "a") as debug_setup:
        debug_setup.write("--- START OF DEBUG LOG SESSION " + log_current_datetime + " ---\n" )
    debug.debugLog("initiate.py", "botSetup", "Technical setup completed; New debug session started.")
    print("TECHNICAL SETUP COMPLETE")
    return bot_file_setup






