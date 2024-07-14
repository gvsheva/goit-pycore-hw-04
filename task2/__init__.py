from pathlib import Path
from typing import Iterator, TypedDict


class CatInfo(TypedDict):
    id: str
    name: str
    age: int


def iter_cats_info(path: Path) -> Iterator[CatInfo]:
    cats: list[CatInfo] = []
    with path.open() as f:
        for line in f:
            try:
                id, name, age = line.split(",")
                yield {
                    "id": id.strip(),
                    "name": name.strip(),
                    "age": int(age.strip()),
                }
            except ValueError:
                continue
    return cats


def get_cats_info(path: Path):
    return list(iter_cats_info(path))
