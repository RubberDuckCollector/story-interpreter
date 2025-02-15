import sys
import time
from html.parser import HTMLParser


class SpeedTagException(Exception):
    pass


class PauseTagException(Exception):
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


    def handle_starttag(self, tag, attrs):
        if tag == "speed":
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
        elif tag == "pause":
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


    def handle_data(self, data):
        if self.collect_data == "speed":
            slow_print(data, self.speed)


    def handle_endtag(self, tag):
        if tag == "speed":
            self.collect_data = ""
            self.speed = None


def main():
    parser = storyParser()
    parser.feed("<speed val=0.1>Hello world!</speed><pause val=1><speed val=0>Test</speed>")


if __name__ == "__main__":
    main()
