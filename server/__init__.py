class HttpServer:
    def __init__(self):
        print("init ")
        from flask import Flask
        self.app = Flask(__name__)

    def start_server(self):
        @self.app.route('/api/v1/query')
        def index():
            return "any!"

        self.app.run(debug=True)
