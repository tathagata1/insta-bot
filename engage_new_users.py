import random
from instapy import InstaPy
from instapy import smart_run

# get a session!
session = InstaPy(username="tathagata.m",
password="Tatha1922!", 
#headless_browser=True,
geckodriver_path="D:\Coding\webdriver\geckodriver.exe")

# let's go! :>
with smart_run(session):
    # general settings
    session.set_quota_supervisor(enabled=True, sleep_after=['server_calls_h'],
                                 sleepyhead=True, stochastic_flow=True,
                                 notify_me=True,
                                 peak_likes_hourly=57, peak_likes_daily=585,
                                 peak_follows_hourly=48,
                                 peak_unfollows_hourly=35, peak_unfollows_daily=402,
                                 peak_server_calls_hourly=500)
    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=-1.3,
                                    delimit_by_numbers=True,
                                    max_followers=10000,
                                    max_following=15000,
                                    min_followers=75,
                                    min_following=75)
    session.set_do_comment(False, percentage=10)
    session.set_comments(['aMEIzing!', 'So much fun!!', 'Nicey!',
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
    session.set_do_follow(enabled=True, percentage=25, times=2)

    # like by tags activity
    list = ['lightpainting', 'gardenlife', 'canon', '1dsmark2', 'gardening', 'garden', 
    'freezeframe', 'canonphotography', 'stopmotion', 'houseplants', 
    'toddlerlife', 'toddlersofinstagram', 'toddlerhairstyles', 'portrait', 'portraitphotography']
    session.set_dont_like(['promoter', 'nightclub'])
    #session.set_delimit_liking(enabled=True, max_likes=1005, min_likes=10)
    session.like_by_tags([list[random.randint(1, len(list)-1)]], amount=50, skip_top_posts=False)

    # interact user followers activity
    session.set_user_interact(amount=5, randomize=True, percentage=50,
                              media='Photo')
    session.set_do_follow(enabled=True, percentage=70)
    session.set_do_like(enabled=True, percentage=70)
    session.set_comments([u"👍" , 'Nice shot! @{}',
	    'I love your profile! @{}',
	    'Your feed is an inspiration :thumbsup:',
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
    session.set_do_comment(enabled=True, percentage=30)
    session.interact_user_followers([''], amount=random.randint(1, 10),
                                    randomize=True)

    # unfollow activity
    session.set_dont_unfollow_active_users(enabled=True, posts=3)
    session.unfollow_users(amount=10,
                           InstapyFollowed=(True, 'all'), style='FIFO',
                           unfollow_after=90 * 60 * 60, sleep_delay=501)

    ''' Joining Engagement Pods...
    '''
    session.join_pods(topic='photography')