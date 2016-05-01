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

    ########################
    # Add tutorial code here
    ########################
    
    # Add vertical spacer
    self.layout.addStretch(1)

    # Set local var as instance attribute
    self.helloWorldButton = helloWorldButton

  def onHelloWorldButtonClicked(self):
    print "Hello World !"

    ########################
    # Add tutorial code here
    ########################

