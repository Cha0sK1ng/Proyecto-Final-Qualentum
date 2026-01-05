class TestInsertData:
    def test_insert_data_success(self, client):
        response = client.post("/data", json={"name": "test_item"})
        assert response.status_code == 200
        assert response.json["message"] == "Data inserted successfully"

    def test_insert_data_duplicate(self, client):
        client.post("/data", json={"name": "duplicate"})
        response = client.post("/data", json={"name":  "duplicate"})
        assert response.status_code == 409
        assert response.json["message"] == "Data already exists"


class TestGetData:
    def test_get_all_data_empty(self, client):
        response = client.get("/data")
        assert response.status_code == 200
        assert response.json == []

    def test_get_all_data_with_items(self, client):
        client.post("/data", json={"name": "item1"})
        client.post("/data", json={"name": "item2"})
        response = client.get("/data")
        assert response.status_code == 200
        assert len(response.json) == 2


class TestDeleteData:
    def test_delete_data_success(self, client):
        client.post("/data", json={"name": "to_delete"})
        response = client.delete("/data/1")
        assert response.status_code == 200
        assert response.json["message"] == "Data deleted successfully"

    def test_delete_data_not_found(self, client):
        response = client.delete("/data/999")
        assert response.status_code == 404
        assert response.json["message"] == "Data not found"