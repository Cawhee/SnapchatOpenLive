import os
import time
from snapchat import Snapchat

PATH = './snaps/'

def download(s, snap):
    """Download a specific snap, given output from s.get_snaps()."""

    id = snap['id']
    result = s.get_media(id)

    if not result:
        return False

    filename = id + '.jpg'
    path = PATH + filename
    with open(path, 'wb') as fout:
        fout.write(result)
    return True

def download_snaps(s):
    """Download all snaps that haven't already been downloaded."""


    snaps = s.get_snaps()
    for snap in snaps:
        id = snap['id']

        result = download(s, snap)

        if not result:
            break
        else:
            print 'Downloaded:', id
            story_id = s.upload(Snapchat.MEDIA_IMAGE, 'snaps/' + id + '.jpg')
            time.sleep(2)
            s.add_story(story_id, time=3)

while True: 
    if __name__ == '__main__':
        s = Snapchat()
        s.login('USERNAME', 'PASSWORD')
        """Make sure you change the USERNAME and PASSWORD to the credentials of your bot"""
        download_snaps(s)
        s.clear_feed()
        time.sleep(25)

