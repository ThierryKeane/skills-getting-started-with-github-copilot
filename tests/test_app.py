from fastapi.testclient import TestClient

from src.app import activities, app


client = TestClient(app)


def test_unregister_participant_removes_email_from_activity():
    activity_name = "Chess Club"
    email = "student@example.com"
    activity = activities[activity_name]

    activity["participants"].append(email)

    try:
        response = client.delete(
            f"/activities/{activity_name}/signup",
            params={"email": email},
        )

        assert response.status_code == 200
        assert email not in activity["participants"]
        assert response.json()["message"] == f"Unregistered {email} from {activity_name}"
    finally:
        if email in activity["participants"]:
            activity["participants"].remove(email)
