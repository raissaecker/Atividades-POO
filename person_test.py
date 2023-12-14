import pytest 

from person import Person, InvalidPhoneError, InvalidNameError

def test_person_creation ():
    person = Person("Raissa Ecker", "+55 42 9 9999-9999")

    assert person.name == "Raissa Ecker"
    assert person.phone == "+55 42 9 9999-9999"

def test_invalid_name():
    with pytest.raises(InvalidNameError):
        Person("Raissa", "+55 42 9 9999-9999")

def test_invalid_phone():
    with pytest.raises(InvalidPhoneError):
        Person("Raissa Ecker", "+55 42 9 9999-9999")

def test_valid_updates():
    person = Person("Raissa Ecker", "+55 42 9 9999-9999")
    person.name = "Raissa Teste"
    person.phone = "+55 42 9 9999-9999"

    assert person.name == "Raissa Teste"
    assert person.phone == "+55 42 9 9999-9999"

def test_str_method():
    person = Person("Raissa Ecker", "+55 42 9 9999-9999")

    assert person.__str__() == "Nome: Raissa Ecker | Telefone: +55 42 9 9999-9999"