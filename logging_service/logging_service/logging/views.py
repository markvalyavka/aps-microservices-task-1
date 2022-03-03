import logging
from flask import request, jsonify

from logging_service.logging import logging


message_map = {}


@logging.route("/logging-service", methods=["GET", "POST"])
def logging():
    if request.method == "GET":
        return jsonify({
            "messages": list(message_map.values())
        })
    elif request.method == "POST":
        request_params = request.get_json()
        if not request_params:
            return "Error!"

        msg_uuid = request_params.get("uuid")
        msg_content = request_params.get("message")
        message_map[msg_uuid] = msg_content
        print({
            'message': msg_content,
            'uuid': msg_uuid
        })
        return {
            "status": 'OK'
        }

