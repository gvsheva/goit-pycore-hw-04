from decimal import Decimal
from pathlib import Path


def total_salary(path: Path):
    total, nlines = Decimal("0"), 0
    with path.open() as f:
        for line in f:
            try:
                *_, salary = line.split(",")
                total += Decimal(salary.strip())
                nlines += 1
            except ValueError:
                continue
    if nlines == 0:
        return total, Decimal("0")
    return total, total / nlines
