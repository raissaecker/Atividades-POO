import re

class InvalidNameError(Exception):
    pass

class InvalidPhoneError(Exception):
    pass

class Person:
    """Person representa uma pessoa."""

    def __init__(self, name: str, phone: str):
        self.name = name
        self.phone = phone 

    def __str__(self):
        return f"Nome: {self.__name} | Telefone: {self.__phone}"

    @property
    def name(self):
        """str: nome da pessoa"""
        return self.__name 
    
    @name.setter
    def name(self, name:str):
        if not self.__is_name_valid(name):
            raise InvalidNameError()
        
        self.__name = name

    @property
    def phone(self):
        """str: número de telefone"""
        return self.__phone
    
    @phone.setter
    def phone(self, phone:str):
        if not self.__is_phone_valid(phone):
            raise InvalidPhoneError()
        
        self.__phone = phone


    def __is_name_valid(self, name:str) -> bool:
        """Verifica se um nome é valido (nome completo)
        
        Args:
            name (str): nome que será verificado.

        Returns:
            bool: True caso o nome seja composto, False caso não seja.
        """
        return len(name.strip().split()) > 1
    
    def __is_phone_valid(self, phone: str) -> bool:
        """Verifica se um telefone é valido (+55 47 9 9999-9999)
        
        Args:
            name (str): número de telefone que será verificado.

        Returns:
            bool: True caso o número seja válido, False caso não seja.
        """
        phone_regex = r"\+55\s?(?:\([1-9]{2}\)|[1-9]{2})\s?(?:9\s?\d{4}[-.\s]?\d{4}|\d{4}[-.\s]?\d{4})"
        return re.match(phone_regex, phone)

