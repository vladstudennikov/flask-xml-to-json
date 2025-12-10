from dataclasses import dataclass, asdict, field
from typing import List
import xmltodict # type: ignore
import json


@dataclass
class Computer:
    type: str
    brand: str
    model: str
    cpu: str
    ram_gb: int
    storage_gb: int
    os: str


@dataclass
class ITProject:
    project_name: str
    start_date: str
    end_date: str
    team_size: int
    description: str
    technologies: List[str] = field(default_factory=list)


@dataclass
class ITData:
    computers: List[Computer] = field(default_factory=list)
    it_projects: List[ITProject] = field(default_factory=list)

    def to_dict(self):
        return asdict(self)

    def to_xml(self):
        return xmltodict.unparse({"root": asdict(self)}, pretty=True)

    @staticmethod
    def from_dict(data: dict):
        computers_data = data.get("computers", [])
        projects_data = data.get("it_projects", [])

        # Handle case where there's only one item and it's not a list
        if not isinstance(computers_data, list):
            computers_data = [computers_data]
        if not isinstance(projects_data, list):
            projects_data = [projects_data]

        computers = [Computer(**c) for c in computers_data]
        it_projects = []
        for p in projects_data:
            techs = p.get("technologies")
            if techs:
                if isinstance(techs, dict):
                    techs = techs.get("technology", [])
                if not isinstance(techs, list):
                    techs = [techs]
            else:
                techs = []
            p["technologies"] = techs
            it_projects.append(ITProject(**p))

        return ITData(computers=computers, it_projects=it_projects)

    @staticmethod
    def from_xml(xml_data: str):
        data = xmltodict.parse(xml_data).get("root", {})
        return ITData.from_dict(data)

    @staticmethod
    def xml_to_json(xml_data: str):
        return ITData.from_xml(xml_data).to_dict()

    @staticmethod
    def json_to_xml(json_data: dict):
        return ITData.from_dict(json_data).to_xml()

if __name__ == '__main__':
    # Example usage
    computers = [
        Computer("laptop", "Dell", "XPS 15", "Intel Core i9", 32, 1024, "Windows 11"),
        Computer("desktop", "Apple", "iMac 24", "Apple M1", 16, 512, "macOS")
    ]
    projects = [
        ITProject("AI Chatbot", "2023-01-15", "2023-12-20", 8, "A chatbot for customer service.", ["Python", "TensorFlow", "Flask"]),
        ITProject("E-commerce Platform", "2022-05-10", "2024-05-30", 15, "A full-featured online store.", ["Java", "Spring", "React", "PostgreSQL"])
    ]
    it_data = ITData(computers=computers, it_projects=projects)

    xml_str = it_data.to_xml()
    print("XML:\n", xml_str)

    parsed_back = ITData.from_xml(xml_str)
    print("\nParsed back to dict:\n", json.dumps(parsed_back.to_dict(), indent=2))
