def work_dict(d, *keys, default=None):
    obj = d
    for key in keys:
        obj = obj.get(key, default)
    return obj


def discard_paths(d, *paths, default=None):
    return [discard(d, path, default) for path in paths]


def discard(d, key, default=None):
    tk = key.split('/', 1)
    if len(tk) == 1:
        return d.pop(tk[0], default)
    else:
        return discard(d[tk[0]], tk[1])

