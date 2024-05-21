#!/usr/bin/env python3
"""
a class to manage the API authentication
"""
from typing import List, TypeVar
from flask import request
import fnmatch

class Auth:
    """
        manage the API authentication
    """
    def __init__(self) -> None:
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
         Method to check if auth is required.
        """
        if path is None or excluded_paths is None:
            return True

        for exec_path in excluded_paths:
            if fnmatch.fnmatch(path, exec_path):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Method to get authorization header.
        """
        return True

    def current_user(self, request=None) -> TypeVar('User'):
        """ Method to get authorization header.
        """
        return None
