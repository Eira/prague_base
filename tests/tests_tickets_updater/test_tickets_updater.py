from app.tickets_updater import tickets_updater


async def test_tickets_updater_smoke():
    await tickets_updater()

    assert True
