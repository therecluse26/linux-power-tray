class Listeners:

    events = []

    def register_listener(self, event, reaction):
        return
    
    def react(self, event):
        return

    def serve(self):
        return

class Event:
    monitored_file = None
    expected_value = None
    timestamp = None
    reactions = []
    polling_time_ms = 5000
    count = 0
    active = True
    
    def __init__(self, monitored_file, expected_value, reactions):
        self.monitored_file = monitored_file
        self.expected_value = expected_value
        self.reactions = reactions
        return

    def fire(self):
        for reaction in self.reactions:
            reaction.function()
        return

class Reaction:
    name = None
    function = None
    active = False