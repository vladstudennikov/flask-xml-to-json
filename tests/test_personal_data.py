
import pytest
from personal_data_libs import FullPersonalData, PersonalData, Address, Work

@pytest.fixture
def sample_personal_data():
    return FullPersonalData(
        personal_data=PersonalData("John", "Doe", "john.doe@example.com"),
        address=Address("USA", "California", "Los Angeles", "123 Main St"),
        work=Work("Example Corp", "Software Engineer", "BSc Computer Science")
    )

@pytest.fixture
def sample_personal_data_dict():
    return {
        "personal_data": {
            "name": "John",
            "surname": "Doe",
            "email": "john.doe@example.com"
        },
        "address": {
            "country": "USA",
            "region": "California",
            "town": "Los Angeles",
            "street": "123 Main St"
        },
        "work": {
            "company": "Example Corp",
            "position": "Software Engineer",
            "education": "BSc Computer Science"
        }
    }

@pytest.fixture
def sample_personal_data_xml():
    return """<?xml version="1.0" encoding="utf-8"?>
<root>
	<personal_data>
		<name>John</name>
		<surname>Doe</surname>
		<email>john.doe@example.com</email>
	</personal_data>
	<address>
		<country>USA</country>
		<region>California</region>
		<town>Los Angeles</town>
		<street>123 Main St</street>
	</address>
	<work>
		<company>Example Corp</company>
		<position>Software Engineer</position>
		<education>BSc Computer Science</education>
	</work>
</root>"""

def test_to_dict(sample_personal_data, sample_personal_data_dict):
    assert sample_personal_data.to_dict() == sample_personal_data_dict

def test_from_dict(sample_personal_data_dict):
    data = FullPersonalData.from_dict(sample_personal_data_dict)
    assert data.personal_data.name == "John"
    assert data.address.street == "123 Main St"
    assert data.work.company == "Example Corp"

def test_xml_to_json(sample_personal_data_xml, sample_personal_data_dict):
    json_data = FullPersonalData.xml_to_json(sample_personal_data_xml)
    assert json_data == sample_personal_data_dict

def test_json_to_xml(sample_personal_data_dict, sample_personal_data_xml):
    # The exact XML string can vary slightly, so we parse it back
    # to a dictionary for a more robust comparison.
    xml_data = FullPersonalData.json_to_xml(sample_personal_data_dict)
    json_from_xml = FullPersonalData.xml_to_json(xml_data)
    assert json_from_xml == sample_personal_data_dict
