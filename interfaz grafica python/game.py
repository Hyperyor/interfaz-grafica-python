import wx
import csv

#pylint: disable=maybe-no-member

class PanelVisualizar(wx.Panel):
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id)
        self.ventanaPrincipal = parent
        self.elementoActual = 0
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

        self.textTitulo = wx.TextCtrl(self)

        #para que no se pueda modificar
        #textTitulo.DoEnable(False)

        hboxTitulo.Add(self.textTitulo, proportion=1)

        vbox.Add(hboxTitulo, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP,  border = 10)

        vbox.Add((-1, 25))

        #anio publicacion--------------------------------------------
        hboxPubli = wx.BoxSizer(wx.HORIZONTAL)

        labPub = wx.StaticText(self, label='Anio publicacion: ')
        #labTit.SetFont(font)
        hboxPubli.Add(labPub, flag=wx.RIGHT, border=8)

        self.textPubli = wx.TextCtrl(self)

        hboxPubli.Add(self.textPubli, proportion=1)

        vbox.Add(hboxPubli, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP,  border = 10)

        vbox.Add((-1, 25))

        #precio--------------------------------------------
        hboxPrecio = wx.BoxSizer(wx.HORIZONTAL)

        labPre = wx.StaticText(self, label='Precio:                    ')
        #labTit.SetFont(font)
        hboxPrecio.Add(labPre, flag=wx.RIGHT, border=8)

        self.textPre = wx.TextCtrl(self)

        hboxPrecio.Add(self.textPre, proportion=1)

        vbox.Add(hboxPrecio, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP,  border = 10)

        vbox.Add((-1, 25))

        #botones de modificacion--------------------------------------------

        hboxBotonesM = wx.BoxSizer(wx.HORIZONTAL)

        self.btnBorrar = wx.Button(self, label='Eliminar', size = (70,30))
        hboxBotonesM.Add(self.btnBorrar)

        self.btnModif = wx.Button(self, label='Modificar', size = (70,30))
        hboxBotonesM.Add(self.btnModif)
        

        self.Bind(wx.EVT_BUTTON, self.OnBorrar,  self.btnBorrar)

        self.Bind(wx.EVT_BUTTON, self.OnModificar,  self.btnModif)
        

        vbox.Add(hboxBotonesM, flag=wx.ALIGN_CENTER|wx.BOTTOM,  border = 10)

        vbox.Add((-1, 25))

        #botones--------------------------------------------
        hboxBotones = wx.BoxSizer(wx.HORIZONTAL)

        self.btn1 = wx.Button(self, label='Anterior', size = (70,30))
        hboxBotones.Add(self.btn1)
        self.btn2 = wx.Button(self, label='Siguiente', size = (70,30))
        hboxBotones.Add(self.btn2)

        self.Bind(wx.EVT_BUTTON, self.ShowPreviousElement,  self.btn1)
        self.Bind(wx.EVT_BUTTON, self.ShowNextElement,  self.btn2)

        #self.ControlDeBotones()

        vbox.Add(hboxBotones, flag=wx.ALIGN_CENTER|wx.BOTTOM,  border = 10)

        self.SetSizer(vbox)
    
    def ShowPreviousElement(self, event):
        self.MostrarDatos(self.elementoActual-1)
        self.elementoActual -= 1 
        self.ControlDeBotones()
    def ShowNextElement(self, event):
        self.MostrarDatos(self.elementoActual+1)
        self.elementoActual += 1
        self.ControlDeBotones()

    def ControlDeBotones(self):
        if self.elementoActual == 0:
            self.btn1.Enable(False)

            if self.elementoActual == len(self.ventanaPrincipal.listaJuegos) - 1:
                self.btn2.Enable(False)
            else:
                self.btn2.Enable(True)

        else:
            self.btn1.Enable(True)

            if self.elementoActual == len(self.ventanaPrincipal.listaJuegos) - 1:
                self.btn2.Enable(False)
            else:
                self.btn2.Enable(True)

    def MostrarPrimero(self):
        self.elementoActual = 0
        self.MostrarDatos(self.elementoActual)
        self.ControlDeBotones()
        

    def MostrarDatos(self, pos):

        row = self.ventanaPrincipal.listaJuegos[pos]
        
        self.textTitulo.SetValue(row[0])
        self.textPubli.SetValue(row[1])
        self.textPre.SetValue(row[2])

    def OnBorrar(self, event):
        decision = wx.MessageBox("Esta seguro de eliminar este elemento?", "Borrar", wx.OK | wx.CANCEL | wx.ICON_QUESTION)

        if int(decision) == 4:
            
            self.ventanaPrincipal.listaJuegos.pop(self.elementoActual)

            if self.elementoActual == len(self.ventanaPrincipal.listaJuegos):
                self.elementoActual -= 1


            if(len(self.ventanaPrincipal.listaJuegos) == 0):
                self.elementoActual = 0

                #cambiar el panel a uno vacio
                self.ventanaPrincipal.CambiarAVisualizar()
            else:
                self.MostrarDatos(self.elementoActual)
                self.ControlDeBotones()
                print(self.ventanaPrincipal.listaJuegos)
    
    def OnModificar(self, event):
        if self.DatosCorrectos():

            #modificar los campos del juego modificado
            self.ModificarLosDatos()

            wx.MessageBox("Modificacion realizada correctamente, " + 
            "guarde los datos para que se vean reflejados en el fichero", 
            "Alta correcta", wx.OK | wx.ICON_INFORMATION)
        else:
            wx.MessageBox("Datos introducidos incorrectos", "Error", wx.OK | wx.ICON_ERROR)

            #devolvemos los datos a su estado original
            self.MostrarDatos(self.elementoActual)

        
    
    def DatosCorrectos(self):
        try:
            if self.textTitulo.GetValue() != "":
                if int(self.textPubli.GetValue()) >= 1982:
                    if float(self.textPre.GetValue()) > 0:
                        return True
        except ValueError:
            return False
        
        return False
    
    def ModificarLosDatos(self):
        juego = self.ventanaPrincipal.listaJuegos[self.elementoActual]

        juego[0] = self.textTitulo.GetValue()
        juego[1] = self.textPubli.GetValue()
        juego[2] = self.textPre.GetValue()

        self.ventanaPrincipal.listaJuegos[self.elementoActual] = juego
        

