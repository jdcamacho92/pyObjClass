from datetime import datetime

class Call:
    def __init__(self, source: str, destination: str , duration: int, timestamp: str, calltype: str):
        self.source =  source
        self.destination = destination
        self._duration = max(0, int(duration)) #make sure is positive
        self.timestamp = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S") #convert to datetime var if needed at future
        self._calltype = calltype
    
    ### getter setters deleters for <duration>
    #getter
    @property
    def duration(self):
        return self._duration

    #setter, validate is integer and positive
    @duration.setter
    def duration(self, new_duration):
        if isinstance(new_duration, int) and new_duration > 0 :
            self._duration = new_duration
        else:
            print ("Duration is not valid, not positive or integer")

    #deleter
    @duration.deleter
    def duration(self):
        del self._duration


    ### get/set/del for <calltype>
    #getter
    @property
    def calltype(self):
        return self._calltype

    #setter
    @calltype.setter
    def calltype(self, new_calltype):
        if new_calltype in ["inbound", "outbound", "xfer"]:
            self._calltype = new_calltype
        else:
            print ("calltype is not valid, must be of inbound, outbound, xfer")

    #deleter
    @calltype.deleter
    def calltype(self):
        del self._calltype

    
    def __str__(self):
        return f"Llamada de {self.source} a {self.destination} - Duracion: {self._duration} - Realizada en {self.timestamp} - tipo de llamada {self._calltype} "
    
    #check if 2 calls (llamadas) are the same call
    def __eq__(self, other):
        return isinstance(other, Call) and \
                self.source == other.source and \
                self.destination == other.destination and \
                self._duration == other._duration and \
                self.timestamp == other.timestamp and \
                self._calltype == other._calltype
    
    #convert to dict for JSON manipulation 
    def to_dict(self):
        return {"origen": self.source, 
                "destino": self.destination, 
                "duracion": self._duration, 
                "timestamp": self.timestamp.strftime("%Y-%m-%d %H:%M:%S"), #convert to string to make sure the dict accepts it
                "calltype": self._calltype}
    
    #for debugging
    def __repr__(self):
        return f"Call(source='{self.source}', destination='{self.destination}', duration={self._duration}, timestamp='{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}', calltype='{self._calltype}')"

call1 = Call("1201","1002",105,"2024-10-10 14:30:00", "inbound")
#print(call1)
print(repr(call1))
