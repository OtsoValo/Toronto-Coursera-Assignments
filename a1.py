# Code written for Python 3

def seconds_difference(time_1, time_2):
    """ (number, number) -> number

    Return the number of seconds later that a time in seconds
    time_2 is than a time in seconds time_1.
        
    >>> seconds_difference(1800.0, 3600.0)
    1800.0
    >>> seconds_difference(3600.0, 1800.0)
    -1800.0
    >>> seconds_difference(1800.0, 2160.0)
    360.0
    >>> seconds_difference(1800.0, 1800.0)
    0.0
    """

    return time_2 - time_1


# print(seconds_difference(1800.0, 3600.0))
# print(seconds_difference(3600.0, 1800.0))
# print(seconds_difference(1800.0, 2160.0))
# print(seconds_difference(1800.0, 1800.0))


def hours_difference(time_1, time_2):
    """ (number, number) -> float

    Return the number of hours later that a time in seconds
    time_2 is than a time in seconds time_1.
        
    >>> hours_difference(1800.0, 3600.0)
    0.5
    >>> hours_difference(3600.0, 1800.0)
    -0.5
    >>> hours_difference(1800.0, 2160.0)
    0.1
    >>> hours_difference(1800.0, 1800.0)
    0.0
    """

    return (time_2 - time_1) / 3600


# print(hours_difference(1800.0, 3600.0))
# print(hours_difference(3600.0, 1800.0))
# print(hours_difference(1800.0, 2160.0))
# print(hours_difference(1800.0, 1800.0))


def to_float_hours(hours, minutes, seconds):
    """ (int, int, int) -> float

    Return the total number of hours in the specified number
    of hours, minutes, and seconds.

    Precondition: 0 <= minutes < 60  and  0 <= seconds < 60

    >>> to_float_hours(0, 15, 0)
    0.25
    >>> to_float_hours(2, 45, 9)
    2.7525
    >>> to_float_hours(1, 0, 36)
    1.01
    """

    return hours + (minutes / 60) + (seconds / 3600)


# print(to_float_hours(0, 15, 0))
# print(to_float_hours(2, 45, 9))
# print(to_float_hours(1, 0, 36))


def to_24_hour_clock(hours):
    """ (number) -> number

    hours is a number of hours since midnight. Return the hour as seen on a
    24-hour clock.

    Precondition: hours >= 0

    >>> to_24_hour_clock(24)
    0
    >>> to_24_hour_clock(48)
    0
    >>> to_24_hour_clock(25)
    1
    >>> to_24_hour_clock(4)
    4
    >>> to_24_hour_clock(28.5)
    4.5
    """

    return hours % 24


# print(to_24_hour_clock(24))
# print(to_24_hour_clock(48))
# print(to_24_hour_clock(25))
# print(to_24_hour_clock(4))
# print(to_24_hour_clock(28.5))


def get_hours(seconds):
    """ (int) -> int

    seconds is a number of seconds since midnight. Return the number of hours
    that have elapsed since midnight, as seen on a 24-hour clock. The return
    value should be in the range 0 to 23, inclusive.

    Precondition: seconds >= 0

    >>> get_hours(3599)
    0
    >>> get_hours(3600)
    1
    >>> get_hours(7999)
    1
    >>> get_hours(8000)
    2
    >>> get_hours(86399)
    23
    >>> get_hours(86400)
    0
    """

    return (seconds // 3600) % 24


# print(get_hours(3599))
# print(get_hours(3600))
# print(get_hours(3800))
# print(get_hours(8000))
# print(get_hours(86399))
# print(get_hours(86400))


def get_minutes(seconds):
    """ (int) -> int

    seconds is a number of seconds since midnight. Return the number of
    minutes that have elapsed since midnight, as seen on a 24-hour clock.
    The return value should be in the range 0 to 59, inclusive.

    Precondition: seconds >= 0

    >>> get_minutes(59)
    0
    >>> get_minutes(60)
    1
    >>> get_minutes(119)
    1
    >>> get_minutes(120)
    2
    >>> get_minutes(3599)
    59
    >>> get_minutes(3600)
    0
    """

    return (seconds // 60) % 60


# print(get_minutes(59))
# print(get_minutes(60))
# print(get_minutes(119))
# print(get_minutes(120))
# print(get_minutes(3599))
# print(get_minutes(3600))


def get_seconds(seconds):
    """ (int) -> int

    seconds is a number of seconds since midnight. Return the number of
    seconds that have elapsed since midnight, as seen on a 24-hour clock.
    The return value should be in the range 0 to 59, inclusive.

    >>> get_seconds(59)
    59
    >>> get_seconds(60)
    0
    >>> get_seconds(74)
    14
    >>> get_seconds(120)
    0
    >>> get_seconds(121)
    1
    >>> get_seconds(3800)
    20
    """

    return seconds % 60


# print(get_seconds(59))
# print(get_seconds(60))
# print(get_seconds(74))
# print(get_seconds(120))
# print(get_seconds(121))
# print(get_seconds(3800))


def time_to_utc(utc_offset, time):
    """ (number, float) -> float

    Return time at UTC+0, where utc_offset is the number of hours away from
    UTC+0.

    >>> time_to_utc(+0, 12.0)
    12.0
    >>> time_to_utc(+1, 12.0)
    11.0
    >>> time_to_utc(-1, 12.0)
    13.0
    >>> time_to_utc(-11, 18.0)
    5.0
    >>> time_to_utc(-1, 0.0)
    1.0
    >>> time_to_utc(-1, 23.0)
    0.0
    """

    return to_24_hour_clock(time - utc_offset)


# print(time_to_utc(+0, 12.0))
# print(time_to_utc(+1, 12.0))
# print(time_to_utc(-1, 12.0))
# print(time_to_utc(-11, 18.0))
# print(time_to_utc(-1, 0.0))
# print(time_to_utc(-1, 23.0))


def time_from_utc(utc_offset, time):
    """ (number, float) -> float

    Return UTC time in time zone utc_offset.

    >>> time_from_utc(+0, 12.0)
    12.0
    >>> time_from_utc(+1, 12.0)
    13.0
    >>> time_from_utc(-1, 12.0)
    11.0
    >>> time_from_utc(+6, 6.0)
    12.0
    >>> time_from_utc(-7, 6.0)
    23.0
    >>> time_from_utc(-1, 0.0)
    23.0
    >>> time_from_utc(-1, 23.0)
    22.0
    >>> time_from_utc(+1, 23.0)
    0.0
    """

    return to_24_hour_clock(time + utc_offset)


# print(time_from_utc(+0, 12.0))
# print(time_from_utc(+1, 12.0))
# print(time_from_utc(-1, 12.0))
# print(time_from_utc(+6, 6.0))
# print(time_from_utc(-7, 6.0))
# print(time_from_utc(-1, 0.0))
# print(time_from_utc(-1, 23.0))
# print(time_from_utc(+1, 23.0))