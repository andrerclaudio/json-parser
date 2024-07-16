# Build-in modules
import logging
import os

# Installed modules
from flask import Flask

logger = logging.getLogger(__name__)


class CreateApp(object):
    """
    Start Flask application.
    """

    def __init__(self):
        # Place where app is defined
        self.app = Flask(__name__, instance_relative_config=False)