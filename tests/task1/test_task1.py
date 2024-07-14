from decimal import Decimal

from pytest import fixture

from task1 import total_salary


@fixture
def srcfile(tmp_path):
    p = tmp_path / "srcfile.txt"
    with p.open("w") as f:
        print("Golden Hook,1300", file=f)
        print("Wicked Wench,1104", file=f)
        print("Firebeard Finn,1233", file=f)
        print("Lightning Liz,1675", file=f)
        print("Phantom Pete,1888", file=f)
        print("Salty Sam,1194", file=f)
        print("Swashbuckler Sue,1740", file=f)
        print("Thunderous Thor,1850", file=f)
        print("Wench Wanda,1930", file=f)
        print("Scurvy Steve,1337", file=f)
    return p


def test_total_salary(srcfile):
    total, average = total_salary(srcfile)
    assert total == Decimal("15251")
    assert average == Decimal("1525.1")
