from quart import Quart, request, jsonify
from logging.config import dictConfig
import os

dictConfig({
    'version': 1,
    'loggers': {
        'quart.app': {
            'level': 'DEBUG',
        },
    },
})

app = Quart(__name__)


@app.route('/')
async def hello():
    return 'hello'


# Проверка доступности Endpoint URL провайдера
@app.route('/gitlab/v1.0/', methods=['GET', 'POST', 'HEAD'])
async def ping():
    if request.method == 'HEAD':
        return jsonify({})

# https://yandex.ru/dev/dialogs/alice/doc/smart-home/reference/unlink-docpage/
#
@app.route('/gitlab/v1.0/user/unlink', methods=['GET', 'POST', 'HEAD'])
async def unlink():
    app.logger.debug('%s', request.headers)
    if request.method == 'POST':
        return jsonify({
            "request_id": request.headers.get('X-Request-Id')
        })


# Информация об устройствах пользователя
# https://yandex.ru/dev/dialogs/alice/doc/smart-home/reference/get-devices-docpage/
# GET https://endpoint_url/v1.0/user/devices
@app.route('/gitlab/v1.0/user/devices', methods=['GET'])
async def devices():
    headers = request.headers
    app.logger.debug('%s', headers)
    res = os.system("curl --header 'Authorization: {}' 'https://gitlab.com/api/v4/user'".
                    format(request.headers.get('Authorization')))
    app.logger.debug('res=%s', res)
    if request.method == 'GET':
        return jsonify({
            "request_id": request.headers.get('X-Request-Id'),
            "payload": {
                "devices": [],
                "user_id": '154646247'
            }
        })


# https://yandex.ru/dev/dialogs/alice/doc/smart-home/reference/post-devices-query-docpage/
# POST https://endpoint_url/v1.0/user/devices/query
@app.route('/gitlab/v1.0/user/devices/query', methods=['POST'])
async def query():
    headers = request.headers
    data = await request.get_json()
    app.logger.debug('%s - %s', headers, data)
    if request.method == 'POST':
        return jsonify({
            "request_id": request.headers.get('X-Request-Id'),
            "payload": {
                "devices": [],
                "user_id": ''
            }
        })


# POST https://endpoint_url/v1.0/user/devices/action
@app.route('/gitlab/v1.0/user/devices/action', methods=['POST'])
async def action():
    headers = request.headers
    data = await request.get_json()
    app.logger.debug('%s - %s', headers, data)
    if request.method == 'POST':
        return jsonify({
            "request_id": request.headers.get('X-Request-Id'),
            "payload": {
                "devices": []
            }
        })


# https://api.ffck.ru/v1/callbak
# https://gitlab.com/oauth/applications/151925
@app.route('/v1/callbak', methods=['GET'])
async def callback():
    headers = request.headers
    data = await request.get_json()
    app.logger.debug('%s - %s', headers, data)
    if request.method == 'GET':
        return "Ok"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
