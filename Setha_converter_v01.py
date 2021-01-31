import PySimpleGUI as sg
import os.path
from moviepy.editor import *
import glob
import sys
from PIL import Image, ImageTk
import io





def get_img_data(f, maxsize=(1200, 850), first=False):
    """Generate image data using PIL
    """
    img = Image.open(f)
    img.thumbnail(maxsize)
    if first:                     # tkinter is inactive the first time
        bio = io.BytesIO()
        img.save(bio, format="PNG")
        del img
        return bio.getvalue()
    return ImageTk.PhotoImage(img)


sg.ChangeLookAndFeel('DarkRed1')

# ------ Menu Definition ------ #
menu_def = []
           

# ------ Column Definition ------ #
column1 = [[sg.Text('Column 1', background_color='lightblue', justification='center', size=(10, 1))],
           [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 1')],
           [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2')],
           [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3')]]

layout = [
    [sg.Menu(menu_def, tearoff=True)],
    
    [sg.Text('SETHA video to mp3 converter', size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
    
      [sg.Image(filename=r'logo.png', size=(200,200))],
      
    
    
    [sg.Input(key='_FILES_'), sg.FilesBrowse()],
    [sg.Text('_' * 80)],
    
    [sg.Submit(tooltip='Click to submit this form'), sg.Cancel()]]

window = sg.Window('SETHA video to mp3 converter', layout, default_element_size=(40, 1), grab_anywhere=False,icon=r'logo_icon.ico')
event, values = window.read()
window.close()


list_val = list(values.values())

print(list_val[1])



my_string = list_val[1] 

result = [x.strip() for x in my_string.split(';')] 
print (len(result))



for x in range(len(result)):
    
        
    video = VideoFileClip(result[x])
    path2 =  result[x] +".mp3"
    video.audio.write_audiofile(os.path.join(result[x],path2 ))

