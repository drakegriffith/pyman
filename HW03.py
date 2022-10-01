
from cgitb import text
import requests, re
from pprint import pprint
from bs4 import BeautifulSoup

## NOTES:

# CS 2316 - Fall 2022 - HW03 Regex, APIs, BeautifulSoup
# HW03: This homework is due by Friday, September 30th @ 11:59PM.

# You are required to complete the missing bodies of the functions below.
# Further instructions are provided in the comments ...
# A few tips:
#   - Make sure you return the right value and datatype
#   - Test your code for each function by uncommenting the respective test cases
#     in the if __name__ == '__main__' block
#   - Do not import modules within functions
#   - Do not leave any print statements within your functions
#   - Submit in Gradescope as HW03.py  - Your submission should be named exactly HW03.py
#   - Print your variables as you code in order to see what values they have
#     especially for questions with API and BeautifulSoup


def mathmatic(target):
    pattern = "(?<=\{)(.*?)(?=\})"
    li = re.findall(pattern, target)
    stringLi = ''
    for item in li: 
        stringLi += item
    return stringLi
    """
    Question 1

    You are doing fun math problems. Given a string of combination of '{}', '[]',
    '()', you are required to return the substring included by the outermost '{}'.
    You need to write your code in one line.

    Args:
        target (str): the string to search in
    Returns:
        str

    >>> mathmatic('{[[[[]()]]]}')
    '[[[[]()]]]'

    >>> mathmatic('[(){([{}])}]')
    '([{}])'

    """
    pass


def group_chat(text_message, friend):
    return re.findall('(?<=' + friend + ':.).*', text_message, flags=re.MULTILINE)
          
    """
    Question 2

    - Your friends are blowing up your group chat. Given a string of text messages
    from your friends and a specific friend's name, return the first text message
    they sent, excluding their name.

    - Each text message ends with either a ?, !, or .

    - Your code must be written in one line.

    Args:
        text_message (astr)
        friend (astr)
    Returns:
        str of first match

    >>> text_message = "Madison: How are you guys going today?" + \
    "Anna: I'm doing pretty well!" + \
    "Madison: That's good to hear. How is everyone else?"

    >>> friend = "Madison"

    >>>group_chat(text_message, friend)
    How are you guys going today?

    """

    pass



#### Questions 3 and 4 use the Deezer API: https://developers.deezer.com/api
#### If you make a free account, you will gain access to the API's documentation


def track_list(album):
    trackList = []
    url = 'https://api.deezer.com/album/{}/tracks'.format(album)
    response = requests.get(url)
    data = response.json()
    print(data)
    for i in range(len(data['data'])):
        if data['data'][i]['duration'] < 300:
            titleData = data['data'][i]['title']
            trackList.append(titleData)
    return trackList
    """
    Question 3

    - Given an album number, go through each track in the album and return a list
    of the tracks whose duration is less than 300 seconds.

    - Use the website provided below:

    https://api.deezer.com/album/{album}/tracks

    Args:
        album (int)
    Returns:
        list

    >>> track_list(302127)
    ['Aerodynamic', 'Harder, Better, Faster, Stronger', 'Crescendolls', 'Nightvision', 'Superheroes', 'High Life', 'Something About Us', 'Voyager', 'Short Circuit', 'Face to Face']

    >>> track_list(302130)
    ['Wake Up', 'Love Her For That', 'Brink Of Love', 'So Easy', 'All I See', 'All We Said', 'A Step Behind', 'Missing Children', 'Thanks A Lot']

    """

    pass



