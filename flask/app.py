import os

from flask import Flask


app = Flask(__name__)

@app.route('/about', methods=['GET'])
def about():
    version = os.environ.get('APP_VERSION')

    return { 'version': version}, 200


@app.route('/secrets', methods=['GET'])
def secret():
    creds = dict()
    creds['db_pass'] = os.environ.get('DB_PASSWORD')
    creds['app_token'] = os.environ.get('APP_TOKEN')
    creds['api_key'] = open("/run/secrets/api_key", "r").read()
    creds['api_key'] = open("/api_key.txt", "r").read()

    return creds, 200


@app.route('/config', methods=['GET'])
def config():
    config = dict()
    
    config['config_dev'] = open("/config-dev.yaml", "r").read()
    config['config_dev_v2'] = open("/config-dev-v2.yaml", "r").read()

    return config, 200