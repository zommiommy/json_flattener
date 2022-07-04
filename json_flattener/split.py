from typing import Iterator

def split_with_escaping(
    string: str,  
) -> Iterator[str]:
    """Generalized version of `str.split` that accepts generic delimiters, escape sequences, and string."""

    is_single_quote: bool = False
    is_double_quote: bool = False
    inside_single_string: bool = False
    inside_double_string: bool = False
    is_escaped: bool = False # if the current **char** is to consider escaped 
    string_idx:int = 0       # where we are in the string
    current_split_group = "" # where we build the current split, we need this to remove quotes

    while string_idx < len(string):
        # if it's escaped, skip the escape sequence and toggle the is_escaped flag
        is_double_quote = string[string_idx] == '"'
        if not is_escaped and not inside_single_string and is_double_quote:
            inside_double_string ^= True
            string_idx += 1
            continue

        is_single_quote = string[string_idx] == "'"
        if not is_escaped and not inside_double_string and is_single_quote:
            inside_single_string ^= True
            string_idx += 1
            continue

        if not is_escaped and string[string_idx:].startswith("\\"):
            is_escaped ^= True
            string_idx += 1
            continue
        else:
            is_escaped = False

        # if it's escaped or it's not the delimiter, just forward the split
        if is_escaped or inside_single_string or inside_double_string or \
            not string[string_idx] in ".:":
            current_split_group += string[string_idx]
            string_idx += 1
        elif string[string_idx] == ".":
            # It's a non escaped delimiter!
            yield current_split_group
            current_split_group = ""
            # skip the delimiter in the next capture
            string_idx += 1
        elif string[string_idx] == ":":
            yield current_split_group
            yield string[string_idx + 1:]
            return
        else:
            raise ValueError("Unreachable!")