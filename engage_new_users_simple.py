from instapy import InstaPy
from instapy.util import smart_run
import random

session = InstaPy(username="tathagata.m",
password="Tatha1922!", 
#headless_browser=True,
geckodriver_path="D:\Coding\webdriver\geckodriver.exe")

with smart_run(session):
    # general settings
    session.set_quota_supervisor(enabled=True, sleep_after=['server_calls_h'],
                                 sleepyhead=True, stochastic_flow=True,
                                 notify_me=True,
                                 peak_likes_hourly=60, peak_likes_daily=600,
                                 peak_follows_hourly=60,
                                 peak_unfollows_hourly=60, peak_unfollows_daily=600,
                                 peak_server_calls_hourly=600)
    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=-1.3,
                                    delimit_by_numbers=True,
                                    max_followers=1000000,
                                    min_followers=0,
                                    max_following=15000,
                                    min_following=75)
    session.set_do_comment(True, percentage=50)
    session.set_comments(['aMEIzing!', 'Nice!',
			'Just incredible :open_mouth:',
			'What camera did you use @{}?',
			'Love your posts @{}',
			'Looks awesome @{}',
			'Getting inspired by you @{}',
			':raised_hands: Yes!',
			'Masterful shot 🔥🔥', 
            'Unbelievably great shot...👍:heart_eyes:👍', 
            'Nice pic..👍:heart_eyes:👍', 
            'Awesome capture...👍'])
    session.set_dont_like(
        ['dick', 'squirt', 'gay', 'homo', '#fit', '#fitfam', '#fittips',
         '#abs', '#kids', '#children', '#child',
         '[nazi',
         'jew', 'judaism', '[muslim', '[islam', 'bangladesh', '[hijab',
         '[niqab', '[farright', '[rightwing',
         '#conservative', 'death', 'racist'])
    #session.set_do_follow(enabled=True, percentage=25, times=2)

    # like by tags activity
    list = ['lightpainting', 'gardenlife', 'canon', '1dsmark2', 'gardening', 'garden', 
    'freezeframe', 'canonphotography', 'stopmotion', 'houseplants', 
    'toddlerlife', 'toddlersofinstagram', 'toddlerhairstyles', 'portrait', 'portraitphotography']
    session.set_dont_like(['promoter', 'nightclub'])
    #session.set_delimit_liking(enabled=True, max_likes=1005, min_likes=10)
    session.like_by_tags([list[random.randint(1, len(list)-1)]], amount=5000, skip_top_posts=False)