__author__ = 'mrkaiser'

from bs4 import BeautifulSoup
from urllib import request
from migrate import Track
import itertools


dragon_base = 'http://dragoncon.org/'
tracks_append = ['?q=fan-tracks-view', '?q=fan-tracks-view&page=1']


def strip_html_tags(html_text):
    if html_text is None:
        return None
    else:
        return ''.join(BeautifulSoup(html_text).findAll(text=True))


def get_tracks():
    '''
    This method will scrape the dragoncon website for all the individual fan tracks for the weekend and return them as the list.
    get_tracks is a helper method on iterating through the list of pages and scraping each page for the tracks
    '''
    tracks_ = list(map(lambda append: scrape_tracklist_soup(get_the_soup(dragon_base + append)), tracks_append))
    return list(itertools.chain.from_iterable(tracks_))


def scrape_tracklist_soup(d_soup):
    '''
    This scrapes a given track page for all the individual tracks and their necessary information.
    '''
    #parse the list for the urls
    urls = list(
        map(lambda div: div.find('a').attrs['href'], d_soup.find('table').find_all('div', class_='views-field-title')))
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
    desc_string_list = []
    if hr is None:
        #do something
        print('hr has non siblings')
        desc_string_list = list(
            map(lambda x: strip_html_tags(str(x)).strip(), list(track_soup.find('div', class_='field-item even').find_all('p')[1::2])[::2]))
    else:
        #get the desc
        desc_string_list = list(map(lambda x: strip_html_tags(str(x)).strip(), list(hr.next_siblings)[::2]))
        desc = "\n".join(desc_string_list)

    director = track_soup.find('div', class_='field-item even').find_all('p')[0].contents[-1].strip()

    desc = "\n".join(desc_string_list)
    print(str(url) + ',' + str(director) + ',' + str(desc))
    return (url, director, desc)


def get_and_insert_tracks():
    tracks = get_tracks()
    track_info = list(map(lambda track: scrape_track(dragon_base + track[2]), tracks))
    return tracks, track_info


