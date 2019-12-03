import gdal
import tkinter as tk
import tkinter.filedialog
import re
from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
from tkMessageBox import *

#Articulo
#Tasseled cap transformation for assessing hurricane landfall impact on a coastal watershed
#Autores
#Chandan Mostafiz, Ni-Bin Chang⁎
#Department of Civil, Environmental and Construction Engineering, University of Central Florida, 4000 Central Florida Blvd., Orlando, FL, 32816, USA
#Doi
#https://doi.org/10.1016/j.jag.2018.08.015
#Agoritmo basado en la metodología usada por el autor en la (Figura 4) Fig. 4. análisis de teledetección realizado para el TCT

#interfaz basica


aplicacion = tk.Tk()
aplicacion.geometry("630x400")

title = 'Tasscap y correcciones'
back = tk.Frame(master=aplicacion)
back.master.title(title)

back.pack_propagate(0) 

back.pack(fill=tk.BOTH, expand=1) 
# label title
aplicacion.titulolbl = tk.Label(master=back, text="tasseled cap Y Correcciones", anchor="center", font=(30))
aplicacion.titulolbl.place(x=200, y=20)



# function for  para datos
def open_file():   
    archivo = tk.filedialog.askopenfile() 
    global tiff 
    tiff = archivo
    b = banda_cbb.get()
    #text.insert('1.0', b + " - " + tiff_name + "\n") 
    text.delete('1.0', END)
    text.config(state=NORMAL)

    if (b == "Banda 1"):
        global b1
        b1 = tiff
        global b1_file
        b1_file = gdal.Open(b1.name)
        global b1_geotransform
        b1_geotransform = b1_file.GetGeoTransform()
        global b1_projection 
        b1_projection = b1_file.GetProjection()
        global b1_band
        b1_band = b1_file.GetRasterBand(1)
        global b1_xsize
        b1_xsize = b1_band.XSize
        global b1_ysize
        b1_ysize = b1_band.YSize
        global b1_array
        b1_array = b1_band.ReadAsArray()
        b1_file = None 
        b1_band = None 
        print(b1.name)
        info = b1.name
        text.delete('1.0', END)
        text.insert('1.0', info + "\n")
    elif (b == "Banda 2"):
        global b2
        b2 = tiff
        b2_file = gdal.Open(b2.name)
        global b2_geotransform
        b2_geotransform = b2_file.GetGeoTransform()
        global b2_projection 
        b2_projection = b2_file.GetProjection()
        global b2_band
        b2_band = b2_file.GetRasterBand(1)
        global b2_xsize
        b2_xsize = b2_band.XSize
        global b2_ysize
        b2_ysize = b2_band.YSize
        global b2_array
        b2_array = b2_band.ReadAsArray()
        b2_file = None 
        b2_band = None         
        print(b2.name)
        print("Banda 2")
        info = b2.name
        text.delete('1.0', END)
        text.insert('1.0', info + "\n")
    elif (b == "Banda 3"):
        global b3
        b3 = tiff
        b3_file = gdal.Open(b3.name)
        global b3_geotransform
        b3_geotransform = b3_file.GetGeoTransform()
        global b3_projection 
        b3_projection = b3_file.GetProjection()
        global b3_band
        b3_band = b3_file.GetRasterBand(1)
        global b3_xsize
        b3_xsize = b3_band.XSize
        global b3_ysize
        b3_ysize = b3_band.YSize
        global b3_array
        b3_array = b3_band.ReadAsArray()
        b3_file = None 
        b3_band = None 
        print(b3.name)
        print("Banda 3")
        info = b3.name
        text.delete('1.0', END)
        text.insert('1.0', info + "\n")
    elif (b == "Banda 4"):
        global b4
        b4 = tiff
        b4_file = gdal.Open(b4.name)
        global b4_geotransform
        b4_geotransform = b4_file.GetGeoTransform()
        global b4_projection 
        b4_projection = b4_file.GetProjection()
        global b4_band
        b4_band = b4_file.GetRasterBand(1)
        global b4_xsize
        b4_xsize = b4_band.XSize
        global b4_ysize
        b4_ysize = b4_band.YSize
        global b4_array
        b4_array = b4_band.ReadAsArray()
        b4_file = None 
        b4_band = None 
        print(b4.name)
        print("Banda 4")
        info = b4.name
        text.delete('1.0', END)
        text.insert('1.0', info + "\n")
    elif (b == "Banda 5"):
        global b5
        b5 = tiff
        b5_file = gdal.Open(b5.name)
        global b5_geotransform
        b5_geotransform = b5_file.GetGeoTransform()
        global b5_projection 
        b5_projection = b5_file.GetProjection()
        global b5_band
        b5_band = b5_file.GetRasterBand(1)
        global b5_xsize
        b5_xsize = b5_band.XSize
        global b5_ysize
        b5_ysize = b5_band.YSize
        global b5_array
        b5_array = b5_band.ReadAsArray()
        b5_file = None 
        b5_band = None 
        print(b5.name)
        print("Banda 5")
        info = b5.name
        text.delete('1.0', END)
        text.insert('1.0', info + "\n")
    elif (b == "Banda 6"):
        global b6
        b6 = tiff
        b6_file = gdal.Open(b6.name)
        global b6_geotransform
        b6_geotransform = b6_file.GetGeoTransform()
        global b6_projection 
        b6_projection = b6_file.GetProjection()
        global b6_band
        b6_band = b6_file.GetRasterBand(1)
        global b6_xsize
        b6_xsize = b6_band.XSize
        global b6_ysize
        b6_ysize = b6_band.YSize
        global b6_array
        b6_array = b6_band.ReadAsArray()
        b6_file = None 
        b6_band = None 
        print(b6.name)
        print("Banda 6")
        info = b6.name
        text.delete('1.0', END)
        text.insert('1.0', info + "\n")
    elif (b == "metadatos"):
        global metadatos
        metadatos = tiff
        metadatos_file = open(metadatos.name,'r')
        
        # = Es el factor multiplicativo de escalado especifico por banda obtenido del metadato para b1
        with open(metadatos.name) as fp:
            line = fp.readlines()
            print line[187]
        line1=(line[187])
        global REFLECTANCE_MULT_BAND_1
        REFLECTANCE_MULT_BAND_1=float(line1[30:])
        print REFLECTANCE_MULT_BAND_1
        
        # = Es el factor multiplicativo de escalado especifico por banda obtenido del metadato para b2
        with open(metadatos.name) as fp:
            line = fp.readlines()
            print line[188]
        line1=(line[188])
        global REFLECTANCE_MULT_BAND_2
        REFLECTANCE_MULT_BAND_2=float(line1[30:])
        print REFLECTANCE_MULT_BAND_2
    
        # = Es el factor multiplicativo de escalado especifico por banda obtenido del metadato para b3
        with open(metadatos.name) as fp:
            line = fp.readlines()
            print line[189]
        line1=(line[189])
        global REFLECTANCE_MULT_BAND_3
        REFLECTANCE_MULT_BAND_3=float(line1[30:])
        print REFLECTANCE_MULT_BAND_3
    
        # = Es el factor multiplicativo de escalado especifico por banda obtenido del metadato para b4
        with open(metadatos.name) as fp:
            line = fp.readlines()
            print line[190]
        line1=(line[190])
        global REFLECTANCE_MULT_BAND_4
        REFLECTANCE_MULT_BAND_4=float(line1[30:])
        print REFLECTANCE_MULT_BAND_4

        # = Es el factor multiplicativo de escalado especifico por banda obtenido del metadato para b5
        with open(metadatos.name) as fp:
            line = fp.readlines()
            print line[191]
        line1=(line[191])
        global REFLECTANCE_MULT_BAND_5
        REFLECTANCE_MULT_BAND_5=float(line1[30:])
        print REFLECTANCE_MULT_BAND_5

        # = Es el factor multiplicativo de escalado especifico por banda obtenido del metadato para b5
        with open(metadatos.name) as fp:
            line = fp.readlines()
            print line[192]
        line1=(line[192])
        global REFLECTANCE_MULT_BAND_6
        REFLECTANCE_MULT_BAND_6=float(line1[30:])
        print REFLECTANCE_MULT_BAND_6
        
        # = Es el factor aditivo de escalado especifico por banda obtenido del metadato
        with open(metadatos.name) as fp:
            line = fp.readlines()
            print line[196]
        line1=(line[196])
        global REFLECTANCE_ADD_BAND_1
        REFLECTANCE_ADD_BAND_1=float(line1[29:])
        print REFLECTANCE_ADD_BAND_1

        # = Es el factor aditivo de escalado especifico por banda obtenido del metadato
        with open(metadatos.name) as fp:
            line = fp.readlines()
            print line[197]
        line1=(line[197])
        global REFLECTANCE_ADD_BAND_2
        REFLECTANCE_ADD_BAND_2=float(line1[29:])
        print REFLECTANCE_ADD_BAND_2

        # = Es el factor aditivo de escalado especifico por banda obtenido del metadato
        with open(metadatos.name) as fp:
            line = fp.readlines()
            print line[198]
        line1=(line[198])
        global REFLECTANCE_ADD_BAND_3
        REFLECTANCE_ADD_BAND_3=float(line1[29:])
        print REFLECTANCE_ADD_BAND_3

        # = Es el factor aditivo de escalado especifico por banda obtenido del metadato
        with open(metadatos.name) as fp:
            line = fp.readlines()
            print line[199]
        line1=(line[199])
        global REFLECTANCE_ADD_BAND_4
        REFLECTANCE_ADD_BAND_4=float(line1[29:])
        print REFLECTANCE_ADD_BAND_4

        # = Es el factor aditivo de escalado especifico por banda obtenido del metadato       
        with open(metadatos.name) as fp:
            line = fp.readlines()
            print line[200]
        line1=(line[200])
        global REFLECTANCE_ADD_BAND_5
        REFLECTANCE_ADD_BAND_5=float(line1[29:])
        print REFLECTANCE_ADD_BAND_5

        # = Es el factor aditivo de escalado especifico por banda obtenido del metadato
        with open(metadatos.name) as fp:
            line = fp.readlines()
            print line[201]
        line1=(line[201])
        global REFLECTANCE_ADD_BAND_6
        REFLECTANCE_ADD_BAND_6=float(line1[29:])
        print REFLECTANCE_ADD_BAND_6
             
        info = (metadatos.name)
        text.delete('1.0', END)
        text.insert('1.0', info + "\n")

