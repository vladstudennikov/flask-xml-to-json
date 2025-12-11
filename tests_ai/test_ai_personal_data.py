from personal_data_libs import (
    FullPersonalData, PersonalData, Address, Work
)


def test_dict_round_trip():
    p = FullPersonalData(
        personal_data=PersonalData("A", "B", "a@b"),
        address=Address("C", "D", "E", "F"),
        work=Work("G", "H", "I")
    )

    d = p.to_dict()
    assert FullPersonalData.from_dict(d).to_dict() == d


def test_xml_round_trip():
    p = FullPersonalData(
        personal_data=PersonalData("X", "Y", "xy@z"),
        address=Address("U", "V", "W", "S"),
        work=Work("Comp", "Eng", "PhD")
    )

    xml_s = p.to_xml()
    restored = FullPersonalData.from_xml(xml_s)
    assert restored.to_dict() == p.to_dict()