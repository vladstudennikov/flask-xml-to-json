from flask import Flask, request, jsonify, render_template
from personal_data_libs import FullPersonalData
from it_data_libs import ITData

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template("index.html")

# Personal Data Endpoints
@app.route('/personal/xml-to-json', methods=['POST'])
def personal_xml_to_json():
    xml_data = request.data.decode('utf-8')
    try:
        json_data = FullPersonalData.xml_to_json(xml_data)
        return jsonify(json_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/personal/json-to-xml', methods=['POST'])
def personal_json_to_xml():
    json_data = request.json
    try:
        xml_data = FullPersonalData.json_to_xml(json_data)
        return xml_data, 200, {'Content-Type': 'application/xml'}
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# IT Data Endpoints
@app.route('/it/xml-to-json', methods=['POST'])
def it_xml_to_json():
    xml_data = request.data.decode('utf-8')
    try:
        json_data = ITData.xml_to_json(xml_data)
        return jsonify(json_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/it/json-to-xml', methods=['POST'])
def it_json_to_xml():
    json_data = request.json
    try:
        xml_data = ITData.json_to_xml(json_data)
        return xml_data, 200, {'Content-Type': 'application/xml'}
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
