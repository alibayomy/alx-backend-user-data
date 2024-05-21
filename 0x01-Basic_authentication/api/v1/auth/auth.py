#!/usr/bin/env python3
"""
a class to manage the API authentication
"""
from typing import List, TypeVar
from flask import request


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
        return False

    def authorization_header(self, request=None) -> str:
        """
        Method to get authorization header.
        """
        return True

    def current_user(self, request=None) -> TypeVar('User'): 
        """ Method to get authorization header.
        """
        return None
         