def top_songs(artist):
    albumDict = {}
    url = 'https://api.deezer.com/artist/{}/albums'.format(artist)
    responseArtist = requests.get(url)
    artistData = responseArtist.json()
    for i in range(len(artistData['data'])):
        responseTopTracks = requests.get(artistData['data'][i]['tracklist'])
        trackData = responseTopTracks.json()
        trackDict = {}
        topThree = []
        for j in range(len(trackData['data'])):
            trackDict[trackData['data'][j]['title']] = trackData['data'][j]['rank']
  
        topThree = [name for name, rank in sorted(trackDict.items(), key = lambda x: x[1], reverse=True)[:3]]
    
        albumDict[artistData['data'][i]['title']] = topThree
    return albumDict

            



    
   

    """
    Question 4
    - Given an artist code, go through the albums by the artist and create a
    dictionary mapping each of them to their three top_ranked tracks (highest three ranks).

    - Please do not include EPs nor singles, only albums. This last condition can be
    checked by looking at the record_type attribute.

    - You will need to use requests.get() more than once.
    - The first request should be to the following endpoint:

    https://api.deezer.com/artist/{artist_code}/albums

    Args:
        artist (int)
    Returns:
        dict

    >>> top_songs(892) # Coldplay!
    {'A Head Full of Dreams':
        ['Hymn for the Weekend','Everglow','A Head Full of Dreams'],
    'A Rush of Blood to the Head':
        ['The Scientist', 'Clocks', 'In My Place'],
     ...
    'Viva La Vida or Death and All His Friends':
        ['Viva La Vida', 'Violet Hill','Strawberry Swing'],
    'X&Y':
        ['Fix You', 'Speed of Sound', 'Talk']}
    >>> len(top_songs(892))
    15

    >>> top_songs(1352097) # Bastille!
    {'All This Bad Blood':
        ['Things We Lost In The Fire', 'Of The Night', 'Pompeii'],
    'Bad Blood':
        ['Laughter Lines (Bonus Track)', 'Pompeii', 'Oblivion'],
    'Doom Days':
        ['Joy', 'Doom Days', 'Those Nights'],
    ...
    'Wild World (Complete Edition)':
        ['Good Grief', 'Send Them Off!', 'Blame']}

    >>> len(top_songs(1352097))
    11


    """
    pass

def get_data(url):
    stateDict = {}
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    divTag = soup.find_all("tbody")
    for tag in divTag:
        trTag = soup.find_all("tr")
        for tag2 in trTag:
            print(tag2[0])
        #for tag in tdTag:
            #print(tag.text)
        #listItem = [tag[1].text, tag[2].text, tag[3].text]
        #stateDict[tag[0].text] = listItem
    return stateDict
            


    #tableData = [(fatality, fatTotal, annualAmount) for fatality, fatTotal, annualAmount in table]
    #print(tableData)
    

    """
    Question 5

    Given a website url (url), search through the corresponding HTML file, find the main table,
    and return a dictionary that maps each state to a list that contains

    - the 2018 Fatalities,
    - the 10-Year Fatality Total,
    - the Annual Economic Cost Due to Motor Vehicle Crashes

    listed in the row for that state.

    Keep in mind, there may be empty columns. Make sure to be testing your code
    in order to locate these.

    Input:
        str     url --> 'https://www.transportation.gov/research-and-technology/state-state-crash-data-and-economic-cost-index'
    Returns:
        dict    {str: list}

    For the provided url, we return:

    {'Alabama': ['953', '8,977', '$4.47 billion'],
     'Alaska':  ['80', '683', '$592 million'],
        ...
        etc
        ...
     'Wyoming': ['111', '1,275', '$788 million']}

     The length should be 51 (no need to skip DC).
     Also, no need to modify the Utah row.

    """

    pass


def companies(website):
    """
    Question 6
    - Acces the table at the provided website:
     'https://en.wikipedia.org/wiki/Companies_listed_on_the_New_York_Stock_Exchange_(C)'

    - Parse through it and retrieve the names of all companies in the site that
        ~ Are based in the US
        ~ Have an acronym anywhere in their name
        ~ (Let us define 'acronym' as any two or more consecutive capital letters)

    Args:
        string (website)
    Returns:
        list   (list of company names)

    >>> web1 = 'https://en.wikipedia.org/wiki/Companies_listed_on_the_New_York_Stock_Exchange_(C)'
    >>> web2 = 'https://en.wikipedia.org/wiki/Companies_listed_on_the_New_York_Stock_Exchange_(T)'
    >>> companies(web1)
    ['CACI',
     'CAI International, Inc.',
     'CARBO Ceramics Inc.',
      ...
     'CYS Investments, Inc.']
    >>> len(companies(web1))
    27
    >>> len(companies(web2))
    23


    """
    pass

def transportation():
    """
    Question 7

    - Access the table at the provided website:
    https://www.transportation.gov/research-and-technology/state-state-crash-data-and-economic-cost-index

    - Return a dictionary with each state that contains consecutive double letters
    mapped to its yearly economic cost due to motor vehicle crashes

    - Only include the state if the name contains consecutive double letters.
    For example, Connecticut has two consecutive n's, so it will be included.
    Remember, consecutive letters can also be at the end of the name.

    - HINT: You should investigate back references to match groups
    - https://www.regular-expressions.info/backref.html


    Args:
        none
    Return:
        dict

    >>> transportation()

    {'Connecticut': '$4.880 billion',
     'Hawaii': '$577 million',
     'Illinois': '$10.885 billion',
     'Massachusetts': '$5.835 billion',
     'Minnesota': '$3.057 billion',
     'Mississippi': '$2.718 billion',
     'Missouri': '$5.560 billion',
     'Pennsylvania': '$5.851 billion',
     'Tennessee': '$5.6667 billion'}

    """
    pass

