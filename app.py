from flask import Flask, request, jsonify
import jwt
import datetime

class Config:
    API_KEY = "2f5ae96c-b558-4c7b-a590-a501ae1c3f6c"
    SECRET_KEY = "1234"

app = Flask(__name__)
app.config.from_object(Config)

def validate_token(token):
    try:
        jwt_payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        # Aquí puedes incluir la lógica adicional basada en el JWT payload si es necesario
        return jwt_payload
    except jwt.ExpiredSignatureError:
        return {"ERROR": "JWT Token Expired"}
    except jwt.InvalidTokenError:
        return {"ERROR": "Invalid JWT Token"}

@app.route('/DevOps', methods=['POST'])
def devops():
    if 'X-Parse-REST-API-Key' not in request.headers or request.headers['X-Parse-REST-API-Key'] != app.config['API_KEY']:
        return jsonify({"ERROR": "Unauthorized"}), 401

    if 'X-JWT-KEY' not in request.headers:
        return jsonify({"ERROR": "JWT Token Missing"}), 401

    token = request.headers['X-JWT-KEY']
    validation_result = validate_token(token)

    if 'ERROR' in validation_result:
        return jsonify(validation_result), 401

    content = request.json
    message = content.get('message')
    to = content.get('to')
    return jsonify({
        "message": f"Hello {to} your message will be sent"
    })

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"ERROR": "Invalid Request"}), 404

if __name__ == '__main__':
    app.run(debug=True)
