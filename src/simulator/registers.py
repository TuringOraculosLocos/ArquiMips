# Universidad Nacional Autónoma de México
# Facultad de Ciencias
# Arquitectura de Computadoras
# [Proyecto] Máquina Virtual
# Nombre: Erick Ivan Perez Jimenez
# No.Cuenta: 311042122


REGISTER_LENGTH_NUM = 14
EMPTY_WORD = [ b'\x00' for _ in range (4)]

class MIPSRegister(object):
    def __init__(self) -> None:
        super().__init__()
        self.__mips_bytes = [ EMPTY_WORD for _ in range(REGISTER_LENGTH_NUM)] 
