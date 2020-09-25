#Link Budget Tool README

## Installation

1. Make sure you have python installed
2. Move all files to a folder
3. Done

## Usage

The program has slots that configurations can be loaded into. These configurations can be defined using data files, like _example.dat_. The
 program look at the order of the variables, so **`do not change the order`**. Comments can be added using the **`#`** symbol, causing the whole line
 to be ignored. These configurations can be run, changed, copied, moved and cleared. A good use would be to load the default configuration, see if
 the budget closes. Then the configuration can be copied to a new slot, some parameters can be changed and a fitting name can be given to this
 configuration. Finally the software can be run again to compare both cases. This process can be iterated until the budget can be closed.

#### Example of usage
1. To start, doubleclick _RUN.BAT_
2. Make a data file, formatted like _example.dat_, in a text editor
2. Put the data file(s) in the same folder as the program
2. Load the data file(s) using the **LOAD** command
3. Run the configurations using the **RUN** command
4. Optionally move, copy or clear cases
5. Change parameters by using the **CHANGE** command
6. Rename configurations using the **NAME** command
7. Show all parameters using the **SHOW** command

#### COMMAND LIST

    LOAD file [slot]        > load new input file [optionally at given slot, else at new slot]
    RUN [slot               > run all slots or given slot
    SHOW [slot]             > show all slots or given slot, their value id's and values
    CHANGE slot id value	> changes the value of the given id of the given slot
    MOVE old_slot new_slot  > moves the old slot to the new slot
    COPY old_slot new_slot	> copies the old slot to the new slot
    NAME slot name          > change the name of a slot
    CLEAR [slot]            > clear all slots or given slot
    EXIT                    > exit the program
    HELP                    > show commands