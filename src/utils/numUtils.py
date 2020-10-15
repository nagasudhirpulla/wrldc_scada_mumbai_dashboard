def sumWithNone(*args):
    args = [a for a in args if not a is None]
    return sum(args) if args else None 