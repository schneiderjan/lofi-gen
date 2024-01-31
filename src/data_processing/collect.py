import os, glob
from pathlib import Path
import music21
from music21 import converter, instrument, note, chord
import subprocess
from pydub import AudioSegment
import pickle

def extract_notes(file):
    notes = []
    pick = None
    for j in file:
        songs = instrument.partitionByInstrument(j)
        for part in songs.parts:
            pick = part.recurse()
            for element in pick:
                if isinstance(element, note.Note):
                    notes.append(str(element.pitch))
                elif isinstance(element, chord.Chord):
                    notes.append(".".join(str(n) for n in element.normalOrder))

    return notes

def store_mp3(midi_fp):
    # Define paths for temporary and output files
    temp_wav_file = "temp_output.wav"
    output_audio_file = "sample.mp3"

    # Convert the MIDI score to a WAV file using FluidSynth
    fs_cmd = [
        "fluidsynth",
        "-ni",  # Use the default SoundFont
        "-r", "44100",  # Sample rate (adjust as needed)
        "-T", "wav",  # Output format
        "-F", temp_wav_file,  # Output file path
        "path/to/your/soundfont.sf2",  # Path to your SoundFont file
        midi_fp,  # Input MIDI file
    ]
    subprocess.run(fs_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    audio = AudioSegment.from_wav(temp_wav_file)
    audio.export(output_audio_file, format="mp3")

    # Clean up temporary WAV file
    subprocess.run(["rm", temp_wav_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(f"Audio saved as {output_audio_file}")

if __name__ == "__main__":
    mid_fps = glob.glob(os.path.join(Path.cwd(), "data", "lofi_midi", "*mid"))
    print(f"Found {len(mid_fps)} mid files.")

    store_mp3(mid_fps[1]) # store a sample mp3 file

    parsed_midis = [converter.parse(midi) for midi in mid_fps]
    corpus = extract_notes(parsed_midis)
    # Pickle the corpus and save it to disk
    with open(os.path.join(Path.cwd(), "data", "corpus", "corpus.pkl"), "wb") as file:
        pickle.dump(corpus, file)
    print("Corpus saved as corpus.pkl")
