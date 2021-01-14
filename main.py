import random

def stack_boxes(height, length, width):


def main():
    n, fr, to = 20, 1, 200
    height = [random.randint(fr,to) for _ in range(n)]
    length = [random.randint(fr, to) for _ in range(n)]
    width = [random.randint(fr, to) for _ in range(n)]

    stack_boxes(height, length, width)

    n = 30
    height = [random.randint(fr,to) for _ in range(n)]
    length = [random.randint(fr, to) for _ in range(n)]
    width = [random.randint(fr, to) for _ in range(n)]

    stack_boxes(height, length, width)

if __name__ == "__main__":
    main()