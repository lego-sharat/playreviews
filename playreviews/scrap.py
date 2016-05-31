import sys
from playreviews import *

if __name__ == '__main__':
    if len(sys.argv) > 1:
        app_id = sys.argv[1]
        plr = PlayReviews()
        plr.fetch_and_write_reviews(app_id)
