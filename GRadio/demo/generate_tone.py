# Demo: (Dropdown, Slider, Textbox) -> (Audio)

import gradio as gr
import numpy as np

notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]


def generate_tone(note, octave, duration):
    sr = 48000
    a4_freq, tones_from_a4 = 440, 12 * (octave - 4) + (note - 9)
    frequency = a4_freq * 2 ** (tones_from_a4 / 12)
    duration = int(duration)
    audio = np.linspace(0, duration, duration * sr)
    audio = (20000 * np.sin(audio * (2 * np.pi * frequency))).astype(np.int16)
    return sr, audio


iface = gr.Interface(
    generate_tone, 
    [
        gr.inputs.Dropdown(notes, type="index"),
        gr.inputs.Slider(4, 6, step=1),
        gr.inputs.Textbox(type="number", default=1, label="Duration in seconds")
    ], "audio")

iface.test_launch()
if __name__ == "__main__":
    iface.launch()
