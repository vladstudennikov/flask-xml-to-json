from dataclasses import dataclass, asdict, field
from typing import List
import xmltodict  # type: ignore
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
        data = asdict(self)

        xml_ready = {"root": {}}

        # Computers: <computers><computer>...</computer>...</computers>
        comps = data.get("computers", [])
        xml_ready["root"]["computers"] = {"computer": comps if comps else []}

        # Projects: technologies become repeated <technology> tags
        projects = []
        for pr in data.get("it_projects", []):
            pr_copy = dict(pr)
            techs = pr_copy.get("technologies", [])
            pr_copy["technologies"] = {"technology": techs if techs else []}
            projects.append(pr_copy)
        xml_ready["root"]["it_projects"] = {"project": projects if projects else []}

        return xmltodict.unparse(xml_ready, pretty=True)

    @staticmethod
    def _to_int_safe(value):
        """
        Convert value to int if possible; if value is None or empty, return 0.
        If it's already int, return as is.
        """
        if isinstance(value, int):
            return value
        if value is None:
            return 0
        s = str(value).strip()
        if s == "":
            return 0
        try:
            return int(s)
        except ValueError:
            # If conversion fails, re-raise so developer notices invalid input shapes
            raise

    @staticmethod
    def from_dict(data: dict):
        # Defensive shallow copy
        data = dict(data)

        # --- Computers ---
        comps = data.get("computers", [])
        if isinstance(comps, dict) and "computer" in comps:
            comps_list = comps["computer"]
        else:
            comps_list = comps

        if not isinstance(comps_list, list):
            comps_list = [comps_list] if comps_list else []

        computers: List[Computer] = []
        for c in comps_list:
            # Ensure we don't mutate caller dict
            c_copy = dict(c)
            # Normalize numeric fields: ram_gb, storage_gb
            if "ram_gb" in c_copy:
                c_copy["ram_gb"] = ITData._to_int_safe(c_copy["ram_gb"])
            else:
                c_copy["ram_gb"] = 0
            if "storage_gb" in c_copy:
                c_copy["storage_gb"] = ITData._to_int_safe(c_copy["storage_gb"])
            else:
                c_copy["storage_gb"] = 0
            computers.append(Computer(**c_copy))

        # --- Projects ---
        projects_block = data.get("it_projects", [])
        if isinstance(projects_block, dict) and "project" in projects_block:
            projects_list = projects_block["project"]
        else:
            projects_list = projects_block

        if not isinstance(projects_list, list):
            projects_list = [projects_list] if projects_list else []

        it_projects: List[ITProject] = []
        for p in projects_list:
            p_copy = dict(p)

            techs = p_copy.get("technologies", [])
            if isinstance(techs, dict) and "technology" in techs:
                techs_val = techs["technology"]
            else:
                techs_val = techs

            if isinstance(techs_val, list):
                techs_normalized = techs_val
            elif techs_val is None or techs_val == "":
                techs_normalized = []
            else:
                techs_normalized = [techs_val]

            p_copy["technologies"] = techs_normalized

            # Normalize numeric team_size
            if "team_size" in p_copy:
                p_copy["team_size"] = ITData._to_int_safe(p_copy["team_size"])
            else:
                p_copy["team_size"] = 0

            it_projects.append(ITProject(**p_copy))

        return ITData(computers=computers, it_projects=it_projects)

    @staticmethod
    def from_xml(xml_data: str):
        parsed = xmltodict.parse(xml_data)
        root = parsed.get("root", {})
        return ITData.from_dict(root)

    @staticmethod
    def xml_to_json(xml_data: str):
        return ITData.from_xml(xml_data).to_dict()

    @staticmethod
    def json_to_xml(json_data: dict):
        return ITData.from_dict(json_data).to_xml()


if __name__ == '__main__':
    # Quick manual check
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