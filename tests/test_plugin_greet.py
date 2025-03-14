import pytest
from app import App

def test_app_greet_command(capfd, monkeypatch):
    inputs = iter(['greet', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    
    assert e.value.code == 0

    out, err = capfd.readouterr()
    
    assert "No such command: unknown_command" in out


