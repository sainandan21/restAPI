from flask import Flask
main = Flask(__name__)
endpoint = "/restapi"
@main.route(endpoint)
def post_data(message = "Hello"):
    return message
if __name__ == '__main__':
    main.run(debug=True)

