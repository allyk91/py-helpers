import yaml
import os


def get_config():
    print("Hello from py-helpers!")


def merge_config(*config_files):
    d = {}
    for f in config_files:
        try:
            with open(f) as config:
                c = yaml.safe_load(config)
                d = d | c
        except:
            print("Fail to load config")
    return d

def test():
    print("testing!")


if __name__ == "__main__":
    d1 = {"a": 1, "b": 3}
    d2 = {"c": 3, "b": 4}
    d3 = {"a": 5, "d": 6}

    c1 = os.path.join(os.getcwd(), "config.yml")
    c2 = os.path.join(os.getcwd(), "global_config.yml")
    c3 = os.path.join(os.getcwd(), "workload.yml")
    print(c2)
    new_d = merge_config(c1, c2, c3)
    # new_d = c2 | c3 | c1
    print(new_d)
