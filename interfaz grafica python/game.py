import wx

#pylint: disable=maybe-no-member

class FramePrincipal(wx.Frame):
    def __init__(self, parent, title):
        # asegurar que se llame al __init__ de los padres
        super(FramePrincipal, self).__init__(parent, title=title,
                                        size=(450,400))
        self.Initialize()

    def Initialize(self):
        
        #creamos la barra del menu
        self.CreateMenuBar()

        #centramos en la pantalla
        self.Centre(True)
        self.Show()

    def CreateMenuBar(self):
         #creamos un elemento menu para cargar/guardar archivos y salir
        menuArchivo = wx.Menu()

        menuArchivo.Append(-1, "Cargar Datos")

        menuArchivo.Append(-1, "Guardar datos")

        menuArchivo.AppendSeparator()

        itemSalir = menuArchivo.Append(wx.ID_EXIT)

        #creamos el menu como tal y le añadimos los submenus
        barraDeMenu = wx.MenuBar()
        barraDeMenu.Append(menuArchivo, "Archivo")

        # asignamos la barra de menu al frame
        self.SetMenuBar(barraDeMenu)
        
        #asociamos elemento del menu a una accion del sistema
        self.Bind(wx.EVT_MENU, self.OnSalir,  itemSalir)

    #metodoque se llama al presionar el boton salir del menu
    def OnSalir(self, event):
        self.Close(True)

if __name__ == '__main__':
    # Cuando este modulo se ejecuta (no se importa), crear la aplicacion,
    # el frame, mostrarlo e iniciar el bucle de eventos.
    app = wx.App()
    frm = FramePrincipal(None, title='Gestion de videojuegos')
    frm.Show()
    app.MainLoop()