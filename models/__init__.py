#!/usr/bin/python3
"""
File storage instance module
"""

from models.base_model import BaseModel
from ..engine.file_storage import FileStorage
import sys

storage = FileStorage()
storage.reload()
