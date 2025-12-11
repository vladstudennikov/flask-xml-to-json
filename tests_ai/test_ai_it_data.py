import pytest
from it_data_libs import ITData, Computer, ITProject


def test_dict_round_trip():
    data = ITData(
        computers=[Computer("laptop", "Dell", "XPS", "i7", 16, 512, "Windows")],
        it_projects=[
            ITProject(
                "Proj", "2020-01-01", "2020-12-31", 5, "Desc", ["Py", "Flask"]
            )
        ],
    )

    d = data.to_dict()
    restored = ITData.from_dict(d)
    assert restored.to_dict() == d


def test_xml_round_trip():
    data = ITData(
        computers=[Computer("desktop", "Apple", "iMac", "M1", 8, 256, "macOS")],
        it_projects=[ITProject("A", "2023", "2024", 3, "X", ["Go"])]
    )

    xml_s = data.to_xml()
    restored = ITData.from_xml(xml_s)
    assert restored.to_dict() == data.to_dict()


def test_numeric_normalization():
    src = {
        "computers": {
            "computer": {
                "type": "laptop",
                "brand": "HP",
                "model": "Z",
                "cpu": "i5",
                "ram_gb": "16",
                "storage_gb": "",
                "os": "Win"
            }
        },
        "it_projects": {
            "project": {
                "project_name": "X",
                "start_date": "a",
                "end_date": "b",
                "team_size": None,
                "description": "d",
                "technologies": {"technology": "Py"}
            }
        },
    }

    obj = ITData.from_dict(src)
    c = obj.computers[0]
    p = obj.it_projects[0]

    assert c.ram_gb == 16
    assert c.storage_gb == 0
    assert p.team_size == 0
    assert p.technologies == ["Py"]