from data_management import Data
from calculator import get_received_snr


def print_help():
    print("\n\tCOMMANDS\n\n"
          "LOAD file [slot]\t> load new input file [optionally at given slot, else at new slot]\n"
          "RUN [slot]\t\t> run all slots or given slot\n"
          "SHOW [slot]\t\t> show all slots or given slot, their value id's and values\n"
          "CHANGE slot id value\t> changes the value of the given id of the given slot\n"
          "MOVE old_slot new_slot\t> moves the old slot to the new slot\n"
          "COPY old_slot new_slot\t> copies the old slot to the new slot\n"
          "NAME slot name\t\t> change the name of a slot\n"          
          "CLEAR [slot]\t\t> clear all slots or given slot\n"
          "EXIT\t\t\t> exit the program\n"
          "HELP\t\t\t> show commands\n")


data_slots = []

print("\nLink Budget Tool\nADSEE2 Group 22")

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
            try:
                while len(data_slots) < int(command[2]):
                    data_slots.append(None)
                data_slots[int(command[2])-1] = data
                print(f'File loaded at slot {data_slots.index(data) + 1}')
            except ValueError:
                print("ERROR: slot should be integer.")

    elif command[0].upper() == 'SHOW':
        if len(command) == 1:
            for data_slot_i, data_slot in enumerate(data_slots):
                if data_slot is not None:
                    print("\nData slot " + str(data_slot_i + 1) + ": " + data_slot.name)
                    data_slot.print_values()
        if len(command) == 2:
            try:
                print("Data slot " + command[1] + ": " + data_slots[int(command[1])-1].name)
                data_slots[int(command[1]) - 1].print_values()
            except IndexError:
                print("Slot does not exist yet.")
            except ValueError:
                print("ERROR: slot should be integer.")

    elif command[0].upper() == 'CHANGE':
        if len(command) == 4:
            try:
                values = data_slots[int(command[1]) - 1].get_values()
                values[int(command[2]) - 1] = float(command[3])
                data_slots[int(command[1]) - 1].set_values(values)
                print("New values for data slot " + command[1] + ": " + data_slots[int(command[1])-1].name)
                data_slots[int(command[1]) - 1].print_values()
            except IndexError:
                print("Slot or ID does not exist.")
            except ValueError:
                print("ERROR: slot should be integer.")
        else:
            print("Please fill in a slot, id and new value.")

    elif command[0].upper() == 'MOVE':
        if len(command) == 3:
            try:
                while len(data_slots) < int(command[2]):
                    data_slots.append(None)
                data_slots[int(command[2]) - 1] = data_slots[int(command[1]) - 1]
                data_slots[int(command[1]) - 1] = None
            except ValueError:
                print("ERROR: slot should be integer.")
        else:
            print("Please fill in an old and new slot.")

    elif command[0].upper() == 'COPY':
        if len(command) == 3:
            try:
                while len(data_slots) < int(command[2]):
                    data_slots.append(None)
                data_slots[int(command[2]) - 1] = data_slots[int(command[1]) - 1]
            except ValueError:
                print("ERROR: slot should be integer.")
        else:
            print("Please fill in an old and new slot.")

    elif command[0].upper() == 'NAME':
        if len(command) >= 3:
            try:
                if data_slots[int(command[1])-1] is None:
                    raise IndexError
                name = ' '.join(command[2:(len(command))])
                data_slots[int(command[1])-1].name = name
                print(f"changed name of slot {command[1]} to {data_slots[int(command[1])-1].name}")
            except IndexError:
                print("Slot does not exist yet.")
            except ValueError:
                print("ERROR: slot should be integer.")
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
            except ValueError:
                print("ERROR: slot should be integer.")

    elif command[0].upper() == 'CLEAR':
        if len(command) == 1:
            data_slots = []
            calculation_slots = []
            print("All slots cleared")
        elif len(command) == 2:
            try:
                data_slots[int(command[1])-1] = None
                print(f"Slot {command[1]} cleared")
            except ValueError:
                print("ERROR: slot should be integer.")

    elif command[0].upper() == 'EXIT':
        print("Exiting, Goodbye!")
        raise SystemExit

    elif command[0].upper() == 'HELP':
        print_help()
    else:
        print("ERROR: Command not found")

