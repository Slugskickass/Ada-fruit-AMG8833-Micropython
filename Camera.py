import machine
from micropython import const

i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
_PIXEL_OFFSET = const(0x80)
_PIXEL_TEMP_CONVERSION = .25
_PIXEL_ARRAY_WIDTH = const(8)
_PIXEL_ARRAY_HEIGHT = const(8)

retbuf = [[0 ] *_PIXEL_ARRAY_WIDTH for _ in range(_PIXEL_ARRAY_HEIGHT)]


def get_array():
    for I in range(8):
        for J in range(8):
            i = I * _PIXEL_ARRAY_HEIGHT + J
            out = i2c.readfrom_mem(105, _PIXEL_OFFSET + (i << 1), 2)
            raw = (out[1] << 8) | out[0]
            abs_val = (raw & 0x7FF)
            retbuf[I][J] = (float(abs_val)*.25)
    return(retbuf)