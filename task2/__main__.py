
if __name__ == "__main__":
    import argparse
    from pathlib import Path

    from task2 import iter_cats_info

    ap = argparse.ArgumentParser()
    ap.add_argument("path", type=Path, help="Path to the file")
    args = ap.parse_args()
    cats = iter_cats_info(args.path)
    for cat in cats:
        print(f"{cat['id']}: {cat['name']} is {cat['age']} years old")
