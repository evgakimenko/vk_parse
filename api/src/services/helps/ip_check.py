import time

from fastapi import HTTPException, Request

MAX_REQUESTS_PER_IP = 1
requests_per_ip = {}


def rate_limit_client_ip(request: Request):
    client_ip = request.client.host
    if client_ip in requests_per_ip:
        elapsed_time = time.time() - requests_per_ip[client_ip]
        if elapsed_time < 1:
            raise HTTPException(status_code=429, detail="Too Many Requests")
    requests_per_ip[client_ip] = time.time()
    return True
