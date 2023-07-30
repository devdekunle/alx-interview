#!/usr/bin/python3
def validUTF8(data):
    """
    Function to check if a byte is a valid continuation byte (starts with '10')
    """
    def is_continuation(byte):
        """
        check byte continuation
        """
        return (byte >> 6) == 2

    # Iterate through the list of integers (bytes)
    i = 0
    while i < len(data):
        byte = data[i]

        # Check for 1-byte character (0xxxxxxx)
        if byte >> 7 == 0:
            i += 1
        # Check for 2-byte character (110xxxxx 10xxxxxx)
        elif byte >> 5 == 6:
            if i + 1 < len(data) and is_continuation(data[i + 1]):
                i += 2
            else:
                return False
        # Check for 3-byte character (1110xxxx 10xxxxxx 10xxxxxx)
        elif byte >> 4 == 14:
            if i + 2 < len(data):
                if is_continuation(data[i + 1]):
                    if is_continuation(data[i + 2]):
                        i += 3
                    else:
                        return False
                else:
                    return False
            else:
                return False
        # Check for 4-byte character (11110xxx 10xxxxxx 10xxxxxx 10xxxxxx)
        elif byte >> 3 == 30:
            if i + 3 < len(data):
                if is_continuation(data[i + 1]):
                    if is_continuation(data[i + 2]):
                        if is_continuation(data[i + 3]):
                            i += 4
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    return True
