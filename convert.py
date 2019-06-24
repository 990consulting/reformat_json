def convert(json_in: dict) -> dict:
    parent_dict, local_dict = _convert(json_in, "")
    return local_dict


def _convert(json_in: dict, parent: str) -> (dict, dict):
    parent_dict = {}
    local_dict = dict(json_in)

    if type(json_in) == dict:
        for key in json_in:
            if type(json_in[key]) == str:
                if key.startswith("@"):
                    parent_dict[parent + key] = json_in[key]
                    del local_dict[key]
                elif key == "_":
                    parent_dict[parent] = json_in[key]
                    del local_dict[key]
            elif type(json_in[key]) == dict:
                _parent_dict, _local_dict = _convert(json_in[key], key)
                if _local_dict:
                    local_dict[key] = _local_dict
                else:
                    del local_dict[key]
                local_dict.update(_parent_dict)
            elif type(json_in[key]) == list:
                ret_list = []
                for el in json_in[key]:
                    _, _local_dict = _convert(el, "")
                    ret_list.append(_local_dict)
                local_dict[key] = ret_list

    return parent_dict, local_dict



