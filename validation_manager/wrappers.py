from functools import wraps
from flask_login import current_user
from flask import abort, jsonify, request

from api.functions import is_key_blocked
from models import ApiKey
from validation_manager.functions import get_route_status


def logout_required(func):
    """Checks whether user is logged out or raises error 401."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_user.is_authenticated:
            abort(401)
        return func(*args, **kwargs)

    return wrapper


def admin_only(func):
    """Checks whether user is admin or raises error 403."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_user.is_authenticated is False or current_user.admin is False:
            abort(403)
        return func(*args, **kwargs)

    return wrapper


def staff_only(func):
    """Checks whether a user is a staff member or raises 403 error."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_user.is_authenticated is False:
            abort(401)
        if current_user.admin is False and current_user.author is False:
            abort(403)
        return func(*args, **kwargs)

    return wrapper


def validate_api_route(func):
    """Checks whether a route is available or raises the appropriate error."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        route_status = get_route_status(func.__name__)
        print(route_status)
        if route_status == 'blocked':
            return jsonify(response={"Route Blocked": "The requested route is blocked."}), 503
        elif route_status == 'unavailable':
            return jsonify(response={"Route Configuration Unavailable": "The requested route configuration"
                                                                        " is unavailable."}), 500
        else:
            return func(*args, **kwargs)

    return wrapper


def validate_api_key(func):
    """Checks whether an api key is valid or raises the appropriate error."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        api_key = request.args.get('api_key')
        requested_key = ApiKey.query.filter_by(api_key=api_key).first()
        if requested_key:
            if is_key_blocked(api_key):
                return jsonify(response={"Forbidden": "Blocked API Key."}), 403
            return func(*args, **kwargs)
        else:
            return jsonify(response={"Malformed API Request": "Invalid API Key."}), 401

    return wrapper