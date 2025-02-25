import platform

# UNIX STANDARD PATH DELIMITER
OS_PATH_DELIM = '/'

if platform.system().lower().startswith("windows"):
    # WINDOWS PATHS ARE THE OPPOSITE
    OS_PATH_DELIM = '\\'

