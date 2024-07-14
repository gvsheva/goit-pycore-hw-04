from pytest import fixture

from task2 import get_cats_info


@fixture
def srcfile(tmp_path):
    p = tmp_path / "srcfile.txt"
    with p.open("w") as f:
        print("aaaa1,Whiskers,3", file=f)
        print("aaaa2,Fluffy,5", file=f)
        print("aaaa3,Mr. Tinkles,1", file=f)
        print("aaaa4,Scratchy,2", file=f)
    return p


def test_get_cats_info(srcfile):
    cats = get_cats_info(srcfile)
    assert cats == [
        {"id": "aaaa1", "name": "Whiskers", "age": 3},
        {"id": "aaaa2", "name": "Fluffy", "age": 5},
        {"id": "aaaa3", "name": "Mr. Tinkles", "age": 1},
        {"id": "aaaa4", "name": "Scratchy", "age": 2},
    ]
