from elos_core import elos_status


def test_elos_status_shape():
    s = elos_status()
    assert isinstance(s, dict)
    assert s["name"] == "ELOS"
    assert s["state"] == "online"
    assert "version" in s
