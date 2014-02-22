__author__ = 'mrkaiser'

from event_parser import parser


def test_event_factory_one():
    text = 'See an episode and have your questions answered by the National Geographic Channel\'s ' \
           'resident engineering geniuses. D. Taylor, R. Jones, C. Taylor; Fri 11:30 am; Crystal Ballroom [Hil]'

    assert parser(text) == True