from flask import Flask, request, jsonify # type: ignore
from personal_data import PersonalData, Address, Work, FullPersonalData

app = Flask(__name__)

@app.route('/xml-to-json', methods=['POST'])
def xml_to_json():
    xml_data = request.data.decode('utf-8')
    try:
        full_personal_data = FullPersonalData.xml_to_json(xml_data)
        return jsonify(full_personal_data), 200, {'Content-Type': 'application/json'}
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route('/json-to-xml', methods=['POST'])
def json_to_xml():
    json_data = request.json
    try:
        xml_data = FullPersonalData.json_to_xml(json_data)
        return xml_data, 200, {'Content-Type': 'application/xml'}
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
    
if __name__ == '__main__':  
    app.run(debug=True)