def trans_dict(adict):
    """
    Question 8

    --- Make Sure to Test Your Question 5 Before Starting This Question ---

    Given the dictionary you implemented in Question 5, construct a new dictionary that
    has the key equals to each state and the value as a dictionary that contains
    the following key-value pairs:
    1.  The ratio of the 2018 Fatalities to the 10-Year Fatality Total, keep 2 floating
        points.
    2.  The boolean value that indicate whether the Annual Economic Cost Due to
        Motor Vehicle Crashes is high or low. For a cost to be high, it needs to
        be larger than 4 billion.
    3.  Consider using regex rather than list comprehension in this question.

    Returns:
        Dictionary {str: list}

    For the provided dictinary, we return:
    {'Alabama': {'High Cost': True, 'Ratio': 0.11},
    'Alaska': {'High Cost': False, 'Ratio': 0.12},
        ...
        etc
        ...
     'Wyoming': {'High Cost': False, 'Ratio': 0.09}}

     """
    pass




def episodes(show_code, first_year, last_year):
    """
    Question 9
    - For this question, you will use the IMDB website to find the best episodes for
    a given show. The website you will use is the following:

    https://www.imdb.com/title/{show_code}/episodes?year={year}

    - Notice that in order to access the desired page where the episodes are listed,
    you must input the code for the show as well as the year that interests you. We
    want to consider the entire show, so we  are interested in all years between first_year
    and last_year (both inclusive).

    - You will need to iterate through range(first_year, last_year+1)

    - As you go through the list of episodes for each year, keep a record of which episodes
        * Have a rating of at least 8.0 and
        * Have a number of reviews of at least 2000.

    - Then return a set with the names of all those episodes

    Args:
        str (show_code)
        int (first_year)
        int (last year)

    Returns:
        set

    >>> episodes('tt0411008', 2004, 2010)
        {'...In Translation',
         '316',
         '?',
         ...
         'Whatever Happened, Happened',
         'White Rabbit'}
    >>> len(episodes('tt0411008', 2004, 2010))
        107

    >>> episodes('tt1196946', 2008, 2015)
        {'Blinking Red Light',
         'Blue Bird',
         'Fire and Brimstone',
         'Pilot',
         'Strawberries and Cream: Part 2',
         'The Desert Rose',
         'White Orchids'}

    """
    pass



if __name__ == "__main__":

    pass

    # # Q1
    #print(mathmatic('{[[[[]()]]]}'))
    #print(mathmatic('[(){([{}])}]'))

    # # Q2
    text_message = "Madison: How are you guys going today?" + \
                     "Anna: I'm doing pretty well!" + \
                     "Madison: That's good to hear. How is everyone else?"
    friend1 = "Madison"

    #print(group_chat(text_message, friend1))


    # # Q3
    #print(track_list(302127))
    #print(track_list(302130))



    # # Q4
    #pprint(top_songs(892))          # Coldplay albums
    #pprint(top_songs(1352097))      # Bastille albums


    # # Q5
    url = 'https://www.transportation.gov/research-and-technology/state-state-crash-data-and-economic-cost-index'
    pprint(get_data(url))


    # # Q6
    # web1 = 'https://en.wikipedia.org/wiki/Companies_listed_on_the_New_York_Stock_Exchange_(C)'
    # web2 = 'https://en.wikipedia.org/wiki/Companies_listed_on_the_New_York_Stock_Exchange_(T)'
    # pprint(companies(web1))
    # pprint(companies(web2))


    # # Q7
    # pprint(transportation())

    # # Q8
    # url = 'https://www.transportation.gov/research-and-technology/state-state-crash-data-and-economic-cost-index'
    # adict = get_data(url)
    # pprint(trans_dict(adict))


    # # Q9
    # pprint(episodes('tt0411008', 2004, 2010))
    # pprint(episodes('tt1196946', 2008, 2015))
    # pprint(episodes('tt0108778', 1994, 2004))





