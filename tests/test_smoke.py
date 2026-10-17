def test_help_command_exact():
    res = reply("help")  # exact help command
    assert "Available commands" in res  # check help string

def test_help_command_in_sentence():
    res = reply("please help me")  # sentence containing help
    assert "Available commands" in res  # check help response