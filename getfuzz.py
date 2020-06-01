#!/usr/bin/env python

import aiohttp
import asyncio
import sys
import getopt
import util.gui as gui
import util.helpers as helper
import warnings

warnings.filterwarnings('ignore')

# Variable Initialization
url = ''
_status = 404
HEADERS = {}
wordlist = ''
mode = 'https://'
_limit = 10
_limit_per_host = 0


# Main function for fuzzing
async def fuzz(param):
    try:
        async with session.get(formatedUrl.replace('*F*', param), headers=HEADERS) as res:
            # pageHtml = await res.text()
            if res.status == 429:
                print('Too fast for this server, u got a 429 Too Many Requests  ')
                sys.exit(1)

            if res.status != _status:
                print('Found ' + str(res.status) + ' - ' + formatedUrl.replace('*F*', param) + ' - 🤔 - ')
                      
            sys.stdout.write('Trying: ' + formatedUrl.replace('*F*', param) + '\r')
            sys.stdout.flush()
    except aiohttp.ClientConnectionError as e:
        pass
    except Exception as e:
        print(e)
        return


# Args definition
try:
    # Define options u, w, h
    options, remainder = getopt.gnu_getopt(
        sys.argv[1:],  # terminal arguments
        'u:w:l:L:f:hH',  # Shotr options
        [  # Long arguments
            'url=',
            'wordlist=',
            'limit=',
            'limit-ph=',
            'filter=',
            'help='
        ])
# Catch errors from malformed input
except getopt.GetoptError as err:
    print('Nope: ', err)
    sys.exit(1)

# set the variables with arguments values
for opt, arg in options:
    # Difine URL
    if opt in ('-u', '--url'):
        url = arg

    # Define wordlist path
    elif opt in ('-w', '--wordlist'):
        wordlist = helper.loadWordlist(arg)

    # Request limit
    elif opt in ('-l', '--limit'):
        _limit = int(arg)

    # Request limit per host
    elif opt in ('-L', '--limit-per-host'):
        _limit_per_host = int(arg)

    # Filter requests
    elif opt in ('-f', '--filter'):
        _status = int(arg)

    # Return the help text
    elif opt in ('-h', '--help'):
        gui.printBanner()
        gui.printhelp()
        sys.exit(2)

    # Change the request from httpsto http
    elif opt == '-H':
        mode = 'http://'

# Check if url or wordlist is empty
if url or wordlist != '':
    # Print the banner
    gui.printBanner()

    # Print the wordlist size
    print('To check/wordlist size: ' + str(len(wordlist)) + '\n')

    # Create the loop event
    loop = asyncio.get_event_loop()

    # Connector and limits
    tcp = aiohttp.TCPConnector(
        limit=_limit, limit_per_host=_limit_per_host, loop=loop)
    session = aiohttp.ClientSession(connector=tcp)

    try:
        # Format the url to https://site.com or http://site.com based on -H
        formatedUrl = helper.formatUrl(url, mode) 

        # Run the loop until wordlist finish
        loop.run_until_complete(
            asyncio.gather(*(fuzz(param) for param in wordlist))
        )

        # Close open connections and exit
        print('\nClosing Connections...')
        loop.run_until_complete(asyncio.sleep(0.250))
        tcp.close()

    except KeyboardInterrupt:
        print('Cancela cancela \n')
        sys.exit(2)
# Return the error message
else:
    gui.printBanner()
    gui.printhelp()
