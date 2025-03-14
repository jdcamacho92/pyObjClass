from datetime import datetime

class Call:
    # Initialize a Call object with source, destination, duration, timestamp, and call type of the object
    def __init__(self, source: str, destination: str, duration: int, timestamp: str):
        self.source = source  # Source phone number
        self.destination = destination if isinstance(destination, str) else "Unknown"  # Ensure destination is a string
        self._duration = max(0, duration) if isinstance(duration, int) else 0  # Ensure duration is a positive integer
        self.timestamp = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S") if isinstance(timestamp, str) else datetime.now()
        self._calltype = "unknown"  # Default value for call type
    
    @property
    def duration(self):
        return self._duration
    
    @duration.setter
    def duration(self, new_duration):
        if isinstance(new_duration, int) and new_duration > 0:
            self._duration = new_duration
        else:
            raise ValueError("Duration is not valid, it must be a positive integer")
    
    @duration.deleter
    def duration(self):
        del self._duration
    
    @property
    def call_type(self):
        return self._calltype
    
    @call_type.setter
    def call_type(self, new_calltype):
        valid_calltypes = ["inbound", "outbound", "xfer"]  # Allowed call types
        if new_calltype in valid_calltypes:
            self._calltype = new_calltype
        else:
            raise ValueError("Call type is not valid, must be one of: inbound, outbound, xfer")
    
    @call_type.deleter
    def call_type(self):
        del self._calltype

    def __str__(self):
        return f"Call from {self.source} to {self.destination} | Duration: {self._duration} seconds | Type: {self._calltype} | Time: {self.timestamp}"

    def __eq__(self, other):
        return (
            isinstance(other, Call) and
            self.source == other.source and
            self.destination == other.destination and
            self._duration == other._duration and
            self.timestamp == other.timestamp
        )
    
    def __repr__(self):
        return f"Call(source='{self.source}', destination='{self.destination}', duration={self._duration}, timestamp='{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}', calltype='{self._calltype}')"

class CallLog:
    """Class to store and manage a collection of call records"""
    def __init__(self):
        self.listofcalls = []  # Initialize an empty list of calls
    
    def add_call(self, call: Call):
        """Adds a Call object to the list of calls if it is of type Call"""
        if isinstance(call, Call):
            self.listofcalls.append(call)
        else:
            raise TypeError("Only Call objects can be added to the log")
    
    def find_call_by_source_destination(self, source: str, destination: str):
        """Finds and returns a list of calls matching the given source and destination numbers"""
        if not isinstance(source, str) or not isinstance(destination, str):
            raise TypeError("Source and destination must be strings")
        
        return [call for call in self.listofcalls if call.source == source and call.destination == destination]
    
    def find_call_by_timerange(self, startdate: str, enddate: str):
        """Finds and returns a list of calls that fall within the given time range"""
        try:
            startdateconv = datetime.strptime(startdate, "%Y-%m-%d %H:%M:%S")
            enddateconv = datetime.strptime(enddate, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            raise ValueError("Invalid date format, use YYYY-MM-DD HH:MM:SS")
        
        return [call for call in self.listofcalls if startdateconv <= call.timestamp <= enddateconv]
    
    def show_calls(self):
        """Returns all stored calls in a formatted string"""
        return "\n".join(str(call) for call in self.listofcalls)
    
    def __repr__(self):
        return f"CallLog({self.listofcalls})"
