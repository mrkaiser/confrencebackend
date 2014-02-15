
__author__ = 'mrkaiser'

from bs4 import BeautifulSoup
from urllib import request
from ormdefs import Track
import itertools

dragon_base = 'http://dragoncon.org/'
tracks_append = ['?q=fan-tracks-view', '?q=fan-tracks-view&page=1']


def get_tracks():
    '''
    This method will scrape the dragoncon website for all the individual fan tracks for the weekend and return them as the list.
    get_tracks is a helper method on iterating through the list of pages and scraping each page for the tracks
    '''
    tracks_ = list(map(lambda append: scrape_tracklist_soup(get_the_soup(dragon_base+append)), tracks_append))
    return list(itertools.chain.from_iterable(tracks_))


def scrape_tracklist_soup(d_soup):
    '''
    This scrapes a given track page for all the individual tracks and their necessary information.
    '''
    #parse the list for the urls
    urls = list(map(lambda div: div.find('a').attrs['href'], d_soup.find('table').find_all('div', class_='views-field-title')))
    taglines = list(map(lambda x: x.text.strip(), d_soup.find('table').find_all('div', class_='field-content')[1::2]))
    titles = list(map(lambda x: x.text.strip(), d_soup.find('table').find_all('div', class_='views-field-title')))
    return list(zip(titles, taglines, urls))


def get_the_soup(url):
    '''
    Will return a soup object for a given URL
    '''
    response = request.urlopen(url)
    track_doc = response.read()
    d_soup = BeautifulSoup(track_doc)
    return d_soup


def scrape_track(url):
    '''
    Scrapes a SPECIFIC track page for the director and description.

    '''
    print(url)
    track_soup = get_the_soup(url)
    hr = track_soup.find('div', class_='field-item even').hr
    desc = ''
    if(hr is None):
        #get the desc
    else:
        #get the desc
        desc_string_list = list(map(lambda x: x.text, list(hr.next_siblings)[::2]))
        desc = "\n".join(desc_string_list)
    good_stuff = track_soup.find('div', class_='field-item even').find_all('p')
    director = track_soup.find('div', class_='field-item even').find_all('p')[0].contents[1].strip()

    hr = track_soup.find('div', class_='field-item even').hr
    #every call text on every even element and return it as a list
    desc_string_list = list(map(lambda x: x.text, list(hr.next_siblings)[::2]))
    desc = "\n".join(desc_string_list)
    return (good_stuff, url, director, hr, desc)


def get_and_insert_tracks():
    tracks = get_tracks()
    track_info = list(map(lambda track: scrape_track(dragon_base+track[2]), tracks))
    return tracks, track_info


