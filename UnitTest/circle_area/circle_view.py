import ui
from circle import area

def btn_area_onclick(sender):
  view = sender.superview
  larea = view['lbl_area']
  tradius = view['txt_radius']
  larea.text = str(area(float(tradius.text)))
    
    
v = ui.load_view()
v.present('sheet')

