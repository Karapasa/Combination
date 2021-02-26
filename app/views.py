import logging.config
from settings import logging_config
from app import app
from app.utils.cobmination import res, moving_to_dir
from flask import render_template, request,  make_response, send_file

logging.config.dictConfig(logging_config)
logger = logging.getLogger('combination_logger')

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json(force=True)
    print(data)
    name = res(data['parlist'], data['exclist'])
    print(name)
    moving_to_dir(name)
    logger.debug("Данные и исключения: %s | %s", data['parlist'], data['exclist'])
    return make_response(name)

@app.route('/app/static/combs/<path>', methods=['GET'])
def download_file(path):
    return send_file(path)


@app.errorhandler(404)
def http_404_handler(error):
    return render_template('page_404.html'), 404

