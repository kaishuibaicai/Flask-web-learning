from functools import wraps
from flask import g
from .errors import forbidden


def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not g.current.can(permission):
                return forbiddent('Insufficient permission')
            return f(*args, **kwargs)
        return decorated_function
    return decorator