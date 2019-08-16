from enum import  Enum
from collections import namedtuple

Error = namedtuple('Error', ['message', 'status_code'])

class Errors(Enum):
    PARAM_NOT_FOUND = Error('required parameter not found in request', 400)
    INVALID_PARAM = Error('parameter supplied is not valid', 400)


class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, error, payload=None):
        Exception.__init__(self)
        self.message = error.value.message
        self.error_code = error.name
        self.payload = payload
        self.status_code = error.value.status_code

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        rv['error_code'] = self.error_code
        return rv

