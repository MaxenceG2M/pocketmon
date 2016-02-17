"""
Add reading time tags to each article on Pocket.
"""

import logging

import pocket

from config import (
    consumer_key,
    access_token,
    words_per_minute,
    logging_level,
    logging_handler,
)

logger = logging.getLogger(__name__)
logger.setLevel(logging_level)
logger.addHandler(logging_handler)


def add_tag(id, title, tag):
    """ Add a tag on an article. """

    logger.debug('Tag "%s" on %s -- %s' % (tag, id, title))

    api.send("""
    [
        {
            "action"  : "tags_add",
            "item_id" : "%s",
            "tags"    : "%s"
        }
    ]
    """ % (id, tag))

def remove_tag(id, title, tag):
    """ Add a tag on an article. """

    logger.debug('Remove tag "%s" on %s -- %s' % (tag, id, title))

    api.send("""
    [
        {
            "action"  : "tags_remove",
            "item_id" : "%s",
            "tags"    : "%s"
        }
    ]
    """ % (id, tag))


def reading_time(minutes):
    """ Convert minutes to a nice string representing the time. """
    rounded = int(5 * round(float(minutes)/5)) or 2

    if 0 < rounded < 50:
        return '%d minutes' % rounded
    elif 50 <= rounded < 75:
        return '1 hour'
    elif 75 <= rounded < 105:
        return '1.5 hours'
    else:
        return '2+ hours'


if __name__ == '__main__':
    api = pocket.Pocket(consumer_key=consumer_key, access_token=access_token)

    try:
        datas,_ = api.get(sort='newest', state='unread',
                        detailType='complete')
    except AttributeError:
        datas = {}

    for _,v in datas.get('list',{}).items():
        given_title = v.get('given_title', 'no_title')
        item_id = v.get('item_id', 'no_id')
        is_article = int(v.get('is_article', '0'))

        f = list(filter(lambda t: 'minute' in t or 'hour' in t, v.get('tags',[])))

        if len(f) > 1:
            remove_tag(item_id, given_title, ",".join(f))
        elif f:
            continue

        wc = int(v.get('word_count','0'))

        logger.debug('Article %s -- %s have %s word count' % (item_id, given_title, wc))
        if wc:
            add_tag(item_id, given_title, reading_time(wc / words_per_minute))