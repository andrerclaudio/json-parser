# Build-in modules
import logging

# Installed modules
from flask import jsonify, request

# Local modules
from app.connectors import CreateApp
from app.error_codes import ValidationCodes

# Print in software terminal
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s | %(process)d | %(name)s | %(levelname)s:  %(message)s',
                    datefmt='%d/%b/%Y - %H:%M:%S')

logger = logging.getLogger(__name__)

"""
Create Flask object and basic routes.
"""
application = CreateApp()
app = application.app


# ----------------------------------------------------------------------------------------------------------------------
# Basic routes

@app.route('/', methods=['GET'])
def index():
    """Application is alive"""
    message = {"Agnes. Your reading companion!"}
    resp = jsonify(message)
    # Sending OK response
    resp.status_code = 200
    # Returning the object
    return resp


@app.errorhandler(404)
def page_not_found(e):
    """Send message to the user with notFound 404 status."""
    # Message to the user
    message = {
        "err":
            {
                "msg": "This route is currently not supported."
            }
    }
    logger.error(e)
    # Making the message looks good
    resp = jsonify(message)
    # Sending ERROR response
    resp.status_code = 404
    # Returning the object
    return resp


# ----------------------------------------------------------------------------------------------------------------------
# Show Main Options screen 


