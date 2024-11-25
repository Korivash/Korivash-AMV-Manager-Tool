class Utils:
    @staticmethod
    def convert_time_to_seconds(time_str):
        """
        Converts a time string in MM:SS or HH:MM:SS format to seconds.
        :param time_str: A string representing time in MM:SS or HH:MM:SS format.
        :return: Total seconds as an integer, or None if the format is invalid.
        """
        try:
            parts = [int(part) for part in time_str.split(":")]
            if len(parts) == 2:
                minutes, seconds = parts
                return minutes * 60 + seconds
            elif len(parts) == 3:
                hours, minutes, seconds = parts
                return hours * 3600 + minutes * 60 + seconds
            else:
                raise ValueError
        except (ValueError, AttributeError):
            return None
