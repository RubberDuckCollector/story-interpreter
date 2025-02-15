import sys
import time
import pprint
import textwrap
# import my_modules.colors
from html.parser import HTMLParser

colors = {
    "reset": "\033[0m",
    "red": "\033[031m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[96m",
    "lightGray": "\033[37m",
    "darkGray": "\033[90m",
    "lightRed": "\033[91m",
    "lightGreen": "\033[92m",
    "lightYellow": "\033[93m",
    "lightBlue": "\033[94m",
    "lightMagenta": "\033[95m",
    "lightCyan": "\033[96m",
    "white": "\033[97m",
    "warn": "\033[93m",
    "underline": "\033[4m",
    "bold": "\033[1m",
    "hidden": "\033[8m",
    "blink": "\033[5m",
    "dim": "\033[2m",
    "reverse": "\033[7m",
}


class SpeedTagException(Exception):
    pass


class PauseTagException(Exception):
    pass


class ColorTagException(Exception):
    pass


def slow_print(msg: str, interval):
    interval = float(interval) if not isinstance(interval, int|float) else interval # may come in as a string, so must cast to float
    for i in msg:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(interval)  # if this is 0, it writes the characters instantly as the wait time is 0


class storyParser(HTMLParser):  # inherits from HTMLParser class

    def __init__(self):
        super().__init__()  # override the original __init__() and add my own attributes visible to every method
        self.speed = None  # will either be a float or None
        self.collect_data = ""  # empty string means don't collect data, but is a string to accomodate for different tags
        self.color = ""


    def handle_starttag(self, tag, attrs):
        if tag == "speed":  # sets speed of typing in-between the speed tags
            # print(attrs)  # DEBUG
            # `attrs` is a list of tuples of attribues in a tag.
                # e.g: <speed val=5> -> [('val', '5')]
            # `attr_name` is the [0] index of the tuple, `value` is the [1] index of the tuple
            for attr_name, value in attrs:
                if attr_name == "val":
                    if value is None:  # check if `val` is present
                        raise SpeedTagException("Speed tag value is missing.")
                    value = float(value)
                    if value < 0.0:
                        raise SpeedTagException("Speed tag value is negative. It must be 0, 0.0, or a positive number.")
                    # if we're in a speed tag and the attribute is called `val`, set the speed
                    # also raise flag that data coming up should be handled as inside `speed` tags.
                    self.speed = value
                    self.collect_data = "speed"
        elif tag == "pause":  # pauses typing for a specified duration
            # print(attrs)  # DEBUG
            for attr_name, value in attrs:
                if attr_name == "val":
                    if value is None:  # check if `val` is present
                        raise PauseTagException("Pause tag value is missing.")
                    value = float(value)
                    if value <= 0:
                        raise PauseTagException("Pause tag value is 0.0 or less. It must be a positive number.")
                    # made it past the checks, free to implement the pause tag's functionality now
                    time.sleep(value)
        elif tag == "br":
            sys.stdout.write('\n')
            sys.stdout.flush()
        elif tag == "color":
            for attr_name, value in attrs:
                if attr_name == "val":
                    if value is None:  # check if `val` is present
                        raise ColorTagException("Color tag has no value.")
                    # if not hasattr(Color, value):  # if the data at `value` is not found in the `Color` class:
                    try:
                        # if not colors[value]:  # if the data at `value` is not found in the `Color` class:
                        #     raise ColorTagException(f"Color '{value}' is not a valid color. Valid colors: {colors.items()}")
                        # retrieve the actual string in the color class at the `value` name
                        # self.color = getattr(Color, value, Color.Reset)
                        self.color = colors[value]
                    except KeyError:
                        raise ColorTagException(f"Color '{value}' is not a valid color. Valid colors: {colors.keys()}")


    def handle_data(self, data):
        if self.collect_data == "speed":
            data = textwrap.dedent(data)
            print(f"{self.color}", end='', flush=True)
            slow_print(data, self.speed)
            print(f"{colors['reset']}", end='', flush=True)


    def handle_endtag(self, tag):
        if tag == "speed":
            self.collect_data = ""
            self.speed = None


def interpret_file(filename: str):
    with open(filename, "r") as f:
        # print(f.read())
        parser = storyParser()
        parser.feed(f.read())


def main():
    parser = storyParser()
    # parser.feed("<speed val=0.1>Hello world!</speed><br><pause val=1><speed val=0>Test</speed>")
    interpret_file("stories/example_yuri.html")
    # interpret_file("stories/test.html")


if __name__ == "__main__":
    main()