showinfo('Cómo usar','Solo para Landsat 8, primero Selecionar las 6 bandas a Usar y el metadato de las Imagenes, luego se calculan las corecciones y finalmente el Tasseled cap, la reproyeccióna UTM 17N incluida ')

# function for corr_btn
def correcciones_function():
    
    # de nuemeros digitales a reflectancia TOA B1
    # fuente: Descripción y Corrección de Productos Landsat 8 LDCM  (Landsat Data Continuity Mission) IGAC  2013

    reflectancia_b1=(REFLECTANCE_MULT_BAND_1*b1_array+REFLECTANCE_ADD_BAND_1)

    
    #Corrección por DOS1
    correccion= reflectancia_b1[reflectancia_b1>0].min() - reflectancia_b1

    
    # guardado de la imagen
    output_raster_name=('banda1_corregida.tif')
    driver = gdal.GetDriverByName('GTiff')
    new_tiff = driver.Create(output_raster_name,b1_xsize,b1_ysize,1,gdal.GDT_Int16)
    new_tiff.SetGeoTransform(b1_geotransform)
    new_tiff.SetProjection(b1_projection)
    new_tiff.GetRasterBand(1).WriteArray(correccion)
    new_tiff.FlushCache() 
    new_tiff = None 

    # de nuemeros digitales a reflectancia TOA B2
    reflectancia_b2=(REFLECTANCE_MULT_BAND_2*b2_array+REFLECTANCE_ADD_BAND_2)
    
    #Corrección por DOS1
    correccion2= reflectancia_b2[reflectancia_b2 != 0].min() - reflectancia_b2
    
    # guardado de la imagen
    output_raster_name=('banda2_corregida.tif')
    driver = gdal.GetDriverByName('GTiff')
    new_tiff = driver.Create(output_raster_name,b1_xsize,b1_ysize,1,gdal.GDT_Int16)
    new_tiff.SetGeoTransform(b1_geotransform)
    new_tiff.SetProjection(b1_projection)
    new_tiff.GetRasterBand(1).WriteArray(correccion2)
    new_tiff.FlushCache() 
    new_tiff = None 

    # de nuemeros digitales a reflectancia TOA B3
    reflectancia_b3=(REFLECTANCE_MULT_BAND_3*b3_array+REFLECTANCE_ADD_BAND_3)
    
    #Corrección por DOS1
    correccion3= reflectancia_b3[reflectancia_b3 != 0].min() - reflectancia_b3
    
    # guardado de la imagen
    output_raster_name=('banda3_corregida.tif')
    driver = gdal.GetDriverByName('GTiff')
    new_tiff = driver.Create(output_raster_name,b1_xsize,b1_ysize,1,gdal.GDT_Int16)
    new_tiff.SetGeoTransform(b1_geotransform)
    new_tiff.SetProjection(b1_projection)
    new_tiff.GetRasterBand(1).WriteArray(correccion3)
    new_tiff.FlushCache() 
    new_tiff = None 
    
    # de nuemeros digitales a reflectancia TOA B4
    reflectancia_b4=(REFLECTANCE_MULT_BAND_4*b4_array+REFLECTANCE_ADD_BAND_4)
    #Corrección por DOS1
    correccion4= reflectancia_b4[reflectancia_b4 != 0].min() - reflectancia_b4
    
    # guardado de la imagen
    output_raster_name=('banda4_corregida.tif')
    driver = gdal.GetDriverByName('GTiff')
    new_tiff = driver.Create(output_raster_name,b1_xsize,b1_ysize,1,gdal.GDT_Int16)
    new_tiff.SetGeoTransform(b1_geotransform)
    new_tiff.SetProjection(b1_projection)
    new_tiff.GetRasterBand(1).WriteArray(correccion4)
    new_tiff.FlushCache() 
    new_tiff = None

    # de nuemeros digitales a reflectancia TOA B5
    reflectancia_b5=(REFLECTANCE_MULT_BAND_5*b5_array+REFLECTANCE_ADD_BAND_5)
    
    #Corrección por DOS1
    correccion5= reflectancia_b5[reflectancia_b5 != 0].min() - reflectancia_b5
    
    # guardado de la imagen
    output_raster_name=('banda5_corregida.tif')
    driver = gdal.GetDriverByName('GTiff')
    new_tiff = driver.Create(output_raster_name,b1_xsize,b1_ysize,1,gdal.GDT_Int16)
    new_tiff.SetGeoTransform(b1_geotransform)
    new_tiff.SetProjection(b1_projection)
    new_tiff.GetRasterBand(1).WriteArray(correccion5)
    new_tiff.FlushCache() 
    new_tiff = None       

    # de nuemeros digitales a reflectancia TOA B6
    reflectancia_b6=(REFLECTANCE_MULT_BAND_6*b6_array+REFLECTANCE_ADD_BAND_6)
    
    #Corrección por DOS1
    correccion6= reflectancia_b6[reflectancia_b6 != 0].min() - reflectancia_b6
    
    # guardado de la imagen
    output_raster_name=('banda6_corregida.tif')
    driver = gdal.GetDriverByName('GTiff')
    new_tiff = driver.Create(output_raster_name,b1_xsize,b1_ysize,1,gdal.GDT_Int16)
    new_tiff.SetGeoTransform(b1_geotransform)
    new_tiff.SetProjection(b1_projection)
    new_tiff.GetRasterBand(1).WriteArray(correccion6)
    new_tiff.FlushCache() 
    new_tiff = None       
    
    tsscd_btn.configure(state=NORMAL)
    showinfo('Información','Imágenes con Corrección Radiométrica y Atmosférica guardadas en el directorio dónde se encuentra el Script ')

