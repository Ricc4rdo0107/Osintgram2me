import instaloader
from instaloader import *

def high(target):
    instance = instaloader.Instaloader()

    instance.login(user="__pawn_chess__", passwd="pawner55")


    profile = Profile.from_username(instance.context, username=target)

    for highlight in instance.get_highlights(user=profile):
        # highlight is a Highlight object
        for item in highlight.get_items():
            # item is a StoryItem object
            instance.download_storyitem(item, '{}/{}'.format(highlight.owner_username, highlight.title))


if __name__ == "__main__":
    a = input("Download highlights of ==>  ")
    high(a)
        
