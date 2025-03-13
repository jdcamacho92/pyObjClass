from datetime import datetime

class Call:
    def __init__(self, source: str, destination: str, duration: int, timestamp: str, calltype: str):
        self.source = source if isinstance(source, str) else "Unknown"
        self.destination = destination if isinstance(destination, str) else "Unknown"
        self._duration = max(0, duration) if isinstance(duration, int) else 0
        self._calltype = calltype if calltype in ["inbound", "outbound", "xfer"] else "unknown"
        
        # Validate and convert timestamp to datetime object
        try:
            self.timestamp = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            raise ValueError("Invalid date format, use YYYY-MM-DD HH:MM:SS")

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, new_duration):
        if isinstance(new_duration, int) and new_duration > 0:
            self._duration = new_duration
        else:
            raise ValueError("Duration is not valid, must be a positive integer")

    @duration.deleter
    def duration(self):
        del self._duration

    @property
    def calltype(self):
        return self._calltype

    @calltype.setter
    def calltype(self, new_calltype):
        if new_calltype in ["inbound", "outbound", "xfer"]:
            self._calltype = new_calltype
        else:
            raise ValueError("Invalid call type. Must be one of: inbound, outbound, xfer")
    
    @calltype.deleter
    def calltype(self):
        del self._calltype

    def __str__(self):
        return f"Call from {self.source} to {self.destination}, Duration: {self._duration}s, Time: {self.timestamp}, Type: {self._calltype}"

    def __eq__(self, other):
        if isinstance(other, Call):
            return (
                self.source == other.source and
                self.destination == other.destination and
                self._duration == other._duration and
                self.timestamp == other.timestamp and
                self._calltype == other._calltype
            )
        return False

    def __repr__(self):
        return f"Call(source='{self.source}', destination='{self.destination}', duration={self._duration}, timestamp='{self.timestamp}', calltype='{self._calltype}')"

class CallLog:
    def __init__(self):
        """
        Initializes an empty call log list.
        """
        self.listofcalls = []  # Stores Call objects
    
    def add_call(self, call: Call):
        """
        Adds a new Call object to the call log.
        """
        if isinstance(call, Call):
            self.listofcalls.append(call)
        else:
            raise ValueError("Only instances of Call can be added to the log.")
    
    def show_calls(self):
        """
        Returns a list of all stored call objects.
        """
        return self.listofcalls  

    def find_call_by_source_destination(self, source: str, destination: str):
        """
        Finds calls that match the given source and destination.
        :param source: The source number as a string.
        :param destination: The destination number as a string.
        :return: List of Call objects that match the source and destination.
        """
        if not isinstance(source, str) or not isinstance(destination, str):
            raise ValueError("Source and Destination must be strings.")
        return [call for call in self.listofcalls if call.source == source and call.destination == destination]
    
    def find_call_by_timerange(self, startdate: str, enddate: str):
        """
        Filters and returns calls that fall within the specified time range.
        :param startdate: Start datetime in 'YYYY-MM-DD HH:MM:SS' format.
        :param enddate: End date in the same format.
        :return: List of Call objects that have timestamps within the range.
        """
        try:
            startdateconv = datetime.strptime(startdate, "%Y-%m-%d %H:%M:%S")
            enddateconv = datetime.strptime(enddate, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            raise ValueError("Invalid date format, use YYYY-MM-DD HH:MM:SS")
        
        return [call for call in self.listofcalls if startdateconv <= call.timestamp <= enddateconv]
    
    def __repr__(self):
        return f"CallLog({self.listofcalls})"

# Example usage
call1 = Call("1201", "1002", 105, "2024-10-12 14:30:00", "inbound")
call2 = Call("1003", "1102", 200, "2024-10-12 15:00:00", "outbound")

logllamadas = CallLog()
logllamadas.add_call(call1)
logllamadas.add_call(call2)

print("All calls:", logllamadas.show_calls())
print("Calls from 1201 to 1002:", logllamadas.find_call_by_source_destination("1201", "1002"))
print("Calls in time range:", logllamadas.find_call_by_timerange("2024-10-10 13:30:00", "2024-10-10 15:00:00"))
