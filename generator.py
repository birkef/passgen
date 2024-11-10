from typing import List

import string
import secrets


class Generator:
    def __init__(
            self,
            password_length: int = 16,
            lower_registry: bool = True,
            upper_registry: bool = True,
            digits: bool = True,
            special_symbols: bool = True
    ) -> None:
        if password_length < 8:
            raise ValueError("The password length must be greater than or equal to 8.")
        elif password_length > 24:
            raise ValueError("The password length must be less than or equal to 24.")

        self.password_length = password_length
        self.lower_registry = lower_registry
        self.upper_registry = upper_registry
        self.digits = digits
        self.special_symbols = special_symbols

    def set_password_length(self, password_length: int) -> None:
        self.password_length = password_length

    def set_lower_registry_enabled(self, value: bool) -> None:
        self.lower_registry = value

    def set_upper_registry_enabled(self, value: bool) -> None:
        self.upper_registry = value

    def set_digits_enabled(self, value: bool) -> None:
        self.digits = value

    def set_special_symbols_enabled(self, value: bool) -> None:
        self.special_symbols = value

    def new_password(self) -> str:
        return self.generate(
            1,
            self.password_length,
            self.lower_registry,
            self.upper_registry,
            self.digits,
            self.special_symbols
        )[0]

    def new_password_array(self, password_count: int) -> List[str]:
        return self.generate(
            password_count,
            self.password_length,
            self.lower_registry,
            self.upper_registry,
            self.digits,
            self.special_symbols
        )

    @staticmethod
    def generate(
            passwords_count: int = 1,
            password_length: int = 16,
            lower_registry: bool = True,
            upper_registry: bool = True,
            digits: bool = True,
            special_symbols: bool = True
    ) -> list:
        passwords: list = []
        password_symbols: str = ""

        if passwords_count < 1:
            raise ValueError("The password count must be greater than or equal to 1.")
        elif passwords_count > 16:
            raise ValueError("The password count must be less than or equal to 16.")

        if password_length < 8:
            raise ValueError("The password length must be greater than or equal to 8.")
        elif password_length > 24:
            raise ValueError("The password length must be less than or equal to 24.")

        if lower_registry:
            password_symbols += string.ascii_lowercase

        if upper_registry:
            password_symbols += string.ascii_uppercase

        if digits:
            password_symbols += string.digits

        if special_symbols:
            password_symbols += string.punctuation

        if password_symbols == "":
            raise ValueError("Choose at least one type of symbol.")

        for _ in range(passwords_count):
            password: str = "".join(
                [secrets.choice(password_symbols) for _ in range(password_length)]
            )
            passwords.append(password)

        return passwords
