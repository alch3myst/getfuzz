from sys import platform


class bcolors:  # Fency colors
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''


# Most important function
def printBanner():
    if platform != 'win32':
        print(bcolors.OKBLUE+'''
            _____ ______ _______'''+bcolors.WARNING + ''' ______ _    _ ____________'''+bcolors.OKBLUE+'''
            / ____|  ____|__   __'''+bcolors.WARNING+'''|  ____| |  | |___  /___  /'''+bcolors.OKBLUE+'''
            | |  __| |__     | |  '''+bcolors.WARNING + '''| |__  | |  | |  / /   / /'''+bcolors.OKBLUE+'''
            | | |_ |  __|    | |  '''+bcolors.WARNING + '''|  __| | |  | | / /   / /'''+bcolors.OKBLUE+'''
            | |__| | |____   | |  '''+bcolors.WARNING+'''| |    | |__| |/ /__ / /__'''+bcolors.OKBLUE+'''
            \_____|______|  |_|  '''+bcolors.WARNING + '''\_|     \____//_____/_____|'''+'''
                                            Python series
            
            A http brute force...
                                This can go really fast
            '''+bcolors.ENDC)
    else:
        print('''
         _____ ______ _______ ______ _    _ ____________
        / ____|  ____|__   __|  ____| |  | |___  /___  /
        | |  __| |__    | |  | |__  | |  | |  / /   / /
        | | |_ |  __|   | |  |  __| | |  | | / /   / /
        | |__| | |____  | |  | |    | |__| |/ /__ / /__
        \_____ |______| |_|  \_|     \____//_____/_____|
                                           Python series
        
        A http brute force...
                                 This can go really fast
        ''')

# print Help


def printhelp():
    if platform != 'win32':
        print(bcolors.OKBLUE+'''
        ##############     Commands    ################
        |                                             |
        | -u --url        Target site url             |
        | -w --wordlist   Wordlist location           |
        | -l --limit      Http requests per second    |
        |                 Default 10, Max Infinite    |
        |                 (Or server response 429 :l) |
        | -L --limit-ph   Limit per host (play with)  |
        |                 Default 0 (0 = unlimited)   |
        | -H              Change request to HTTP      |
        | -f              Default 404, request code   |
        |                 will be hidde from output   |
        |                                             |
        ###############################################
        Example
        getfuzz.py -u doogle.com -w /common.txt -l 50
        '''+bcolors.ENDC)
    else:
        print('''
        ##############     Commands    ################
        |                                             |
        | -u --url        Target site url             |
        | -w --wordlist   Wordlist location           |
        | -l --limit      Http requests per second    |
        |                 Default 10, Max Infinite    |
        |                 (Or server response 429 :l) |
        | -L --limit-ph   Limit per host (play with)  |
        |                 Default 0 (0 = unlimited)   |
        | -H              Change request to HTTP      |
        | -f              Default 404, request code   |
        |                 will be hidde from output   |
        |                                             |
        ###############################################
        Example
        getfuzz.py -u doogle.com -w /common.txt -l 50
        ''')
