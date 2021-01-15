import random


def stack_boxes(length, width, height):
    boxes = list(zip(length, width, height))

    # sort the boxes in descending order of area(L x W)
    boxes.sort(key=lambda x: x[0] * x[1], reverse=True)

    # max_height[i] stores the maximum possible height when i'th box is on the top
    max_height = [[], []]

    max_height[0] = [0] * len(boxes)
    max_height[1] = [[]] * len(boxes)
    # fill max_height in bottom-up manner
    for i in range(len(boxes)):
        for j in range(i):
            # dimensions of the lower box are each strictly larger than those
            # of the higher box
            if (boxes[i][0] < boxes[j][0] and
                    boxes[i][1] < boxes[j][1]):
                max_height[0][i] = max(max_height[0][i], max_height[0][j])

        max_height[0][i] += boxes[i][0]
        max_height[1][i].append(boxes[i])

    # return the maximum value in max_height
    max_index = max_height[0].index(max(max_height[0]))
    max_stack = max_height[1][max_index]
    print("boxes stack is:")
    for box in max_stack:
        print(box)
    return max(max_height[0])


def main():
    n, fr, to = 20, 1, 200
    print("amount of boxes: ", n)
    height = [random.randint(fr, to) for _ in range(n)]
    length = [random.randint(fr, to) for _ in range(n)]
    width = [random.randint(fr, to) for _ in range(n)]

    print("The maximum height is ", stack_boxes(height, length, width))

    n = 30
    print("amount of boxes: ", n)
    height = [random.randint(fr, to) for _ in range(n)]
    length = [random.randint(fr, to) for _ in range(n)]
    width = [random.randint(fr, to) for _ in range(n)]

    print("The maximum height is ", stack_boxes(height, length, width))


if __name__ == "__main__":
    main()