__author__ = 'mrkaiser'
import re


def parser(event_body):
    True


def strip_raw_event(event_body):
    regex = r'.+;.+[\.!?]'
    reversed = event_body[::-1]
    rereverse = re.findall(regex, reversed)[0]
    return rereverse[::-1]
