import uuid

def get_random_guid():
    return str(uuid.uuid4()).replace('-', '')