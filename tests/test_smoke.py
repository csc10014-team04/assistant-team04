def test_partial_office_name():
    res = reply("where is training")  # query with partial name
    assert "1.101" in res  # verify correct room returned

def test_partial_office_name_case_insensitive():
    res = reply("WHERE IS TRAINING")  # query with uppercase partial name
    assert "1.101" in res  # verify case insensitivity