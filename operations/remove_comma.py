def remove_trailing_commas(string):
    if string.endswith(","):
        string = string.rstrip(",")
    return string