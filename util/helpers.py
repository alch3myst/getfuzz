# Load wordlist from arg -w
def loadWordlist(location):
    # Wordlist load
    with open(location) as wordlists:
        wordlists = wordlists.readlines()
    wordlists = [x.strip() for x in wordlists]

    # Return a list with all lines splited asa arrai
    return wordlists


# Format url
def formatUrl(url, mode):
    if url[:4] != 'http':
        url = mode + url

    if mode not in url:
        url = mode + url[url.find('//')+2:]

    return url
