from data_management import Data
from calculator import get_received_snr


def print_help():
    print("\n\tCOMMANDS\n\n"
          "LOAD file [slot] > load new input file [optionally at given slot, else at new slot]\n"
          "RUN [slot] > run all slots or given slot\n"
          "SHOW [slot] > show all slots or given slot\n"
          "NAME slot name > change the name of a slot\n"          
          "CLEAR [slot] > clear all slots or given slot\n"
          "EXIT > exit the program\n"
          "HELP > show commands\n")


data_slots = []
calculation_slots = []

print("\nLink Budget Tool\nADSEEII Group 22")

print_help()

while True:
    command = input("> ")
    command = command.split()
    # print("command: " + str(command))

    if command[0].upper() == 'LOAD':
        if len(command) == 1:
            print('Please enter a file!')
        data = Data()
        if data.load_data(command[1]) is None:
            pass
        elif len(command) == 2:
            data_slots.append(data)
            print(f'File loaded at slot {data_slots.index(data)+1}')
        elif len(command) == 3:
            while len(data_slots) < int(command[2]):
                data_slots.append(None)
            data_slots[int(command[2])-1] = data
            print(f'File loaded at slot {data_slots.index(data) + 1}')

    elif command[0].upper() == 'SHOW':
        if len(command) == 1:
            for data_slot_i, data_slot in enumerate(data_slots):
                if data_slot is not None:
                    print("Data slot " + str(data_slot_i + 1) + ": " + data_slot.name)
                    data_slot.print_values()
        if len(command) == 2:
            try:
                print("Data slot " + command[1] + ": " + data_slots[int(command[1])-1].name)
                data_slots[int(command[1]) - 1].print_values()
            except IndexError:
                print("Slot does not exist yet")

    elif command[0].upper() == 'NAME':
        if len(command) == 3:
            try:
                if data_slots[int(command[1])-1] is None:
                    raise IndexError
                data_slots[int(command[1])-1].name = command[2]
                print(f"changed name of slot {command[1]} to {data_slots[int(command[1])-1].name}")
            except IndexError:
                print("Slot does not exist yet")
        else:
            print("Please fill in a slot and a new name.")

    elif command[0].upper() == 'RUN':
        if len(command) == 1:
            for data_slot_i, data_slot in enumerate(data_slots):
                if data_slot is not None:
                    data_slot.output = get_received_snr(data_slot)
                    print(f"Data slot {str(data_slot_i + 1)}, {data_slot.name}\n\tReceived SNR: {str(data_slot.output):4.4} [dB]\n\tRequired SNR:"
                          f" {str(data_slot.required_snr):4.4} [dB]\n\tMargin: {str(data_slot.output - data_slot.required_snr):4.4} [dB]")
        elif len(command) == 2:
            try:
                if data_slots[int(command[1])-1] is not None:
                    data_slots[int(command[1])-1].output = get_received_snr(data_slots[int(command[1])-1])
                    print(f"Data slot {command[1]}, {data_slots[int(command[1])-1].name}\n\tReceived SNR:"
                          f" {str(data_slots[int(command[1])-1].output):4.4} [dB]\n\tRequired SNR:"
                          f" {str(data_slots[int(command[1])-1].required_snr):4.4} [dB]\n\tMargin: {str(data_slots[int(command[1])-1].output - data_slots[int(command[1])-1].required_snr):4.4} [dB]")
            except IndexError:
                print("Slot does not exist yet")

    elif command[0].upper() == 'CLEAR':
        if len(command) == 1:
            data_slots = []
            calculation_slots = []
            print("All slots cleared")
        elif len(command) == 2:
            data_slots[int(command[1])-1] = None
            print(f"Slot {command[1]} cleared")

    elif command[0].upper() == 'EXIT':
        print("Exiting, Goodbye!")
        raise SystemExit

    elif command[0].upper() == 'HELP':
        print_help()
    else:
        print("ERROR: Command not found")