# function tasseled cap
def tasseled_function():
    #brillo 
    brillo = correccion*0.3029+correccion2*0.2786+correccion3*0.4733+correccion4*0.5599+correccion5*0.508+correccion6*0.1872
    # guardar brillo 
    output_raster_name_brillo=('Brillo.tif')
    driver = gdal.GetDriverByName('GTiff')
    new_tiff = driver.Create(output_raster_name_brillo,b1_xsize,b1_ysize,1,gdal.GDT_Int16)
    new_tiff.SetGeoTransform(b1_geotransform)
    new_tiff.SetProjection(b1_projection)
    new_tiff.GetRasterBand(1).WriteArray(brillo)
    new_tiff.FlushCache() 
    new_tiff = None 
    
    #verdor
    verdor = correccion*(-0.2941)+correccion2*(-0.243)+correccion3*(-0.5424)+correccion4*0.7276+correccion5*0.0713+correccion6*(-0.1608)
    #guardar verdor 
    output_raster_name_verdor=('verdor.tif')
    driver = gdal.GetDriverByName('GTiff')
    new_tiff = driver.Create(output_raster_name_verdor,b1_xsize,b1_ysize,1,gdal.GDT_Int16)
    new_tiff.SetGeoTransform(b1_geotransform)
    new_tiff.SetProjection(b1_projection)
    new_tiff.GetRasterBand(1).WriteArray(verdor)
    new_tiff.FlushCache() 
    new_tiff = None 
    
    #humedad
    humedad =  correccion*0.1511+correccion2*0.1973+correccion3*0.3283+correccion4*0.3407+correccion5*(-0.7117)+correccion6*(-0.4559)
    #guardar humedad
    output_raster_name_verdor=('Humedad.tif')
    driver = gdal.GetDriverByName('GTiff')
    new_tiff = driver.Create(output_raster_name_verdor,b1_xsize,b1_ysize,1,gdal.GDT_Int16)
    new_tiff.SetGeoTransform(b1_geotransform)
    new_tiff.SetProjection(b1_projection)
    new_tiff.GetRasterBand(1).WriteArray(humedad)
    new_tiff.FlushCache() 
    new_tiff = None
    
    showinfo('Tasseled','Imágenes de brillo verdor y humedad guardadas en el directorio dónde se encuentra el Script ')
    
