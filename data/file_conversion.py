import py_midicsv as pm
import csv

def convert_to_csv(converting_file):
    csv_string = pm.midi_to_csv(converting_file + '.mid')
    with open(converting_file + '.csv', 'w', newline='') as csv_file:
        for line in csv_string:
            csv_file.write(line)


def convert_to_midi(converting_file):
    with open(converting_file + '.csv', newline='') as revert_file:
        midi_object = pm.csv_to_midi(revert_file)

    with open("example_converted.mid", "wb") as midi_file:
        midi_writer = pm.FileWriter(midi_file)
        midi_writer.write(midi_object)
