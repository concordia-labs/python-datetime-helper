from datetime import datetime, time

HOUR_SECONDS = 3600 # The amount of seconds in an hour
DAY_HOURS = 24 # The amount of hours in a day
MINUTE_SECONDS = 60 # The amount of seconds in a minute
HOURS_MINUTES = 60 # The amount of minutes in an hour

class TimeHelper():
    """
        A class with helpers that assist on time conversion management
    """

    @staticmethod
    def is_time_between(period_beginning: float, period_ending: float, given_time: float=datetime.utcnow().time()) -> bool:
        """
            Verify if the time is between the given period

            Parameters:
                period_beginning (float): The beginning of the period in seconds
                period_ending (float): The ending of the period in seconds
                given_time (float): The time that will be verified to fit or not into the period, in seconds
            Returns:
                bool: A boolean indicating if the time is or not into the period
        """
        if period_beginning < period_ending:
            return given_time >= period_beginning and given_time <= period_ending
        else:
            # If the period passes midnight, use a different rule inverting the validation
            return given_time >= period_beginning or given_time <= period_ending

    @staticmethod
    def time_instance_to_seconds(time_instance: time) -> float:
        """
            Converts a time instance to seconds
        """
        time_positions = time_instance.isoformat().split(':')
        time_hours_seconds = TimeHelper.hours_to_seconds(float(time_positions[0]))
        time_minutes_seconds = TimeHelper.minutes_to_seconds(float(time_positions[1]))
        time_seconds = TimeHelper.minutes_to_seconds(float(time_positions[2]))
        
        return time_hours_seconds + time_minutes_seconds + time_seconds
        
    @staticmethod
    def days_to_seconds(days: float) -> float:
        """
            Converts the given days to seconds
        """
        return days * DAY_HOURS * HOUR_SECONDS

    @staticmethod
    def hours_to_seconds(hours: float) -> float:
        """
            Converts the given hours to seconds
        """
        return hours * HOUR_SECONDS

    @staticmethod
    def minutes_to_seconds(minutes: float) -> float:
        """
            Converts the given minutes to seconds
        """
        return minutes * MINUTE_SECONDS

    @staticmethod
    def seconds_to_days(seconds: float) -> float:
        """
            Converts the given seconds to days
        """
        return seconds / (DAY_HOURS * HOUR_SECONDS)

    @staticmethod
    def seconds_to_hours(seconds: float) -> float:
        """
            Converts the given seconds to hours
        """
        return seconds / HOUR_SECONDS

    @staticmethod
    def seconds_to_minutes(seconds: float) -> float: 
        """
            Converts the given seconds to minutes
        """
        return seconds / MINUTE_SECONDS
