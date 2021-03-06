from data_input import *
from plot_spectrograms import *
import convolutional_neural_networks

'''
main.py obsługuje całą funkcjonalność aplikacji

fs - częstotliwość próbkowaina
samples - numpy array z próbkami typu float32
file_name - nazwa pliku

@@@ przy wybraniu opcji record zatrzymujemy za pomocą CTRL+C @@@

'''


fs, samples, file_name, file_path = data_input()  # wybieramy plik który chcemy przeanalizować
spectrogram(fs, samples, file_name)  # plotuje i zapisuje do .png spektrogram
mel_spectrogram(fs, samples, file_name)  # plotuje i zapisuje do .png spektrogram melowy
name = convolutional_neural_networks.print_prediction(f'{file_path}/{file_name}')