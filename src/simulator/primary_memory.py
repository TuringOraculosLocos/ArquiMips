
# Universidad Nacional Autónoma de México
# Facultad de Ciencias
# Arquitectura de Computadoras
# [Proyecto] Máquina Virtual
# Nombre: Erick Ivan Perez Jimenez
# No.Cuenta: 311042122

# Reference: https://refactoring.guru/es/design-patterns/singleton/python/example

class SingletonMeta(type):
    """https://refactoring.guru/es/design-patterns/singleton/python/example"""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class MIPSMemory(metaclass=SingletonMeta):
    def read(self, registry):
        pass

    def write(self, registry, payload):
        pass