class PanelAlta(wx.Panel):
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id)
        self.ventanaPrincipal = parent
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

        self.textTitulo = wx.TextCtrl(self)

        #para que no se pueda modificar
        #textTitulo.DoEnable(False)

        hboxTitulo.Add(self.textTitulo, proportion=1)

        vbox.Add(hboxTitulo, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP,  border = 10)

        vbox.Add((-1, 25))

        #anio publicacion--------------------------------------------
        hboxPubli = wx.BoxSizer(wx.HORIZONTAL)

        labPub = wx.StaticText(self, label='Anio publicacion: ')
        #labTit.SetFont(font)
        hboxPubli.Add(labPub, flag=wx.RIGHT, border=8)

        self.textPubli = wx.TextCtrl(self)

        hboxPubli.Add(self.textPubli, proportion=1)

        vbox.Add(hboxPubli, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP,  border = 10)

        vbox.Add((-1, 25))

        #precio--------------------------------------------
        hboxPrecio = wx.BoxSizer(wx.HORIZONTAL)

        labPre = wx.StaticText(self, label='Precio:                    ')
        #labTit.SetFont(font)
        hboxPrecio.Add(labPre, flag=wx.RIGHT, border=8)

        self.textPre = wx.TextCtrl(self)

        hboxPrecio.Add(self.textPre, proportion=1)

        vbox.Add(hboxPrecio, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP,  border = 10)

        vbox.Add((-1, 25))

        #botones--------------------------------------------
        hboxBotones = wx.BoxSizer(wx.HORIZONTAL)

        self.btn1 = wx.Button(self, label='Aceptar', size = (70,30))
        hboxBotones.Add(self.btn1)
        self.btn2 = wx.Button(self, label='Cancelar', size = (70,30))
        hboxBotones.Add(self.btn2)

        self.Bind(wx.EVT_BUTTON, self.DarDeAlta,  self.btn1)
        self.Bind(wx.EVT_BUTTON, self.CancelarAlta,  self.btn2)

        vbox.Add(hboxBotones, flag=wx.ALIGN_CENTER|wx.BOTTOM,  border = 10)

        self.SetSizer(vbox)
    
    def DarDeAlta(self, event):

        if self.DatosCorrectos():
            print("Datos correctos")
            nuevoJuego = []
            nuevoJuego.append(self.textTitulo.GetValue())
            nuevoJuego.append(self.textPubli.GetValue())
            nuevoJuego.append(self.textPre.GetValue())

            self.ventanaPrincipal.listaJuegos.append(nuevoJuego)
            self.ventanaPrincipal.contadorJuegos+=1

            wx.MessageBox("Alta realizada correctamente", "Alta correcta", wx.OK | wx.ICON_INFORMATION)
        else:
            wx.MessageBox("Datos introducidos incorrectos", "Error", wx.OK | wx.ICON_ERROR)

        self.ResetPanel()
    
    def DatosCorrectos(self):
        try:
            if self.textTitulo.GetValue() != "":
                if int(self.textPubli.GetValue()) >= 1982:
                    if float(self.textPre.GetValue()) > 0:
                        return True
        except ValueError:
            return False
        
        return False


    def CancelarAlta(self, event):
        self.ResetPanel()
        self.ventanaPrincipal.CambiarAVisualizar()

    def ResetPanel(self):
        self.textPre.SetValue("")
        self.textPubli.SetValue("")
        self.textTitulo.SetValue("")

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

