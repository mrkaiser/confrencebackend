__author__ = 'mrkaiser'

from event_parser import parser, strip_raw_event


def test_event_factory_one():
    text = 'See an episode and have your questions answered by the National Geographic Channel\'s ' \
           'resident engineering geniuses. D. Taylor, R. Jones, C. Taylor; Fri 11:30 am; Crystal Ballroom [Hil]'

    assert parser(text) == True


def test_strip_one():
    text = 'The actors from some of your favorite cartoons give you insight on the people behind the voices!' \
            ' B. West, K. Najimy, R. Horvitz, R. Simons, R. Paulsen, B. Carter; Sat 2:30 pm; Cent. II–III [HYT]'

    assert strip_raw_event(text) == '! B. West, K. Najimy, R. Horvitz, R. Simons, R. Paulsen, B. Carter; ' \
                                    'Sat 2:30 pm; Cent. II–III [HYT]'


def test_strip_two():
    text = 'A look at Frylock, Shake and Meatwad! Sat 4:00 pm; Dunwoody [HYT]'

    assert strip_raw_event(text) == '! Sat 4:00 pm; Dunwoody [HYT]'


def test_strip_three():
    text = 'Fan group [adult swim] Central does a live panel and podcast about the black sheep of the Turner family.' \
           ' Fri 5:30 pm; Dunwoody [HYT]'

    assert strip_raw_event(text) == '. Fri 5:30 pm; Dunwoody [HYT]'
