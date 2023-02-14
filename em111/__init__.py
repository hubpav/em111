import click
from pymodbus.client import ModbusSerialClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder


def read_int16(mb, address):
    result = mb.read_input_registers(address=address, count=1, slave=1)
    decoder = BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=Endian.Big, wordorder=Endian.Little)
    return decoder.decode_16bit_int()

def read_int32(mb: ModbusSerialClient, address):
    result = mb.read_input_registers(address=address, count=2, slave=1)
    decoder = BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=Endian.Big, wordorder=Endian.Little)
    return decoder.decode_32bit_int()

@click.command()
@click.option('--port', required=True, prompt='PORT', help='Serial port.')
def main(port):
    mb = ModbusSerialClient(port=port, baudrate=9600, bytesize=8, parity='N', stopbits=1)
    mb.connect()

    voltage = read_int32(mb, 0x0) / 10
    current = read_int32(mb, 0x2) / 1000
    power = read_int32(mb, 0x4) / 10
    power_factor = read_int16(mb, 0xe) / 1000
    frequency = read_int16(mb, 0xf) / 10
    total_power_import = read_int32(mb, 0x10) / 10
    total_power_export = read_int32(mb, 0x20) / 10

    print('Voltage:', voltage, 'V')
    print('Current:', current, 'A')
    print('Power:', power, 'W')
    print('Power factor:', power_factor)
    print('Frequency:', frequency, 'Hz')
    print('Total power import:', total_power_import, 'kWh')
    print('Total power export:', total_power_export, 'kWh')
