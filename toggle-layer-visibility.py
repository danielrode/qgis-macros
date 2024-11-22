from qgis.PyQt.QtGui import QKeySequence
from qgis.PyQt.QtWidgets import QShortcut
from qgis.PyQt.QtCore import Qt

from qgis.utils import iface
from qgis.core import QgsProject

def openProject():

    def toggle_layer_visibility(layer_tag):
        layers = QgsProject.instance().mapLayers().values()
        for l in layers:
            if not l.name().endswith(layer_tag):
                continue
     
            l = QgsProject.instance().layerTreeRoot().findLayer(l)
            if l.itemVisibilityChecked():
                l.setItemVisibilityChecked(False)
            else:
                l.setItemVisibilityChecked(True)

    # Make sure the shortcuts you pick below are not already being used
    # somewhere else (look under Settings > Keyboard Shortcuts...)
    # Other keyboard shortcut combo example:
    # QKeySequence(Qt.ControlModifier + Qt.ShiftModifier + Qt.Key_1)
    bind_layertag_map = (
        (Qt.Key_F1, '<f1>'),
        (Qt.Key_F1 + Qt.ShiftModifier, '<s-f1>'),
        # (Qt.Key_F2, '<f2>'),
        (Qt.Key_F2 + Qt.ShiftModifier, '<s-f2>'),
        (Qt.Key_F3, '<f3>'),
        (Qt.Key_F3 + Qt.ShiftModifier, '<s-f3>'),
    )

    for bind, tag in bind_layertag_map:
        shortcut = QShortcut(QKeySequence(bind), iface.mainWindow())
        shortcut.setContext(Qt.ApplicationShortcut)
         # To understand reason for this convoluted lambda syntax, see 
         # https://stackoverflow.com/questions/19837486/lambda-in-a-loop
        callback_func = (lambda t: lambda: toggle_layer_visibility(t))(tag)
        shortcut.activated.connect(callback_func)

def saveProject():
    pass

def closeProject():
    pass
