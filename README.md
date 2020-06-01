         _____ ______ _______ ______ _    _ ____________
        / ____|  ____|__   __|  ____| |  | |___  /___  /
        | |  __| |__    | |  | |__  | |  | |  / /   / /
        | | |_ |  __|   | |  |  __| | |  | | / /   / /
        | |__| | |____  | |  | |    | |__| |/ /__ / /__
        \_____ |______| |_|  \_|     \____//_____/_____|

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
