import yaml


def get_config():
    print("Hello from py-helpers!")


def merge_dicts(*dicts):
    d = {}
    for dict in dicts:
        for key in dict:
            try:
                d[key] = dict[key]
            except KeyError:
                print(f"unable to update {key} in {dict}")
    return d


def test():
    print("testing!")


if __name__ == "__main__":
    d1 = {"a": 1, "b": 3}
    d2 = {"c": 3, "b": 4}
    d3 = {"a": 5, "d": 6}

    try:
        with open("config.yml") as config:
            c1 = yaml.safe_load(config)
    except:
        print("Fail to load config")

    try:
        with open("global_config.yml") as config:
            c2 = yaml.safe_load(config)
    except:
        print("Fail to load config")

    try:
        with open("workload.yml") as config:
            c3 = yaml.safe_load(config)
    except:
        print("Fail to load config")

    # print(c1)
    # print(c2)
    # new_d = merge_dicts(c2, c3, c1)
    new_d = c2 | c3 | c1
    print(new_d)
