from config import (
    words_per_minute
)

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
    print(reading_time(14 / words_per_minute))