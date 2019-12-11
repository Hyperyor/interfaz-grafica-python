import wx

#pylint: disable=maybe-no-member

class PanelVisualizar(wx.Panel):
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id)
        
        self.inicializar()

    def inicializar(self):

        vbox = wx.BoxSizer(wx.VERTICAL)

        vbox.Add((-1, 25))

        #nombre panel--------------------------------------------
        hboxNom = wx.BoxSizer(wx.HORIZONTAL)

        labNombre = wx.StaticText(self, label='Listado de videojuegos')
        hboxNom.Add(labNombre, flag=wx.RIGHT, border=8)

        vbox.Add(hboxNom, flag=wx.ALIGN_CENTER,  border = 10)

        vbox.Add((-1, 25))

        #titulo--------------------------------------------
        hboxTitulo = wx.BoxSizer(wx.HORIZONTAL)

        labTit = wx.StaticText(self, label='Titulo:                     ')
        #labTit.SetFont(font)
        hboxTitulo.Add(labTit, flag=wx.RIGHT, border=8)

        textTitulo = wx.TextCtrl(self)

        #para que no se pueda modificar
        #textTitulo.DoEnable(False)

        hboxTitulo.Add(textTitulo, proportion=1)

        vbox.Add(hboxTitulo, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP,  border = 10)

        vbox.Add((-1, 25))

        #anio publicacion--------------------------------------------
        hboxPubli = wx.BoxSizer(wx.HORIZONTAL)

        labPub = wx.StaticText(self, label='Anio publicacion: ')
        #labTit.SetFont(font)
        hboxPubli.Add(labPub, flag=wx.RIGHT, border=8)

        textPubli = wx.TextCtrl(self)

        hboxPubli.Add(textPubli, proportion=1)

        vbox.Add(hboxPubli, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP,  border = 10)

        vbox.Add((-1, 25))

        #precio--------------------------------------------
        hboxPrecio = wx.BoxSizer(wx.HORIZONTAL)

        labPre = wx.StaticText(self, label='Precio:                    ')
        #labTit.SetFont(font)
        hboxPrecio.Add(labPre, flag=wx.RIGHT, border=8)

        textPre = wx.TextCtrl(self)

        hboxPrecio.Add(textPre, proportion=1)

        vbox.Add(hboxPrecio, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP,  border = 10)

        vbox.Add((-1, 25))

        #botones--------------------------------------------
        hboxBotones = wx.BoxSizer(wx.HORIZONTAL)

        btn1 = wx.Button(self, label='Anterior', size = (70,30))
        hboxBotones.Add(btn1)
        btn2 = wx.Button(self, label='Siguiente', size = (70,30))
        hboxBotones.Add(btn2)

        vbox.Add(hboxBotones, flag=wx.ALIGN_CENTER|wx.BOTTOM,  border = 10)

        self.SetSizer(vbox)

class PanelAlta(wx.Panel):
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id)
        
        self.inicializar()

    def inicializar(self):

        vbox = wx.BoxSizer(wx.VERTICAL)

        vbox.Add((-1, 25))

        #nombre panel--------------------------------------------
        hboxNom = wx.BoxSizer(wx.HORIZONTAL)

        labNombre = wx.StaticText(self, label='Alta de videojuego')
        hboxNom.Add(labNombre, flag=wx.RIGHT, border=8)

        vbox.Add(hboxNom, flag=wx.ALIGN_CENTER,  border = 10)

        vbox.Add((-1, 25))

        #titulo--------------------------------------------
        hboxTitulo = wx.BoxSizer(wx.HORIZONTAL)

        labTit = wx.StaticText(self, label='Titulo:                     ')
        #labTit.SetFont(font)
        hboxTitulo.Add(labTit, flag=wx.RIGHT, border=8)

        textTitulo = wx.TextCtrl(self)

        #para que no se pueda modificar
        #textTitulo.DoEnable(False)

        hboxTitulo.Add(textTitulo, proportion=1)

        vbox.Add(hboxTitulo, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP,  border = 10)

        vbox.Add((-1, 25))

        #anio publicacion--------------------------------------------
        hboxPubli = wx.BoxSizer(wx.HORIZONTAL)

        labPub = wx.StaticText(self, label='Anio publicacion: ')
        #labTit.SetFont(font)
        hboxPubli.Add(labPub, flag=wx.RIGHT, border=8)

        textPubli = wx.TextCtrl(self)

        hboxPubli.Add(textPubli, proportion=1)

        vbox.Add(hboxPubli, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP,  border = 10)

        vbox.Add((-1, 25))

        #precio--------------------------------------------
        hboxPrecio = wx.BoxSizer(wx.HORIZONTAL)

        labPre = wx.StaticText(self, label='Precio:                    ')
        #labTit.SetFont(font)
        hboxPrecio.Add(labPre, flag=wx.RIGHT, border=8)

        textPre = wx.TextCtrl(self)

        hboxPrecio.Add(textPre, proportion=1)

        vbox.Add(hboxPrecio, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP,  border = 10)

        vbox.Add((-1, 25))

        #botones--------------------------------------------
        hboxBotones = wx.BoxSizer(wx.HORIZONTAL)

        btn1 = wx.Button(self, label='Aceptar', size = (70,30))
        hboxBotones.Add(btn1)
        btn2 = wx.Button(self, label='Cancelar', size = (70,30))
        hboxBotones.Add(btn2)

        vbox.Add(hboxBotones, flag=wx.ALIGN_CENTER|wx.BOTTOM,  border = 10)

        self.SetSizer(vbox)

