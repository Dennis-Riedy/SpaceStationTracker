import tkintermapview as tmp
import tkinter as tk
import spaceStationData

from mpl_toolkits.basemap import Basemap

NAME = 'International Space Station'

window = tk.Tk()
window.title('Internation Space Station Tracker')


current_location = tk.Button(text='Current Location')


latitude_display = tk.Label(text='Latitude: {0}'.format(spaceStationData.get_latitude()))
longitude_display = tk.Label(text='Longtitude: {0}'.format(spaceStationData.get_longitude()))

mapLabel = tk.LabelFrame()
mapLabel.pack(pady=20)

mapWidget = tmp.TkinterMapView(mapLabel, width=800, height=800, corner_radius=0)
mapWidget.set_zoom(0)
mapWidget.set_marker(spaceStationData.get_latitude(), spaceStationData.get_longitude(), text=NAME)
mapWidget.pack()

refresh = tk.Button(text='Refresh')

current_location.pack()
latitude_display.pack()
longitude_display.pack()
refresh.pack()






window.mainloop()

