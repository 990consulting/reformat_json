import json
from convert import convert

with open("example.json") as i_fh, open("converted.json", "w") as o_fh, open("example_sorted.json", "w") as s_fh:
    example = json.load(i_fh)
    converted = convert(example)
    json.dump(converted, o_fh, indent=2, sort_keys=True)
    json.dump(example, s_fh, indent=2, sort_keys=True)