class PanelBienvenida(wx.Panel):
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id)
        
        self.inicializar()

    def inicializar(self):

        vbox = wx.BoxSizer(wx.VERTICAL)

        vbox.Add((-1, 25))
        vbox.Add((-1, 25))
        vbox.Add((-1, 25))
        vbox.Add((-1, 25))
        #mensaje bienvenida--------------------------------------------
        hboxNom = wx.BoxSizer(wx.HORIZONTAL)

        labNombre = wx.StaticText(self, label='BIENVENIDO')
        hboxNom.Add(labNombre, flag=wx.RIGHT, border=8)

        vbox.Add(hboxNom, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.CENTER,  border = 10)

        vbox.Add((-1, 25))
        vbox.Add((-1, 25))
        vbox.Add((-1, 25))
        vbox.Add((-1, 25))
        vbox.Add((-1, 25))

        #autor--------------------------------------------
        hboxNom = wx.BoxSizer(wx.HORIZONTAL)

        labNombre = wx.StaticText(self, label='Autor: Jose Luis Bernal Navarrete 2019')
        hboxNom.Add(labNombre, flag=wx.RIGHT, border=8)

        vbox.Add(hboxNom, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.BOTTOM,  border = 10)

        vbox.Add((-1, 25))

        self.SetSizer(vbox)

class FramePrincipal(wx.Frame):
    def __init__(self, parent, title):
        # asegurar que se llame al __init__ de los padres
        super(FramePrincipal, self).__init__(parent, title=title,
                                        size=(450,400))
        self.Initialize()

    def Initialize(self):
        
        #creamos la barra del menu
        self.CreateMenuBar()
        self.CreatePanels()

        #colocamos el icono a la ventana
        self.icono = wx.Icon()
        self.icono.CopyFromBitmap(wx.Bitmap("icono.png", wx.BITMAP_TYPE_ANY))
        self.SetIcon(self.icono)

        #centramos en la pantalla
        self.Centre(True)
        self.Show()

    def CreatePanels(self):
        
        self.caja = wx.BoxSizer(wx.VERTICAL)

        #creamos el panel visualizar
        self.panelVisualizar = PanelVisualizar(self, -1)
        #self.CreatePanelVisualizar()

        self.panelAlta = PanelAlta(self, -1)

        self.panelBienvenida = PanelBienvenida(self, -1)

        #añadimos los paneles al frame principal
        self.caja.Add(self.panelVisualizar, 1, wx.EXPAND)
        self.caja.Add(self.panelAlta, 1, wx.EXPAND)
        self.caja.Add(self.panelBienvenida, 1, wx.EXPAND)

        #ocultar paneles y mostrar el que toque
        self.panelVisualizar.Hide()
        self.panelAlta.Hide()
        self.SetSizer(self.caja)
        self.Layout()

    def CreateMenuBar(self):
         #creamos un elemento menu para cargar/guardar archivos y salir
        self.menuArchivo = wx.Menu()

        self.menuArchivo.Append(-1, "Cargar Datos")

        self.menuArchivo.Append(2, "Guardar datos")

        self.menuArchivo.AppendSeparator()

        itemSalir = self.menuArchivo.Append(wx.ID_EXIT)

        #menu de botones para los paneles
        self.menuPaneles = wx.Menu()

        itemVisualizar = self.menuPaneles.Append(1, "Visualizar juegos")

        itemAlta = self.menuPaneles.Append(2, "Nuevo juego")

        #creamos el menu como tal y le añadimos los submenus
        barraDeMenu = wx.MenuBar()
        barraDeMenu.Append(self.menuArchivo, "Archivo")
        barraDeMenu.Append(self.menuPaneles, "Opciones")

        #deshabilitamos los botones que requieren que tengamos cargado un fichero
        self.menuPaneles.Enable(1, False)
        self.menuPaneles.Enable(2, False)

        self.menuArchivo.Enable(2, False)

        # asignamos la barra de menu al frame
        self.SetMenuBar(barraDeMenu)
        
        #asociamos elemento del menu a una accion del sistema
        self.Bind(wx.EVT_MENU, self.OnSalir,  itemSalir)
        self.Bind(wx.EVT_MENU, self.OnVisualizar,  itemVisualizar)
        self.Bind(wx.EVT_MENU, self.OnAlta,  itemAlta)

    #metodoque se llama al presionar el boton salir del menu
    def OnSalir(self, event):
        self.Close(True)
    
    def OnVisualizar(self, event):
        self.panelVisualizar.Show()
        self.panelAlta.Hide()
        self.panelBienvenida.Hide()
        self.Layout()
        
    def OnAlta(self, event):
        self.panelAlta.Show()
        self.panelVisualizar.Hide()
        self.panelBienvenida.Hide()
        self.Layout()

if __name__ == '__main__':
    # Cuando este modulo se ejecuta (no se importa), crear la aplicacion,
    # el frame, mostrarlo e iniciar el bucle de eventos.
    app = wx.App()
    frm = FramePrincipal(None, title='Gestion de videojuegos')
    frm.Show()
    app.MainLoop()