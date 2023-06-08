from app.main import start


def test_start():
    res = start()

    assert res is None
