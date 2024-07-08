import customtkinter
import tkintermapview
import space_station_data as ssd


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

main_window = customtkinter.CTk()
main_window.title('International Space Station Tracker')
main_window.geometry("1000x540")

mapLabel = customtkinter.CTkFrame(main_window)
mapWidget = tkintermapview.TkinterMapView(width=400, height=400, corner_radius=0)
mapWidget.set_zoom(0)

iss_marker = mapWidget.set_marker(ssd.get_latitude(), 
                                  ssd.get_longitude(),
                                  text='International Space Station')


lon = customtkinter.CTkLabel(main_window,text='Longitude')
lat = customtkinter.CTkLabel(main_window,text='Latitude')
refresh = customtkinter.CTkButton(main_window, text='Refresh')

weather_frame = customtkinter.CTkFrame(main_window)
weather_status = customtkinter.CTkLabel(weather_frame, text='STATUS')
weather_location = customtkinter.CTkLabel(weather_frame, text='Location')

weather_frame.pack()
weather_location.pack()
weather_status.pack()


mapWidget.pack()
lon.pack()
lat.pack()
refresh.pack()

main_window.mainloop()
