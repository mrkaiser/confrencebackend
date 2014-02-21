__author__ = 'mrkaiser'

from parser import event_factory


def test_event_factory_one():
    input = 'See an episode and have your questions answered by the National Geographic Channel\'s ' \
            'resident engineering geniuses. D. Taylor, R. Jones, C. Taylor; Fri 11:30 am; Crystal Ballroom [Hil]'

    assert event_factory(input) == True