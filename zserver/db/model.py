"""This module contains the database models for the server."""
from mongoengine import Document, BinaryField, DictField, ReferenceField

class Agent(Document):
    """An agent is a user of the system. It is identified by its public key."""
    public_key = BinaryField(required=True)

    def __str__(self):
        return f"Agent(public_key={self.public_key})"

class Event(Document):
    """An event is an action that an agent performs on the system."""
    agent = ReferenceField(Agent, required=True)
    timestamp = BinaryField(required=True)
    signature = BinaryField(required=True)
    data = DictField(required=True)

    def __str__(self):
        str_contents = (
            f"agent={self.agent}",
            f"signature={self.signature}",
            f"timestamp={self.timestamp}",
            f"data={self.data}"
        )
        return f"Event({', '.join(str_contents)})"
