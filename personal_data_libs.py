from dataclasses import dataclass, asdict
import xmltodict # type: ignore
import json


@dataclass
class PersonalData:
    name: str
    surname: str
    email: str


@dataclass
class Address:
    country: str
    region: str
    town: str
    street: str


@dataclass
class Work:
    company: str
    position: str
    education: str


@dataclass
class FullPersonalData:
    personal_data: PersonalData
    address: Address
    work: Work

    def to_dict(self):
        return asdict(self)

    def to_xml(self):
        return xmltodict.unparse({"root": asdict(self)}, pretty=True)

    @staticmethod
    def from_dict(data: dict):
        return FullPersonalData(
            personal_data=PersonalData(**data["personal_data"]),
            address=Address(**data["address"]),
            work=Work(**data["work"])
        )

    @staticmethod
    def from_xml(xml_data: str):
        data = xmltodict.parse(xml_data)["root"]
        return FullPersonalData.from_dict(data)

    @staticmethod
    def xml_to_json(xml_data: str):
        return FullPersonalData.from_xml(xml_data).to_dict()

    @staticmethod
    def json_to_xml(json_data: dict):
        return FullPersonalData.from_dict(json_data).to_xml()


if __name__ == "__main__":
    person = FullPersonalData(
        personal_data=PersonalData("Alice", "Johnson", "alice@example.com"),
        address=Address("USA", "California", "Los Angeles", "Sunset Blvd 123"),
        work=Work("OpenAI", "Engineer", "MSc Computer Science")
    )

    xml_str = person.to_xml()
    print("XML:\n", xml_str)

    parsed_back = FullPersonalData.from_xml(xml_str)
    print("\nParsed back to dict:\n", parsed_back.to_dict())