class PanelListaVacia(wx.Panel):
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

        labNombre = wx.StaticText(self, label='Listado de videojuegos vacio')
        hboxNom.Add(labNombre, flag=wx.RIGHT, border=8)

        vbox.Add(hboxNom, flag=wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.CENTER,  border = 10)

        self.SetSizer(vbox)

class FramePrincipal(wx.Frame):
    def __init__(self, parent, title, style):
        # asegurar que se llame al __init__ de los padres
        super(FramePrincipal, self).__init__(parent, title=title,
                                        size=(450,400), style=style)
        #montamos los componentess de la ventana
        self.Initialize()
        #self.listadoJuegos

    def Initialize(self):
        
        #creamos la barra del menu
        self.CreateMenuBar()
        #creamos paneles
        self.CreatePanels()

        #colocamos el icono a la ventana
        self.icono = wx.Icon()
        self.icono.CopyFromBitmap(wx.Bitmap("icono.png", wx.BITMAP_TYPE_ANY))
        self.SetIcon(self.icono)

        #centramos en la pantalla
        self.Centre(True)
        #mostramos --no necesario realmente, pero por si acaso :)
        self.Show()

    #creamos los paneles y los añadimos a la ventana principal
    def CreatePanels(self):
        
        self.caja = wx.BoxSizer(wx.VERTICAL)

        #creamos el panel visualizar
        self.panelVisualizar = PanelVisualizar(self, -1)
        #self.CreatePanelVisualizar()

        self.panelAlta = PanelAlta(self, -1)

        self.panelBienvenida = PanelBienvenida(self, -1)

        self.panelVacio = PanelListaVacia(self, -1)

        #añadimos los paneles al frame principal
        self.caja.Add(self.panelVisualizar, 1, wx.EXPAND)
        self.caja.Add(self.panelAlta, 1, wx.EXPAND)
        self.caja.Add(self.panelBienvenida, 1, wx.EXPAND)
        self.caja.Add(self.panelVacio, 1, wx.EXPAND)

        #ocultar paneles y mostrar el que toque
        self.panelVisualizar.Hide()
        self.panelAlta.Hide()
        self.panelVacio.Hide()
        self.SetSizer(self.caja)
        self.Layout()

    def CreateMenuBar(self):
         #creamos un elemento menu para cargar/guardar archivos y salir
        self.menuArchivo = wx.Menu()

        itemLoad = self.menuArchivo.Append(-1, "Cargar Datos")

        itemSave = self.menuArchivo.Append(3, "Guardar datos")

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
        self.DesactivarBotonesBarra()

        # asignamos la barra de menu al frame
        self.SetMenuBar(barraDeMenu)
        
        #asociamos elemento del menu a una accion del sistema
        self.Bind(wx.EVT_MENU, self.OnSalir,  itemSalir)
        self.Bind(wx.EVT_MENU, self.OnVisualizar,  itemVisualizar)
        self.Bind(wx.EVT_MENU, self.OnAlta,  itemAlta)
        self.Bind(wx.EVT_MENU, self.OnLoad,  itemLoad)
        self.Bind(wx.EVT_MENU, self.OnSave,  itemSave)
    
    def ActivarBotonesBarra(self):
        self.menuPaneles.Enable(1, True)
        self.menuPaneles.Enable(2, True)

        self.menuArchivo.Enable(3, True)

    def DesactivarBotonesBarra(self):
        self.menuPaneles.Enable(1, False)
        self.menuPaneles.Enable(2, False)

        self.menuArchivo.Enable(3, False)

    #metodoque se llama al presionar el boton salir del menu
    def OnSalir(self, event):
        #self.csvfile.close()
        self.Close(True)
    
    def OnVisualizar(self, event):
        self.CambiarAVisualizar()
        
    def OnAlta(self, event):
        self.CambiarAAlta()

    def OnLoad(self, event):
        openFileDialog = wx.FileDialog(None, message='Cargar el archivo csv.',
            wildcard='CSV (*.csv)|*.csv|All Files|*',
            style=wx.FD_OPEN)

        try:
            if openFileDialog.ShowModal() == wx.ID_CANCEL:
                return wx.ID_CANCEL
        except Exception:
            wx.LogError('Save failed!')
            raise
        
        self.path = openFileDialog.GetPath()
        
        try:
            self.csvfile = open(self.path, newline='')
            self.datos = csv.reader(self.csvfile, delimiter=',', quotechar='|')

            #contamos cuantos elementos tiene el fichero
            self.contadorJuegos = 0
            self.listaJuegos = []

            for row in self.datos:
                print(row[0])
                #aniadimos el campo a la lista
                self.listaJuegos.append(row)
                self.contadorJuegos+=1
            #print("El listado contiene " + str(self.contadorJuegos) + " juegos")
            self.CambiarAVisualizar()
            self.ActivarBotonesBarra()

            wx.MessageBox("Carga correcta", "Carga de datos", wx.OK | wx.CANCEL | wx.ICON_INFORMATION)
            
            #4 = ok, 16 = cancel
            #print(var)
            self.csvfile.close()
        except:
            wx.MessageBox("No se ha podido cargar el fichero", "Error", wx.OK | wx.ICON_ERROR)

        openFileDialog.Destroy()

    def CambiarAVisualizar(self):
        
        if len(self.listaJuegos) > 0:
            self.panelVisualizar.Show()
            self.panelAlta.Hide()
            self.panelBienvenida.Hide()
            self.panelVacio.Hide()

            self.panelVisualizar.MostrarPrimero()
        else:
            self.panelVisualizar.Hide()
            self.panelAlta.Hide()
            self.panelBienvenida.Hide()
            self.panelVacio.Show()

        self.Layout()

    def CambiarAAlta(self):
        self.panelAlta.Show()
        self.panelVisualizar.Hide()
        self.panelBienvenida.Hide()
        self.panelVacio.Hide()

        self.Layout()

    def OnSave(self, event):
        openFileDialog = wx.FileDialog(None, message='Seleccionar archivo csv. para guardar',
            wildcard='CSV (*.csv)|*.csv|All Files|*',
            style=wx.FD_OPEN)

        #print(self.listaJuegos)

        try:
            if openFileDialog.ShowModal() == wx.ID_CANCEL:
                return wx.ID_CANCEL
        except Exception:
            wx.LogError('Save failed!')
            raise
        
        self.path = openFileDialog.GetPath()
        
        try:
            myFile = open(self.path, 'w', newline='')
            with myFile:
                writer = csv.writer(myFile)
                
                writer.writerows(self.listaJuegos)

            myFile.close()
            wx.MessageBox("Guardado correcto", "Guardar datos", wx.OK | wx.ICON_INFORMATION)
        except:
            wx.MessageBox("No se ha podido guardar el fichero", "Error", wx.OK | wx.ICON_ERROR)

        openFileDialog.Destroy()
        


if __name__ == '__main__':
    # Cuando este modulo se ejecuta (no se importa), crear la aplicacion,
    # el frame, mostrarlo e iniciar el bucle de eventos.
    app = wx.App()

    estilo = wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX

    frm = FramePrincipal(None, title='Gestion de videojuegos', style=estilo)
    frm.Show()
    app.MainLoop()