
import pytest
from it_data_libs import ITData, Computer, ITProject

@pytest.fixture
def sample_it_data():
    return ITData(
        computers=[
            Computer("laptop", "Dell", "XPS 15", "Intel Core i9", 32, 1024, "Windows 11"),
            Computer("desktop", "Apple", "iMac 24", "Apple M1", 16, 512, "macOS")
        ],
        it_projects=[
            ITProject("AI Chatbot", "2023-01-15", "2023-12-20", 8, "A chatbot for customer service.", ["Python", "TensorFlow", "Flask"]),
            ITProject("E-commerce Platform", "2022-05-10", "2024-05-30", 15, "A full-featured online store.", ["Java", "Spring", "React", "PostgreSQL"])
        ]
    )

@pytest.fixture
def sample_it_data_dict():
    return {
        "computers": [
            {"type": "laptop", "brand": "Dell", "model": "XPS 15", "cpu": "Intel Core i9", "ram_gb": 32, "storage_gb": 1024, "os": "Windows 11"},
            {"type": "desktop", "brand": "Apple", "model": "iMac 24", "cpu": "Apple M1", "ram_gb": 16, "storage_gb": 512, "os": "macOS"}
        ],
        "it_projects": [
            {"project_name": "AI Chatbot", "start_date": "2023-01-15", "end_date": "2023-12-20", "team_size": 8, "description": "A chatbot for customer service.", "technologies": ["Python", "TensorFlow", "Flask"]},
            {"project_name": "E-commerce Platform", "start_date": "2022-05-10", "end_date": "2024-05-30", "team_size": 15, "description": "A full-featured online store.", "technologies": ["Java", "Spring", "React", "PostgreSQL"]}
        ]
    }

def test_to_dict(sample_it_data, sample_it_data_dict):
    assert sample_it_data.to_dict() == sample_it_data_dict

def test_from_dict(sample_it_data_dict):
    data = ITData.from_dict(sample_it_data_dict)
    assert len(data.computers) == 2
    assert data.computers[0].brand == "Dell"
    assert len(data.it_projects) == 2
    assert data.it_projects[1].project_name == "E-commerce Platform"

def test_xml_to_json(sample_it_data_dict):
    # Convert dict to xml, then xml to json, and check if it's the same
    xml_data = ITData.json_to_xml(sample_it_data_dict)
    json_data = ITData.xml_to_json(xml_data)
    assert json_data == sample_it_data_dict

def test_json_to_xml(sample_it_data_dict):
    xml_data = ITData.json_to_xml(sample_it_data_dict)
    # To robustly check, we convert back to a dictionary.
    data_from_xml = ITData.from_xml(xml_data)
    assert data_from_xml.to_dict() == sample_it_data_dict
