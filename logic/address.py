from pydantic import BaseModel
from typing import Optional


class Address(BaseModel):
    """
    Class to represent an address.

    Attributes:
        street (str): Street name.
        number (int): Address number.
        apartment (int): Apartment number.
        postal_code (int): Postal code.
        locality (str): City or locality.
        department (str): Department or state.
        country (str): Country.

    Methods:
        __str__(): Returns a string representation of the address.
        __eq__(other): Compares two addresses to check if they are equal.
    """

    street: str
    number: int
    apartment: Optional[str]
    postal_code: int
    locality: str
    department: str
    country: str

    def __str__(self):
        """
        Returns a string representation of the address.
        """
        apartment_str = str(self.apartment) if self.apartment is not None else "None"

        return '({0}, {1}, {2}, {3}, {4}, {5}, {6})'.format(
            self.street, self.number, apartment_str,
            self.postal_code, self.locality, self.department,
            self.country
        )

    def __eq__(self, other):
        """
        Compares two addresses to check if they are equal.

        Args:
            other (Address): Another address to compare.

        Returns:
            bool: True if the addresses are equal, False otherwise.
        """
        if isinstance(other, Address):
            return (self.street == other.street and self.number == other.number and
                    self.apartment == other.apartment and
                    self.postal_code == other.postal_code and self.locality == other.locality and
                    self.department == other.department and self.country == other.country)
        else:
            return False
