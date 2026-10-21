from app import greet

def test_greet():
    assert greet() == "Hello from Jenkins CI!"
    print("All tests passed!")

if __name__ == "__main__":
    test_greet()
