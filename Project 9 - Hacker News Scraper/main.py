"""
This module implements the Hacker News scraper exercise of the Section 18 of the course.
"""

import pprint
import requests

from bs4 import BeautifulSoup


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hacker_news = []

    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hacker_news.append({'title': title, 'link': href, 'votes': points})

    # Return news array sorted
    return sort_stories_by_votes(hacker_news)


def start_scraping():
    res = requests.get('https://news.ycombinator.com/news')
    res2 = requests.get('https://news.ycombinator.com/news?p=2')
    soup = BeautifulSoup(res.text, 'html.parser')
    soup2 = BeautifulSoup(res2.text, 'html.parser')

    links = soup.select('.storylink')
    subtext = soup.select('.subtext')
    links2 = soup2.select('.storylink')
    subtext2 = soup2.select('.subtext')

    mega_links = links + links2
    mega_subtext = subtext + subtext2

    # Call the create custom Hacker New function
    pprint.pprint(create_custom_hn(mega_links, mega_subtext))


# Entry point of the script
if __name__ == '__main__':
    # Call the start scraping function
    start_scraping()
