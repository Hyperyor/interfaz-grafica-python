
import wx

#pylint: disable=maybe-no-member

class HolaFrame(wx.Frame):
    """
    Un frame que dice hola mundo
    """

    def __init__(self, *args, **kw):
        # asegurar que se llame al __init__ de los padres
        super(HolaFrame, self).__init__(*args, **kw)

        # crear un panel en el marco
        panel = wx.Panel(self)

        # poner un texto con una fuente en negrita m�s grande
        textoFijo = wx.StaticText(panel, label="Hola Mundo!")
        fuente = textoFijo.GetFont()
        fuente.PointSize += 10
        fuente = fuente.Bold()
        textoFijo.SetFont(fuente)

        # y crear un organizador para administrar el dise�o de widgets secundarios
        organizador = wx.BoxSizer(wx.VERTICAL)
        organizador.Add(textoFijo, wx.SizerFlags().Border(wx.TOP|wx.LEFT, 25))
        panel.SetSizer(organizador)

        # crear una barra de men�
        self.crearBarraDeMenu()
        # y una barra de estado
        self.CreateStatusBar()
        self.SetStatusText("Bienvenido a wxPython!")


    def crearBarraDeMenu(self):
        """
        Una barra de men� se compone de men�s, que se componen de elementos de men�.
        Este m�todo crea un conjunto de men�s y enlaza los controladores que se llamar�n
        cuando se selecciona el elemento del men�.
        """

        # Crear un men� de archivo con elementos Hola y Salir
        menuArchivo = wx.Menu()
        # La sintaxis "\t..." define una clave de acelerador que tambi�n activa 
        # el mismo evento
        itemHola = menuArchivo.Append(-1, "&Hola...\tCtrl-H",
                "Cadena de ayuda mostrada en la barra de estado para este elemento del men�")
        menuArchivo.AppendSeparator()
        # Al usar una ID estandar, no necesitamos especificar la etiqueta del elemento
        # del men�
        itemSalir = menuArchivo.Append(wx.ID_EXIT)

        # Ahora un men� de ayuda para el Acerca de
        menuInfo = wx.Menu()
        itemAcercaDe = menuInfo.Append(wx.ID_ABOUT)

        # Crear la barra de men� y agr�garle los dos men�s. El '&' define
        # que la siguiente letra es el "mnemot�cnico" para el elemento del men�. 
        # En las plataformas que lo soportan, esas letras est�n subrayadas y pueden usarse 
        # para abrir el men� desde el teclado.
        barraDeMenu = wx.MenuBar()
        barraDeMenu.Append(menuArchivo, "A&rchivo")
        barraDeMenu.Append(menuInfo, "&Info")

        # Asignar la barra de men� al marco
        self.SetMenuBar(barraDeMenu)

        # Finalmente, asociar una funci�n de controlador con el evento EVT_MENU
        # para cada uno de los elementos del men�. Eso significa que cuando ese
        # elemento del men� es activado, se llamar� a la funci�n de controlador
        # asociada.
        self.Bind(wx.EVT_MENU, self.OnHola, itemHola)
        self.Bind(wx.EVT_MENU, self.OnSalir,  itemSalir)
        self.Bind(wx.EVT_MENU, self.OnSobre, itemAcercaDe)


    def OnSalir(self, event):
        """Cierrar el frame, finalizando la aplicaci�n."""
        self.Close(True)


    def OnHola(self, event):
        """Saludar al usuario."""
        wx.MessageBox ("Hola de nuevo desde wxPython")


    def OnSobre(self, event):
        """Mostrar un cuadro de di�logo Acerca de"""
        wx.MessageBox("Este es un ejemplo de Hola Mundo en wxPython",
                      "Sobre Hola Mundo",
                      wx.OK|wx.ICON_INFORMATION)


if __name__ == '__main__':
    # Cuando este m�dulo se ejecuta (no se importa), crear la aplicaci�n,
    # el frame, mostrarlo e iniciar el bucle de eventos.
    app = wx.App()
    frm = HolaFrame(None, title='Hola Mundo')
    frm.Show()
    app.MainLoop()