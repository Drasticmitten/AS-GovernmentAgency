from pydantic import BaseModel
from logic.address import Address, address1, address2
from logic.case_history import CaseHistory
from logic.education_history import EducationHistory
from logic.fine_history import FineHistory
from logic.medical_history import MedicalHistory
from logic.vehicle_history import VehicleHistory
from logic.natural_entity import NaturalEntity


class Person(NaturalEntity, BaseModel):
    """
     Class used to represent a Person

     Attributes:
            id_entity (int): id_entity of person ( used in the database ).
            type (str): Type id_entity of person.
            dni (int): DNI of person.
            name (str): Name of person.
            last_name (str): Last name of person.
            phone (int): Phone of person.
            address (object): Address of person.
            education_history (object): Educational history of the person.
            fine_history (object): Fine history of the person.
            case_history (object): Case history of the person.
            medical_history (object): Medical history of the person.
            vehicle_history (object): Vehicle history of the person.
            mediator (object): Mediator for managing interactions.

        Methods:
            __str__(): Returns a string representation of a person.
            __eq__(other): Compares two objects person to check if they are equal.
    """
    type_id_entity: str = 'type id_entity'
    dni: int = 0
    name: str = "Name"
    last_name: str = "LastName"
    phone: int = 0
    address: object = Address
    education_history: object = EducationHistory
    fine_history: object = FineHistory
    vehicle_history: object = VehicleHistory
    case_history: object = CaseHistory
    medical_history: object = MedicalHistory
    mediator: object = None

    def __init__(self, mediator=None, **data):
        super().__init__(**data)
        self.mediator = mediator

    def __eq__(self, another_person):
        """ Returns bool of equality of person objects.
        :returns: bool person
        :rtype: bool
        """
        return another_person.dni == self.dni

    def __str__(self):
        """ Returns str of person.
        :returns: string person
        :rtype: str
        """
        return 'id Person: {0}, Type: {1} , Type id: {2}, Dni: {3}, Full name: {4} {5}, Phone: {6}, Address: {7}, ' \
               'Education History: {8}, Fine History: {9}, Vehicle History: {10}, Case History: {11}, ' \
               'Medical History: {12}'.\
            format(self.id_entity, self.type, self.type_id_entity, self.dni, self.name, self.last_name, self.phone,
                   self.address, self.education_history, self.fine_history, self.vehicle_history, self.case_history,
                   self.medical_history)


if __name__ == '__main__':
    # Prueba Person class

    person1 = Person(id_entity=5120167, type_id_entity="C.C", dni=1043638720, name="Julio", last_name="Rodriguez",
                     phone=3154528309, address=address1)
    person2 = Person(id_entity=1247913, type_id_entity="C.C", dni=45761873, name="Luis", last_name="Castro",
                     phone=3214464925, address=address2)

    person1_str = person1.__str__()
    print(f"Person 1 Information \n {person1_str}")
    person2_str = person2.__str__()
    print(f"Person 2 Information \n {person2_str}")

    are_equal_person = person1.__eq__(person2)
    print(f"Are equals ? \n {are_equal_person} \n\n")

person1 = Person(id_entity=5120167, type_id_entity="C.C", dni=1043638720, name="Julio", last_name="Rodriguez",
                 phone=3154528309, address=address1)
person2 = Person(id_entity=1247913, type_id_entity="C.C", dni=45761873, name="Luis", last_name="Castro",
                 phone=3214464925, address=address2)