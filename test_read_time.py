from config import (
    words_per_minute
)

def reading_time(minutes):
    """ Convert minutes to a nice string representing the time. """

    # First, for 1 and 2 minutes range
    rounded = round(minutes)
    if rounded <= 1:
        return '1 minute'
    elif rounded <= 2:
        return '2 minutes'

    # Second, by interval of 5 minutes
    rounded = int(5 * round(float(minutes)/5)) or 1

    if 0 < rounded < 50:
        return '%d minutes' % rounded
    elif 50 <= rounded < 75:
        return '1 hour'
    elif 75 <= rounded < 105:
        return '1.5 hours'
    else:
        return '2+ hours'

if __name__ == '__main__':
    print(reading_time(100.1))
    print(reading_time(0.6))
    print(reading_time(1.1))
    print(reading_time(1.8))
    print(reading_time(2.5))
    print(reading_time(2.8))
    print(reading_time(3.6))
    print(reading_time(0.1))
