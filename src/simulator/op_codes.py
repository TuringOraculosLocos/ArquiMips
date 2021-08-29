def mips__add():
    """MIPS Suma entera (con signo)"""
    return 3
def mips__sub():
    """Diferencia Entera (con signo)"""
    return 4
def mips__mul():
    """Producto Entero (con signo)"""
    return 10
def mips__div():
    """Cociente Entero (con signo)"""
    return 11
def mips__fadd():
    """Suma flotante"""
    return 4
def mips__fsub():
    """Diferencia flotante"""
    return 5
def mips__fmul():
    """Producto flotante"""
    return 9
def mips__fdiv():
    """Cociente flotante"""
    return 10
def mips__and():
    """Operador de bits AND"""
    return 1
def mips__or():
    """Operador de bits OR"""
    return 1
def mips__xor():
    """Operador de XOR"""
    return 1
def mips__not():
    """Operador de bits NOT"""
    return 1
def mips__lb():
    """Cargar Byte"""
    return 500
def mips__lw():
    """Cargar palabra (4 bytes)"""
    return 1500
def mips__sb():
    """Guardar byte"""
    return 700
def mips__sw():
    """Guardar palabra (4 bytes)"""
    return 2100
def mips__li():
    """Cargar valor constante"""
    return 1500
def mips__b():
    """Salto condicional"""
    return 1
def mips__beqz():
    """Salto si es igual a cero"""
    return 4
def mips__bltz():
    """Salto si es menor a cero"""
    return 5
def mips__syscall():
    """llamada al sistema"""
    return 50

MIPSOpCodes = {
    b'\x00' : mips__add,
    b'\x01' : mips__sub,
    b'\x02' : mips__mul,
    b'\x03' : mips__div,
    b'\x04' : mips__fadd,
    b'\x05' : mips__fsub,
    b'\x06' : mips__fmul,
    b'\x07' : mips__fdiv,
    b'\x08' : mips__and,
    b'\t' : mips__or,
    b'\n' : mips__xor,
    b'\x0b' : mips__not,
    b'\x0c' : mips__lb,
    b'\r' : mips__lw,
    b'\x0e' : mips__sb,
    b'\x0f' : mips__sw,
    b'\x10' : mips__li,
    b'\x11' : mips__b,
    b'\x12' : mips__beqz,
    b'\x13' : mips__bltz,
    b'\x14' : mips__syscall,
}


