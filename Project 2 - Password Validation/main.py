"""
This module implements the password validation exercise of the Section 14 of the course.
"""

import re


def validate_password():
    # Password to validate
    password = "Felix123"

    # Compile the pattern:
    # · At least 8 char long
    # · Contain any sort letters, numbers or $%#@
    # · Has to end with a number
    pattern = re.compile("([A-Za-z0-9$%#@]{7,}[0-9])")

    # Check the password
    check = pattern.fullmatch(password)

    # Print the results
    print(f"Validated => {check is not None}")


# Entry point of the script
if __name__ == '__main__':
    # Call the validate password function
    validate_password()
