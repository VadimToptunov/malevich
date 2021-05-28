import AvantGuard
import MulticolorPatch
import random
import termcolor


def runner():
    try:
        image_n = int(input("How many images do you need? "))
        width = int(input("Set width: "))
        height = int(input("Set height: "))
        boolean = [True, False]
        random_function_list = [MulticolorPatch.create_image(width, height),
                                AvantGuard.generate_image(width, height, random.choice(boolean),
                                                          random.choice(boolean), random.choice(boolean),
                                                          random.choice(boolean))]
        for i in range(image_n):
            random.choice(random_function_list)
    except KeyboardInterrupt:
        print(termcolor.colored("Closing program.", "green"))
    print(termcolor.colored("All pictures are created!", "red"))


if __name__ == "__main__":
    runner()
