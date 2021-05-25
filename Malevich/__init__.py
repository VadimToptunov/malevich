import AvantGuard
import MulticolorPatch
import random


def runner():
    image_n = int(input("How many images do you need? "))
    width = int(input("Set width: "))
    height = int(input("Set height: "))
    random_function_list = [MulticolorPatch.create_image(image_n, width, height),
                            AvantGuard.generate_with_lines(image_n, width, height),
                            AvantGuard.generate_without_lines(image_n, width, height)]
    random.choice(random_function_list)


if __name__ == "__main__":
    runner()