# function for clear_btn
def clear():
    text.delete('1.0', END)
        
# cbb and button for banda 
banda_cbb = ttk.Combobox(aplicacion, state="readonly")
banda_cbb.place(x=20, y=70)
banda_cbb["values"] = ['Banda 1', 'Banda 2', 'Banda 3', 'Banda 4', 'Banda 5', 'Banda 6', 'metadatos']
banda_cbb.set('Banda 1')

banda_btn = tk.Button(master=back, text="Seleccionar", command=open_file) # command calls the function
banda_btn.pack(side="top")
banda_btn.place(x=190, y=60)

# button calcular correcciones
corr_btn = tk.Button(master=back, text="Calcular correcciones", command=correcciones_function)
corr_btn.pack(side="top")
corr_btn.place(x=300, y=60)

# button calcular tsscd
tsscd_btn = tk.Button(master=back, text="Calcular Tsscd", command=tasseled_function)
tsscd_btn.pack(side="top")
tsscd_btn.place(x=480, y=60)
tsscd_btn.configure(state=DISABLED)

# button clear text box
clear_btn = tk.Button(master=back, text="Limpiar", fg='red', command=clear)
clear_btn.pack(side="top")
clear_btn.place(x=290, y=90)

# text box
text_frame = Frame(aplicacion)
text = tk.Text(text_frame, width = 73, height = 15)
text.pack(side=RIGHT, padx=20, pady=10)
text_frame.pack(side="top")
text_frame.place(y=120)

aplicacion.mainloop()
