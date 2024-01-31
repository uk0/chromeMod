
class HttpServer:
    def __init__(self):
       print("init ")
    def start_server(self):
        from flask import Flask
        app = Flask(__name__)
        @app.route('/api/v1/query')
        def index():
            return "Hello, World!"
        if __name__ == '__main__':
            app.run(debug=True)