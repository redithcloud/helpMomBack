from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:Curso1234.@127.0.0.1/helpMomBD'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Definición del modelo de datos
class Respuesta(db.Model):
    __tablename__ = 'Encuestas'
    id = db.Column(db.Integer, primary_key=True)
    respuesta1 = db.Column(db.String(255))
    valor1 = db.Column(db.Integer)
    respuesta2 = db.Column(db.String(255))
    valor2 = db.Column(db.Integer)
    # ... añade más campos aquí según sea necesario

@app.route('/respuestas', methods=['POST', 'OPTIONS'])
@cross_origin()
def guardar_respuestas():
    if request.method == 'OPTIONS':
        # Pre-flight request. Reply successfully:
        return jsonify({'status': 'success'}), 200
    elif request.method == 'POST':
        data = request.get_json()
        print('Datos recibidos:', data)  # Imprime los datos recibidos
        nueva_respuesta = Respuesta(
            respuesta1=data['respuesta1'],
            valor1=data['valor1'],
            respuesta2=data['respuesta2'],
            valor2=data['valor2'],
            # ... añade más campos aquí según sea necesario
        )
        db.session.add(nueva_respuesta)
        db.session.commit()
        return jsonify({'id': nueva_respuesta.id}), 201

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=5000)
