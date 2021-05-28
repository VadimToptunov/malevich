import AvantGuard
import random
import Tech
import termcolor


def runner(width, height):
    try:
        boolean = [True, False]
        AvantGuard.generate_image(width, height, random.choice(boolean), random.choice(boolean), random.choice(boolean),
                                  random.choice(boolean), random.choice(boolean))
    except KeyboardInterrupt:
        print(termcolor.colored("Closing program.", "green"))


if __name__ == "__main__":
    image_n = int(input("How many images do you need? "))
    width = int(input("Set width: "))
    height = int(input("Set height: "))
    for i in range(image_n):
        runner(width, height)
    print(termcolor.colored("All pictures are created!", "red"))
