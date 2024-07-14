
if __name__ == "__main__":
    import argparse
    from pathlib import Path

    from task1 import total_salary

    ap = argparse.ArgumentParser()
    ap.add_argument("path", type=Path, help="Path to the file")
    args = ap.parse_args()
    total, average = total_salary(args.path)
    print(f"Total: {total}, Average: {average}")
