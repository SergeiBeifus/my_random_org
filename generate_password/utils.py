import secrets
import string


class PasswordGenerator:
    def __init__(
            self,
            *,
            password_length: int = 8,
            use_special_symbols: bool = False,
            use_lower: bool = False,
            use_upper: bool = False,
            use_numbers: bool = True
    ):
        self.password_length = password_length
        self.symbols_list = (
                use_special_symbols * string.punctuation +
                use_lower * string.ascii_lowercase +
                use_upper * string.ascii_uppercase +
                use_numbers * string.digits
        )

    def generate(self) -> str:
        password = ""
        for i in range(self.password_length):
            password += secrets.choice(self.symbols_list)
        return password
