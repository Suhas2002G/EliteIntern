from flask import jsonify

def success_response(data=None, message="Request successful", status_code=200, meta=None):
    response = {
        "status": "success",
        "message": message,
        "data": data or {},
        "meta": meta or {}
    }
    return jsonify(response), status_code

def error_response(message="Something went wrong", status_code=400, error_details=None, meta=None):
    response = {
        "status": "error",
        "message": message,
        "error": {
            "details": error_details or "An unexpected error occurred."
        },
        "meta": meta or {}
    }
    return jsonify(response), status_code
