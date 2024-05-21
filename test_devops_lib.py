from devops_lib.random_fruit import fruit


def test_fruit():
    fruit_choice = fruit()
    assert fruit_choice in ["apple", "cheery", "banana", "strawberry"]
