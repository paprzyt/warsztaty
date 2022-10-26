import argparse

def main(val: int):
    print(f"Value: {val}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='My program')
    parser.add_argument("value", type=int, help="Value to print")
    args = parser.parse_args()
    main(args.value)
