import pathlib
import gc
from mne import find_events, Epochs,set_eeg_reference
from mne.io import read_raw_bdf
from mne.channels import make_standard_montage
from numpy import genfromtxt, arange

events_dict0 = {'r_pinch' : 2, 'r_stop' : 4, 'r_left' : 8, 'r_right': 16,
    'pause': 128, 'left' : 130, 'work' : 131, 'right': 134, 'rest' : 255}
events_dict = {'r_pinch' : 2, 'r_stop' : 4, 'left' : 130, 'right': 134, 'rest' : 255}


channels_dict = {}
channels_types = {}
ch_array = genfromtxt('../../preprocessing/ch_dic.csv', delimiter=',', dtype='unicode')

for ch in range(0,64):
    channels_dict[ch_array[0,ch]] = ch_array[1,ch]
    channels_types[ch_array[1,ch]] = 'eeg'

for ch in range(1,9):
    channels_types['EXG'+str(ch)] = 'eog'

montage = make_standard_montage('biosemi64')

def get_channel_types():
    return channels_types

def load_raw_to_epochs(file, filter_line=False):
    dir = pathlib.Path().resolve()
    raw = read_raw_bdf(str(dir)+'/'+file, preload=filter_line)
    raw.drop_channels(['GSR1','GSR2','Erg1','Erg2','Resp','Plet','Temp'])
    raw.rename_channels(channels_dict)
    #raw.set_channel_types(channels_types)
    raw.set_montage(montage, on_missing='warn')
    if filter_line :
        raw = raw.notch_filter(arange(50,251,50), n_jobs=8)
    events = find_events(raw,stim_channel='Status')
    epochs = Epochs(raw,events,tmin=-2,tmax=8, baseline=None)
    epochs.load_data()
    epochs.resample(sfreq=1024, n_jobs=8)
    epochs.event_id = events_dict
    epochs = epochs['left','right','rest','r_pinch','r_stop']
    epochs.save('raw_epo.fif', overwrite=True)
    print(epochs)
    del epochs
    del raw
    gc.collect()
    print('saved')
