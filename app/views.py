from app import app
from app.utils.cobmination import res, moving_to_dir
from flask import render_template, request,  make_response, send_file

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json(force=True)
    name = res(data['parlist'], data['exclist'])
    moving_to_dir(name)
    return make_response(name)

@app.route('/app/static/combs/<path>', methods=['GET'])
def download_file(path):
    return send_file(path)


@app.errorhandler(404)
def http_404_handler(error):
    return render_template('page_404.html'), 404

