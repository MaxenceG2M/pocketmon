"""
Remove all time tags to each article on Pocket.
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


def remove_tag(id, title, tag):
    """ Remove a tag on an article. """

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

if __name__ == '__main__':
    api = pocket.Pocket(consumer_key=consumer_key, access_token=access_token)

    try:
        datas,_ = api.get(sort='newest', state='unread',
                        detailType='complete')
    except AttributeError:
        datas = {}

    for _,v in datas.get('list',{}).items():
        f = list(filter(lambda t: 'minute' in t or 'hour' in t, v.get('tags',[])))
        if len(f) > 0 :
            remove_tag(v.get('item_id','no_id'), v.get('given_title','no_title'), ",".join(f))
            print(f)


        #print(i['word_count'])

        # item.word_count = int(item.word_count)
        # item.is_article = int(item.is_article)
        #
        # if item.word_count:
        #     add_tag(item, reading_time(item.word_count // words_per_minute))
        #
        # elif not item.is_article:
        #     add_tag(item, 'not an article')
