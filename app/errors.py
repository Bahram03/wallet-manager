from flask import jsonify
from app import app


@app.errorhandler(404)
def not_found_error(error):
    return jsonify({'error': 'not found'}), 404


def no_name_found_error():
    return jsonify({'error': 'no name provided'}), 400
