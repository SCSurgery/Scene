# -*- coding: UTF-8 -*-
from __main__ import vtk, qt, ctk, slicer


class Scene:
  def __init__(self, parent):
    parent.title = "Manipular scenes"
    parent.categories = ["Ejemplos"]
    parent.dependencies = []
    parent.contributors = ["Camilo Quiceno Q"] # replace with "Firstname Lastname (Org)"
    parent.helpText = """
    Este modulo sirve para cambiar el layout del slicer
    """
    parent.acknowledgementText = """
    Desarrollado por Camilo Quiceno 
    """ # replace with organization, grant and thanks.
    self.parent = parent

#
# qHelloPythonWidget
#

class SceneWidget:
  def __init__(self, parent = None):
    if not parent:
      self.parent = slicer.qMRMLWidget()
      self.parent.setLayout(qt.QVBoxLayout())
      self.parent.setMRMLScene(slicer.mrmlScene)
    else:
      self.parent = parent
    self.layout = self.parent.layout()
    if not parent:
      self.setup()
      self.parent.show()

  def setup(self):
    # Instantiate and connect widgets ...

    # Collapsible button
    sampleCollapsibleButton = ctk.ctkCollapsibleButton()
    sampleCollapsibleButton.text = "A collapsible button"
    self.layout.addWidget(sampleCollapsibleButton)

    # Layout within the sample collapsible button
    sampleFormLayout = qt.QFormLayout(sampleCollapsibleButton)
    self.layout.addStretch(1)
    labelSeleccionCargarGuardar = qt.QLabel("Desea cargar o guardar? ") #Se crea label para seleccion de tornillo a manipular
    sampleFormLayout.addWidget(labelSeleccionCargarGuardar) #Se añade label
 
    self.comboBoxSeleccionCargarGuardar = qt.QComboBox() #Se crea comboBox para seleccionar tornillo
    self.comboBoxSeleccionCargarGuardar.addItem("Cargar Scene") #Se añade opciones
    self.comboBoxSeleccionCargarGuardar.addItem("Guardar Scene")
    sampleFormLayout.addWidget(self.comboBoxSeleccionCargarGuardar)



    labelNombreScene = qt.QLabel("Nombre: ") #Se crea label para seleccion de tornillo a manipular
    sampleFormLayout.addWidget(labelNombreScene)

    self.nombreSceceTextEdit = qt.QLineEdit()
   
    self.nombreSceceTextEdit.textChanged.connect(self.textchanged1)
    sampleFormLayout.addWidget(self.nombreSceceTextEdit)

    self.cargarGuardarButton = qt.QPushButton("Cargar/Guardar Scene") #Se crea boton pulsable, con texto "Apply"
    sampleFormLayout.addWidget(self.cargarGuardarButton) #Se añade el boton al layout del boton colapsable
    self.cargarGuardarButton.connect('clicked(bool)',self.onApply3)



  def textchanged1(self,text):
      self.name = text

  def onApply3(self):
    if self.comboBoxSeleccionCargarGuardar.currentIndex == 0:
        try:
            print ("Cargaste: " + self.name)
        except(AttributeError):
            qt.QMessageBox.critical(slicer.util.mainWindow(),'Error cargar/guardar', 'Espacio en blanco')


    else:
        try:
            print ("Gurdaste: " + self.name)
            
        except(AttributeError):
            qt.QMessageBox.critical(slicer.util.mainWindow(),'Error cargar/guardar', 'Espacio en blanco')
    

