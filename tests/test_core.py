from laser_model import compute


def test_compute():
    assert compute(["a", "bc", "abc"]) == "abc"


if __name__ == "__main__":
    test_compute()
