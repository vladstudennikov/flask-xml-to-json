class PersonalData:
    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email

    def to_dict(self):
        return {
            "name": self.name,
            "surname": self.surname,
            "email": self.email
        }
    
    def to_xml(self):
        return f"""<personal_data>
            <name>{self.name}</name>
            <surname>{self.surname}</surname>
            <email>{self.email}</email>
        </personal_data>"""
    
    def from_dict(data: dict):
        return PersonalData(
            name=data.get("name"),
            surname=data.get("surname"),
            email=data.get("email")
        )
    
    def from_xml(xml_data: str):
        def get_value(tag):
            start_tag = f"<{tag}>"
            end_tag = f"</{tag}>"
            start_index = xml_data.find(start_tag) + len(start_tag)
            end_index = xml_data.find(end_tag)
            return xml_data[start_index:end_index].strip()
        
        return PersonalData(
            name=get_value("name"),
            surname=get_value("surname"),
            email=get_value("email")
        )


class Address:
    def __init__(self, country, region, town, street):
        self.country = country
        self.region = region
        self.town = town
        self.street = street

    def to_dict(self):
        return {
            "country": self.country,
            "region": self.region,
            "town": self.town,
            "street": self.street
        }

    def to_xml(self):
        return f"""<address>
            <country>{self.country}</country>
            <region>{self.region}</region>
            <town>{self.town}</town>
            <street>{self.street}</street>
        </address>"""

    def from_dict(data: dict):
        return Address(
            country=data.get("country"),
            region=data.get("region"),
            town=data.get("town"),
            street=data.get("street")
        )
    
    def from_xml(xml_data: str):
        def get_value(tag):
            start_tag = f"<{tag}>"
            end_tag = f"</{tag}>"
            start_index = xml_data.find(start_tag) + len(start_tag)
            end_index = xml_data.find(end_tag)
            return xml_data[start_index:end_index].strip()
        
        return Address(
            country=get_value("country"),
            region=get_value("region"),
            town=get_value("town"),
            street=get_value("street")
        )


class Work:
    def __init__(self, company, position, education):
        self.company = company
        self.position = position
        self.education = education

    def to_dict(self):
        return {
            "company": self.company,
            "position": self.position,
            "education": self.education
        }

    def to_xml(self):
        return f"""<work>
            <company>{self.company}</company>
            <position>{self.position}</position>
            <education>{self.education}</education>
        </work>"""
    
    def from_dict(data: dict):
        return Work(
            company=data.get("company"),
            position=data.get("position"),
            education=data.get("education")
        )
    
    def from_xml(xml_data: str):
        def get_value(tag):
            start_tag = f"<{tag}>"
            end_tag = f"</{tag}>"
            start_index = xml_data.find(start_tag) + len(start_tag)
            end_index = xml_data.find(end_tag)
            return xml_data[start_index:end_index].strip()
        
        return Work(
            company=get_value("company"),
            position=get_value("position"),
            education=get_value("education")
        )


class FullPersonalData:
    def __init__(self, personal_data, address, work):
        self.personal_data = personal_data
        self.address = address
        self.work = work

    def to_dict(self):
        return {
            "personal_data": self.personal_data.to_dict(),
            "address": self.address.to_dict(),
            "work": self.work.to_dict()
        }
    
    def to_xml(self):
        return f"""<root>
            {self.personal_data.to_xml()}
            {self.address.to_xml()}
            {self.work.to_xml()}
        </root>"""
    
    def from_dict(data: dict):
        return FullPersonalData(
            personal_data=PersonalData.from_dict(data.get("personal_data", {})),
            address=Address.from_dict(data.get("address", {})),
            work=Work.from_dict(data.get("work", {}))
        )
    
    def from_xml(xml_data: str):
        def extract_section(tag):
            start_tag = f"<{tag}>"
            end_tag = f"</{tag}>"
            start_index = xml_data.find(start_tag)
            end_index = xml_data.find(end_tag) + len(end_tag)
            return xml_data[start_index:end_index].strip()
        
        personal_data_xml = extract_section("personal_data")
        address_xml = extract_section("address")
        work_xml = extract_section("work")
        
        return FullPersonalData(
            personal_data=PersonalData.from_xml(personal_data_xml),
            address=Address.from_xml(address_xml),
            work=Work.from_xml(work_xml)
        )
    
    @staticmethod
    def xml_to_json(xml_data: str):
        full_data = FullPersonalData.from_xml(xml_data)
        return full_data.to_dict()

    @staticmethod
    def json_to_xml(json_data: dict):
        full_data = FullPersonalData.from_dict(json_data)
        return full_data.to_xml()